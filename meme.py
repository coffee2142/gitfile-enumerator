# make sure you have a folder called "done" in the current directory
# just go to /.git/objects/, make folder called done, and run


import os
import subprocess
from subprocess import PIPE

dank = next(os.walk('.'))[1]

for d in dank:
        dd = next(os.walk(d))
        sd = dd[0]
        od = dd[2]
        for zd in od:
                p = subprocess.Popen(['git','cat-file','-p',str(sd+zd)],stdin=PIPE,stdout=PIPE,stderr=PIPE)
                output, err = p.communicate()
                open("done/"+str(sd+zd),"w").write(str(output))
                print(sd+zd)
