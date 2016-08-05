@echo off
python Python_Language\crawler.py -k water -p Download -n 10 
python Python_Language\crawler.py -k apple -p Download -n 10 -o "[size:medium; type:clip; rights:fc]"

pause
