

import os

os.system('cupsfilter demofile2.txt > demofile2.pdf 2> /dev/null')
os.system('open demofile2.pdf')
os.system('rm demofile2.txt')
os.system('rm demofile2.pdf')
