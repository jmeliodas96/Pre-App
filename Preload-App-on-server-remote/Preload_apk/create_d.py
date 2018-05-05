# #!/usr/bin/python
import subprocess
import os
from __main__

# constant
cmd_list = ['mkdir /home/serch/packages/apps/Helper','mkdir /home/serch/packages/apps/Fota','uptime']

# cmd_list = ['mkdir /home/serch/packages/Helper', 'uptime']

print cmd_list

out = []
err = []

for cmd in cmd_list:
    args = cmd.split()
    print ' -> ',args
    proc = subprocess.Popen(args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    (stdoutdata, stderrdata) = proc.communicate()
    out.append(stdoutdata)
    err.append(stderrdata)

print 'out=',out
print 'err=',err
