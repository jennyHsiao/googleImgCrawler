@echo off
call py2 crawler.py -k restaurant -p C:\Users\JennyCL_Hsiao\Documents\gImg -n 0 
call py2 crawler.py -k room -p C:\Users\JennyCL_Hsiao\Documents\gImg -n 0 -o "[size:medium; type:clip; rights:fc]"
call py2 crawler.py -k "mickey mouse" -p C:\Users\JennyCL_Hsiao\Documents\gImg -n 30 -o "[size:icon]"
call py2 crawler.py -k "hello kitty" -p C:\Users\JennyCL_Hsiao\Documents\gImg -n 10 -o "[size:large]"
call py2 crawler.py -k milk -p C:\Users\JennyCL_Hsiao\Documents\gImg -n 0 -o "[size:icon; type:face; rights:fc]"
call py2 crawler.py -k watch -p C:\Users\JennyCL_Hsiao\Documents\gImg -n 0 -o "[type:line; rights:fc]"
call py2 crawler.py -k bag -p C:\Users\JennyCL_Hsiao\Documents\gImg -n 0 -o "[type:photo; rights:f]"
call py2 crawler.py -k spoon -p C:\Users\JennyCL_Hsiao\Documents\gImg -n 0 -o "[type:line; rights:f]"
call py2 crawler.py -k snoopy -p C:\Users\JennyCL_Hsiao\Documents\gImg -n 0
call py2 crawler.py -k shoes -p C:\Users\JennyCL_Hsiao\Documents\gImg -n 0 -o "[type:animated; rights:fmc]"
call py2 crawler.py -k banana -p C:\Users\JennyCL_Hsiao\Documents\gImg -n 0 

pause
