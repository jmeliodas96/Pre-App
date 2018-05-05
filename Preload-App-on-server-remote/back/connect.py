import subprocess
import sys

HOST="10.11.10.63"
# Ports are handled in ~/.ssh/config since we use OpenSSH
COMMAND =   "uname -a"
USER    =   "serch"
# PASSWORD = "101196"


ssh = subprocess.Popen(["ssh", USER, "%s" % HOST, COMMAND],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)

# ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
#                        shell=False,
#                        stdout=subprocess.PIPE,
#                        stderr=subprocess.PIPE)

result = ssh.stdout.readlines()
if result == []:
    error = ssh.stderr.readlines()
    print >>sys.stderr, "ERROR: %s" % error
else:
    print result
