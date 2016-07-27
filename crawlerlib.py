from selenium import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
def crawlerOption(browser, option):
	if option!=None:
		options = option.split(';')
		try:
			browser.find_element_by_id('hdtb-tls').click() #Search tools
			time.sleep(1)
			for o in options:
				if 'size:' in o:
					browser.find_elements_by_class_name('hdtb-mn-hd')[0].click() #size
					if 'large' in o:
						browser.find_element_by_id('isz_l').click() #large
					if 'medium' in o:
						browser.find_element_by_id('isz_m').click() #medium
					if 'icon' in o:
						browser.find_element_by_id('isz_i').click() #icon
				if 'type' in o:
					browser.find_elements_by_class_name('hdtb-mn-hd')[2].click() #type
					if 'face' in o:
						browser.find_element_by_id('itp_face').click() #face
					if 'photo' in o:
						browser.find_element_by_id('itp_photo').click() #photo
					if 'clip' in o:
						browser.find_element_by_id('itp_clipart').click() #clip art
					if 'line' in o:
						browser.find_element_by_id('itp_lineart').click() #line drawing
					if 'animated' in o:
						browser.find_element_by_id('itp_animated').click() #animated
				if 'rights' in o:
					browser.find_elements_by_class_name('hdtb-mn-hd')[4].click() #rights
					if 'fmc' in o:
						browser.find_element_by_id('sur_fmc').click() # labeled for reuse with modification
					elif 'fc' in o:
						browser.find_element_by_id('sur_fc').click() # labeled for reuse
					elif 'fm' in o:
						browser.find_element_by_id('sur_fm').click() # labeled for noncommercial reuse with modification
					elif 'f' in o:
						browser.find_element_by_id('sur_f').click() # labeled for noncommercial reuse
		except Exception as e:
			print "EXCEPTION: ", e,"\n"
		finally:
			print "with no option setting"