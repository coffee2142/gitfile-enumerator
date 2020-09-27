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
                try:
                    open("done/"+str(sd+zd),"w").write(str(output.decode('utf-8')))
                    print(sd+zd)
                except UnicodeDecodeError:
                     print("Failed to decode")
