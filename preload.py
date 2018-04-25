#   Script for preload instructions
#   IMOX TECHNOLOGIES
#   By Jimmy Mena

# dependences
import sched
import datetime
import time
import subprocess
import os


# for show the date eand hours when start the script
scheduler = sched.scheduler(time.time, time.sleep)

# Server Credentials
DIR_KEY_FILE    =   ''
USER            =   ''
HOST            =   ''
PASSWORD        =   ''
# CHARACT         =   '@'

# parameter for find the app
NAMEAPK = ''


# constant
DIR1        = '/system/priv-app'
DIR_PRUEBA  = '/home/serch/prueba/'
DIR_PRELOAD     =   '/packages/apps'



# def find_preload_files(NAMEAPK):
#
# # function for make the connection
def connecttoserver(PASSWORD,USER,HOST):


    # for connect using sshpass
    # os.putenv("%s" % '{0}').format(PASSWORD)
    # command0 = 'ssh {0}@{1}'.format(USER,HOST)
    # command0 = 'sshpass -p {0} ssh {1}@{2}'.format(PASSWORD,USER,HOST)
    command0 = 'cat ssh {0}@{1}'.format(USER,HOST)
    # cat test_a.py | ssh serch@10.11.10.63 python -

    # get ssh connection
    ssh         = subprocess.Popen(command0,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    result      = ssh.stdout.readlines()

    #if result is empty, so print the error
    if result == []:
        error = ssh.stderr.readlines()
        print error, ' __error__'

    #else, is rigth and print the connection successful
    else:
        print 'successful connection : -> ', result
        # break

    # create a directory
    ssh.stdin.write("mkdir Test_1")
    print 'folder created!'



def preload() :

    # barprogress
    end = 10
    i = 0
    sign = '/'

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
    print USER
    print HOST
    print PASSWORD

    # false
    try:
        # call to function for connect
        # connecttoserver(PASSWORD,USER,HOST)
        command0 = 'sshpass -p {0} ssh {1}@{2}'.format(PASSWORD,USER,HOST)
        # get ssh connection
        ssh         = subprocess.Popen(command0,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        result      = ssh.stdout.readlines()
        print 'ready :)'

    except:
        exit(0)
    #
    # if result == []:
    #     error = ssh.stderr.readlines()
    #     print error, ' __error__'
    #
    # #else, is rigth and print the connection successful
    # else:
    #     print 'successful connection : -> ', result
    #     # break


    # print 'Your Credentials for to connect is : ', DIR_KEY_FILE,' ', USER,'@',HOST
    # print '\n'
    # print '----------------------------------------------------------------------------'
    #
    # # asking parameters for find the files to preload (name apk and file Android.mk)
    # NAMEAPK = raw_input('Insert name of apk : ')
    # print 'To preload the APK -> ', NAMEAPK ,'and work properly, you will need to follow this instructions:'
    # print '----------------------------------------'
    # print 'The APK needs to be preloaded in',   DIR1    , 'directory.'


    # #barprogress
    # for i in range(end):
    #     print sign



preload()
