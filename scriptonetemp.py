

import os
os.system('echo 3 | sudo tee /proc/sys/vm/drop_caches >/dev/null 2>&1')
os.system('cupsfilter demofile2.txt > demofile2.pdf')
os.system('open demofile2.pdf')
os.system('rm demofile2.txt')
os.system('rm demofile2.pdf')
