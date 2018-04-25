import os
import psutil
import subprocess
import time
import sched
import datetime

# Server Credentials
DIR_KEY_FILE    =   ''
USER            =   ''
HOST            =   ''
PASSWORD        =   ''

# Current ssh tunnel command in the launcher:
#
# tunnel_cmd = sshBinary + " -i " + tunnelPrivateKeyFileName + " -c " + self.cipher + " " \
#     "-t -t " \
#     "-oStrictHostKeyChecking=no " \
#     "-L " + localPortNumber + ":" + remoteHost + ":" + remotePortNumber + " -l " + tunnelUsername + " " + tunnelServer

def create_tunnel(tunnel_cmd):
    ssh_process = subprocess.Popen(tunnel_cmd,  universal_newlines=True,
                                                shell=True,
                                                stdout=subprocess.PIPE,
                                                stderr=subprocess.STDOUT,
                                                stdin=subprocess.PIPE)

    # Assuming that the tunnel command has "-f" and "ExitOnForwardFailure=yes", then the
    # command will return immediately so we can check the return status with a poll().

    while True:
        p = ssh_process.poll()
        if p is not None: break
        time.sleep(1)

    if p == 0:
        # Unfortunately there is no direct way to get the pid of the spawned ssh process, so we'll find it
        # by finding a matching process using psutil.
        current_username = psutil.Process(os.getpid()).username
        ssh_processes = [proc for proc in psutil.get_process_list() if proc.cmdline == tunnel_cmd.split() and proc.username == current_username]

        if len(ssh_processes) == 1:
            return ssh_processes[0]
        else:
            raise RuntimeError, 'multiple (or zero?) tunnel ssh processes found: ' + str(ssh_processes)
    else:
        raise RuntimeError, 'Error creating tunnel: ' + str(p) + ' :: ' + str(ssh_process.stdout.readlines())



# A quick test:

# start and welcome to user
print '\n'
print ("                        IMOX TECHNOLOGIES              ")
print "Welcome to Script for preload APK's : Date is : ", str(datetime.datetime.now())
print '----------------------------------------------------------------------------'

# asking for parameters to connect server user ODM
print 'Insert your Credentials for connect to server and preload files : '
USER            =   raw_input('  Insert UserName   : ')
HOST            =   raw_input('  Insert Host       : ')
# DIR_KEY_FILE    =   raw_input('  Insert the directory where is ubicated the Key.pem file : ')
PASSWORD        =   raw_input('  Insert Password   : ')


print 'Your credentials have been taken and they are safe : '

# tunnel_cmd = 'ssh -i key.pem -o BatchMode=yes -o ServerAliveInterval=1 -o ServerAliveCountMax=5 -f -o ExitOnForwardFailure=yes -N -L 5901:localhost:5901 user@server'
tunnel_cmd = 'sshpass -p \'{0}\' ssh -o StrictHostKeyChecking=no -o BatchMode=yes -o ServerAliveInterval=1 -o ServerAliveCountMax=5 -f -o ExitOnForwardFailure=yes \'{1}\'@\'{2}\''.format(PASSWORD,USER,HOST)
# tunnel_cmd = 'sshpass -p {0} ssh -o BatchMode=yes -o ServerAliveInterval=1 -o ServerAliveCountMax=5 -o ExitOnForwardFailure=yes -N {1}@{2}'.format(PASSWORD,USER,HOST)
# tunnel_cmd = 'sshpass -p \'{0}\' ssh -o ExitOnForwardFailure=yes \'{1}\'@\'{2}\''.format(PASSWORD,USER,HOST)
try:
    ssh_tunnel_process = create_tunnel(tunnel_cmd)

    print 'made the tunnel...'
    time.sleep(5)

    ssh_tunnel_process.terminate()
    print 'terminated the tunnel'
except RuntimeError as e:
    print ":-("
print e.message
