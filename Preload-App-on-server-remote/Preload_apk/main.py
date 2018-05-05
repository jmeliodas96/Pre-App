# Main content, this call to other script for execute task
# by Jimmy Mena
#!/usr/bin/python
# from __main__ import *
import subprocess
import sched
import datetime
import time
import os

scheduler = sched.scheduler(time.time, time.sleep)

# credentials

USER            =   ''
HOST            =   ''
PASSWORD        =   ''

# case password -> constant
sshpass     = 'sshpass -p '
log         = ' >> mylog.txt 2>&1'
command0    = ' python < create_one.py --user '
command8    = ' --dir '
command9    = ' --work '
command7    = ' python < create_one.py --algo '
command5    = ' python < create_d.py >> mylog.txt 2>&1'
ssh         = ' ssh '
charact     = '@'

# question to users
response    = ''
response1   = ''

# case file key.pem -> constant
scp                 =   'scp -i '
sshkey              =   'ssh -i '
charact1            =   '@'
charact2            =   ':'
DIR_KEY_FILE        =   ''
DIR_FILE_UPLOAD     =   ''
DIR_UPLOAD          =   ''
SPACE               =   ' '
WORKING             =   ''
# WORKING_DIRECTORY_6_0_1_N5



# name of new directorys to create
DIR1    = ''
DIR2    = ''
AMOUNT_DIRECTORYS= 0

# accounters
i = 0

try:

    # start and welcome to user
    print '\n'
    print ("                                                IMOX TECHNOLOGIES                 ")
    print "             Welcome to Script for preload WIN Platform APKs : The Date is : ", str(datetime.datetime.now())
    print '----------------------------------------------------------------------------------------------------------------'
    print '                 Before starting , make sure you have the APKs are required for installation.'
    print '\n'

    response = raw_input("      What type of Authentication do you go to use, write 'p' for password or 'k' for key.pem file : ")

    if(response == 'p'):

        print '\n'
        # response1     =   raw_input("      Do you need to upload a file, write 'yes' for upload or 'not' for not upload files : ")
        print '     -To preload the apks we need to create news directories in the following location : /packages/apps/ directory.'
        print '     -with names that serve as reference to the files apks.'
        #
        # # convert to int
        AMOUNT_DIRECTORYS   =   int(raw_input('     -How many directories do you need to create : '))

        if(AMOUNT_DIRECTORYS <= 0):
            print "Do not to create news directories."

        elif(AMOUNT_DIRECTORYS > 0 and AMOUNT_DIRECTORYS < 2):
            print 'Create one directories.'

        elif(AMOUNT_DIRECTORYS > 1):
            print '     -Create two directories.'

            # asking for parameters to connect server user ODM
            print '\n'
            print '         Insert your Credentials for connect to server and preload files : '
            USER            =   raw_input('         Insert UserName   : ')
            HOST            =   raw_input('         Insert Host       : ')
            PASSWORD        =   raw_input('         Insert Password   : ')

            # build a command
            command1 = sshpass + PASSWORD + ssh + USER + charact + HOST + command5
            print '\n'
            # print '         : ',command1
            # execute instruction
            os.system(command1)
            print '        -The directories were created successfully.'

            # importing second Script
            # import test_a

    elif(response == 'k'):

        print '\n'
        print '     -To preload the apks we need to create news directories in the following location : /packages/apps/ directory.'
        print '     -with names that serve as reference to the files apks.'

        # convert to int
        AMOUNT_DIRECTORYS   =   int(raw_input('     -How many directorys do you need to create : '))

        if(AMOUNT_DIRECTORYS <= 0):
            print "Do not to create news directorys."

        elif(AMOUNT_DIRECTORYS > 0 and AMOUNT_DIRECTORYS < 2):
            print 'Create one directory.'

        elif(AMOUNT_DIRECTORYS > 1):
            print '     -Create two directorys.'

            DIR1                =   raw_input('         Insert name of directorie                           : ')
            WORKING             =   raw_input('         Insert name of Working Directories in your server   : ')

            # information
            print '\n'
            print '         Insert your Credentials for connect to server and preload files : '
            USER                =   raw_input('         Insert UserName                                                             : ')
            HOST                =   raw_input('         Insert Host                                                                 : ')
            DIR_KEY_FILE        =   raw_input('         Insert Local directory where the key.pem file is located for authentication : ')
            # DIR_FILE_UPLOAD     =   raw_input('         Insert Local directory where the files are located to upload to the server  : ')
            # DIR_UPLOAD          =   raw_input('         Insert Remote directory where do you want to upload the files               : ')



            # building commands
            # command2    = scp + DIR_KEY_FILE + SPACE + DIR_FILE_UPLOAD + SPACE + USER + charact1 + HOST + charact2 + DIR_UPLOAD + command   0

            command_last    = command0 + USER + command8 + DIR1 + command9 + WORKING + log

            print command_last
            command2    = sshkey + DIR_KEY_FILE + SPACE + USER + charact1 + HOST + command_last

            print '\n'
            print command2

            # execute
            os.system(command2)

        # elif(response1 == 'not'):
        #     print '\n'
        #     print '         Insert your Credentials for connect to server and preload files : '
        #     USER                =   raw_input('         Insert UserName   : ')
        #     HOST                =   raw_input('         Insert Host       : ')
        #     DIR_KEY_FILE        =   raw_input('         Insert directory where the key.pem file is located for authentication : ')
        #
        #     # build a command
        #     command3 = sshkey + DIR_KEY_FILE + SPACE + USER + charact1 + HOST + command0
        #     print '\n'
        #     print command3
        #
        #     # execute
        #     # os.system(command3)

        # end validation
    else:

        print '                 Please, choose a option!'


    # print ' -> ',command1
    # os.system('sshpass \'{PASSWORD}\' ssh \'{USER}\'@\'{HOST}\' python < test_a.py >> mylog.txt 2>&1')

except Exception as e:
    print '__error__ ',e


# importing other script
# from test_a import *
