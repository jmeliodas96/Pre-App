# #!/usr/bin/python
import subprocess
import sched
import datetime
import time
import os
import argparse

# constant

createdir1 = 'mkdir /home/'
createdir2 = '/packages/apps/'
show       = '/home/'
slash      = '/'
areyousure = ''
# cmd_list = ['mkdir /home/serch/packages/HelperPruebaScript', 'uptime']

parser = argparse.ArgumentParser(description='Short sample app')
# Declare an argument (`--algo`), telling that the corresponding value should be stored in the `algo` field, and using a default value if the argument isn't given
parser.add_argument('--dir', action="store", dest='dir', default=0)

parser.add_argument('--user', action='store', dest='user', default=0)

parser.add_argument('--work', action='store', dest='working', default=0)
# Now, parse the command line arguments and store the values in the `args` variable
args = parser.parse_args()
# Individual arguments can be accessed as attributes...
user    = args.user
dir1    = args.dir
work    = args.working


command         = createdir1 + user + slash + work + createdir2 + dir1
# command1        = show + user + slash + work + createdir2 + dir1



# print 'Directories created : ',command1
# areyousure = raw_input("The directories were created, its correctly path, write 'y' if is correctly or 'n' if not : ")
# if(areyousure == 'y'):
#     print 'Ok.'
# else:
#     print 'so what its?'

# cmd_list = ['mkdir /home/ubuntu/WORKING_DIRECTORY_6_0_1_N5/packages/apps/{DIR1}', 'uptime']
cmd_list = [command, 'uptime']


print cmd_list

out = []
err = []

for cmd in cmd_list:
    args = cmd.split()
    # print ' -> ',args
    proc = subprocess.Popen(args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    (stdoutdata, stderrdata) = proc.communicate()
    out.append(stdoutdata)
    err.append(stderrdata)

print 'out=',out
print 'err=',err
