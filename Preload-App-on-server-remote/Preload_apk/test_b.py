# dependences
import sys, os
import datetime
import time
import sched


# credentials server
DIR_KEY_FILE    =   ''
USER            =   ''
HOST            =   ''
PASSWORD        =   ''

# constant
commands = ""

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

for i in sys.argv[1:]:
        commands += " " + i;

if len(sys.argv) <= 1:
        command0 = 'sshpass -p {0} ssh {1}@{2}'.format(PASSWORD,USER,HOST)
        # os.system("sshpass -p \'{0}\' ssh \'{1}\'@\'{2}\'".format(PASSWORD,USER,HOST))
        os.system(command0)
else:
        # os.system("sshpass -p \'101196\' ssh serch@10.11.10.63" + commands)
        command0 = 'sshpass -p {0} ssh {1}@{2}'.format(PASSWORD,USER,HOST)
        command1 = 'mkdir /home/serch/packages/Apps'
        os.system(command0 + command1 + commands)

        # os.system(command1 + commands)
