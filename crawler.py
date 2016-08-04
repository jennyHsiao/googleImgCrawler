#-*- coding: UTF-8 -*-
import os, sys, urllib, urllib2
import ssl
from selenium import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import requests
import re
import argparse
from base64 import decodestring

import filetype as appendix
import crawlerlib

reload(sys)
sys.setdefaultencoding('utf8')

def get_img(imgurl):
	header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
	context = ssl._create_unverified_context()
	request = urllib2.Request(imgurl, headers = header)
	return urllib2.urlopen(request, context=context)

def getThumbnail(imgurl,count):
	if 'gstatic.com' in imgurl:
		res = get_img(imgurl)
		imgType = res.info().type.split('/')
		filename = keyword+"_"+str(count)+"_timg."+appendix.imgTypeMap(imgType[1])
		try:
			# urllib.urlretrieve(imgurl, filename)	
			raw_img = get_img(imgurl).read()
			img_file = open(filename, 'wb')
			img_file.write(raw_img)
			img_file.close()
		except Exception as e:
			print e, imgurl
			file.write(str(e)+":"+str(imgurl)+'\t'+filename+"\n")
	else:	 #data uri
		head, data = imgurl.split(',') #retrieve data uri
		gimgType = head.split(';')[0].split('/')[1]
		filename = keyword+"_"+str(count)+"_timg."+appendix.imgTypeMap(gimgType)
		ff = open(filename, 'wb')
		ff.write(data.decode('base64'))
		ff.close()
	return filename


parser = argparse.ArgumentParser(description='Example: python crawler.py -k coffee -p C:\Users\JennyCL_Hsiao\Documents\gImg\ -n numbers -o[size:large;type:face;rights:fmc]')

parser.add_argument("-k", "--keyword", help="keyword for google image searching")
parser.add_argument("-p", "--path", help="image saving path")
parser.add_argument("-n", "--number", type=int, help="number of images you need")
parser.add_argument("-o", "--option", help="Optinal request = "+
	"[size: large/medium/icon; type: face/photo/clip/line/animated; rights: fmc/fc/fm/f]")


args = parser.parse_args()

if not((args.number+1) and args.keyword and args.path):
	parser.error('No action requested, add -keyword, -path and -number')

number = args.number
# keyword = unicode(args.keyword, 'big5')
keyword = args.keyword
path = args.path

if not os.path.exists(keyword): #create folder to save download images
	os.makedirs(path+"\\"+keyword)
else:
	print "The folder "+path+"\\"+keyword+ " is already exists. Please change a path for saving images!"
	raise SystemExit

os.chdir(path+"\\"+keyword)

if ' ' in keyword: #keyword string manipulation
	query = keyword.split( )
	query='+'.join(query)

else:
	query = keyword	

url = "https://www.google.com.tw/search?&tbm=isch&q="+query
print (url)

browser = webdriver.Chrome()
browser.get(url)
if args.option:
	option = args.option
	crawlerlib.crawlerOption(browser, option) #-options setting

pause = 0
if(number>100 or number==0):
	# print "number==0"
	nowcnt=0
	scroll=0
	lastHeight = browser.execute_script("return document.body.scrollHeight")
	while True:
	    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	    time.sleep(pause)
	    newHeight = browser.execute_script("return document.body.scrollHeight")
	    if newHeight == lastHeight:
	        break
	    lastHeight = newHeight

	img_urls = browser.find_elements_by_xpath("//a[@class='rg_l']")
	g_img_urls = browser.find_elements_by_xpath("//img[contains(@class, 'rg_i')]")
else:
	img_urls = browser.find_elements_by_xpath("//a[@class='rg_l']")
	g_img_urls = browser.find_elements_by_xpath("//img[contains(@class, 'rg_i')]")

HttpsGeoDomain = "https://www.google.com.tw/imgres?imgurl"
HttpGeoDomain = "http://www.google.com.tw/imgres?imgurl"

file = open('imgurl.txt', 'a')
count = len(os.listdir(".")) - 1
print ("#reults = "+ str(len(img_urls))+"Gimg_urls="+str(len(g_img_urls)))
if number==0:
	number = len(img_urls)
idx = 0;
text_msg='' #record image file name successfully download
while number>idx:
	img = img_urls[idx]
	query = img.get_attribute('href')
	if query!=None:
		vars = query.split('&')
		for v in vars:
			pair = v.split('=')
			if (pair[0] == HttpsGeoDomain) or (pair[0] == HttpGeoDomain):
				imgurl = urllib.unquote(pair[1])
				# print (idx, imgurl)
				try:
					res = get_img(imgurl)  
					imgType = res.info().type.split('/')
					if res.getcode() ==200:
						if imgType[0]=='image': 		
							try:
								filename = keyword+"_"+str(count)+"."+ appendix.imgTypeMap(imgType[1])
								raw_img = get_img(imgurl).read()
								img_file = open(filename, 'wb')
								img_file.write(raw_img)
								img_file.close()
								# urllib.urlretrieve(imgurl, filename)
								text_msg = text_msg+filename+"\n"						
								count = count+1 # get img succefully, count++
							except  Exception as e: #get thumbnail
								gImg = g_img_urls[idx]
								gquery = gImg.get_attribute('src')
								filename=None
								if gquery!=None:
									filename = getThumbnail(gquery, count)
									text_msg = text_msg+filename+"\n"
									count = count+1 # get img succefully, count++
								else:
									filename = "CANNOT get thumbnail"
								file.write("ContentTooShortError: "+str(imgurl)+'\t'+filename+"\n")
						else: # get thumbnail
							gImg = g_img_urls[idx]
							gquery = gImg.get_attribute('src')
							filename=None
							if gquery!=None:
								filename = getThumbnail(gquery, count)
								text_msg = text_msg+filename+"\n"
								count = count+1 # get img succefully, count++
							else:
								filename = "CANNOT get thumbnail"
							file.write("FormatTypeException: "+str(imgurl)+"\t"+str(filename)+"\n")	
						break
				except Exception as inst:
					gImg = g_img_urls[idx]
					gquery = gImg.get_attribute('src')
					filename=None
					if gquery!=None:
						filename = getThumbnail(gquery, count)
						text_msg = text_msg+filename+"\n"
						count = count+1 # get img succefully, count++
					else:
						filename = "CANNOT get thumbnail"				
					file.write("ForbiddenError:"+str(imgurl)+"\t"+str(filename)+"\n")

	idx=idx+1

print ("Program is finished! #images ("+"keyword="+keyword+") = "+str(count)+" saved in path: "+path+"\\"+keyword+".")
file.close()	
f = open('filelist.txt', 'a')
text_msg = str(count)+"\n" + text_msg
# print text_msg
f.write(text_msg)
f.close()

browser.quit()
