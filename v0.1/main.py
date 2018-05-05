#!/usr/bin/python
# by Jimmy Mena

# dependences
import subprocess
import sched
import datetime
import time
import os
import re

# get current date
scheduler = sched.scheduler(time.time, time.sleep)

# credentials
USER            =   ''
HOST            =   ''
PASSWORD        =   ''

# case password -> constant
sshpass     = 'sshpass -p '

# parameters for build commands
log         = ' >> mylog.txt 2>&1'
command0    = ' python create_one.py --algo '
command8    = ' --algo2 '
command9    = ' --algo3 '
command10   = ' --algo4 '

# others
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

"""
    start functions
"""

# if user use password
def ask_password():
    print '\n'
    print '     -To preload the apks we need to create news directories in the following location : /packages/apps/ directory.'

    # asking for parameters to connect server user
    print '\n'
    print '         Insert your Credentials for connect to server and preload files : '
    USER            =   raw_input('         Insert UserName   : ')
    HOST            =   raw_input('         Insert Host       : ')
    PASSWORD        =   raw_input('         Insert Password   : ')

    # build a command
    command1 = sshpass + PASSWORD + ssh + USER + charact + HOST + command5

    # execute instruction
    try:
        # os.system(command1)
        message = '        -The directories were created successfully.'
        return message

    except Exception as e:
        return e

# get current working directorie
def getcwd():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return dir_path

# get all files in subdirectories with extension .mk
def getallfiles(extension):
    dirpath = getcwd()
    result = [os.path.join(dp, f) for dp, dn, filenames in os.walk(dirpath) for f in filenames if os.path.splitext(f)[1] == extension]
    return result

# read the files found in subdirectories
def read_files_mk(dirfile,sizefile):
    i = 0
    for i in range(sizefile):
        f= open(dirfile[i],"r")
        if (f.mode == "r"):
            out =  f.read()
            print out
        else:
            print 'no its read'

# path_script function get all files with extension .py .mk .apk
def path_script():
    find = ['.py','.mk','.apk']
    # find = ['.py','.mk']
    sizefind = len(find)
    j = 0
    for j in range(sizefind):
        extension   =   find[j]
        files       =   getallfiles(extension)
        sizefile    =   len(files)

        # parse list of dirpath
        path_re = re.compile('[a-z]+_[a-z]+.*')
        dirpath_list = []
        print '------'
        k = 0
        for k in range(sizefile):
            path_search = path_re.search(files[k])
            # if path_search return a object match
            if path_search:
                script_load = files[k]
                return script_load

# get_list_files function get the only list of .mk .apk path files
def get_list_files():
    content     = []
    find = ['.mk','.apk']
    sizefind = len(find)

    j = 0
    for j in range(sizefind):
        extension   =   find[j]
        files       =   getallfiles(extension)
        sizefile    =   len(files)
        k = 0
        for k in range(sizefile):
            # print files[k]
            content.append(files[k])
    return content

# mk_list function get all files .mk
def mk_list():
    content = get_list_files()
    mk      = []
    mk_re   = re.compile('.[a-z]+.[d]+.[m]+.-*')
    sizecontent = len(content)

    d = 0
    # iter on mk
    for d in range(sizecontent):
        mk_search = mk_re.search(content[d])
        if mk_search:
            mk.append(content[d])
    return mk

# apk_list function get all files .mk
def apk_list():
    # get list of files from function get_list_files()
    content = get_list_files()
    apk     = []
    apk_re  = re.compile('.[a]+[p]+[k].*')
    sizecontent = len(content)

    d = 0
    # iter on apk
    for d in range(sizecontent):
        apk_search = apk_re.search(content[d])
        if apk_search:
            apk.append(content[d])
    return apk


"""Try this baby :)"""
try:

    # start and welcome to user
    print '\n'
    print ("                                                IMOX TECHNOLOGIES                 ")
    print "             Welcome to Script for preload WIN Platform APKs : The Date is : ", str(datetime.datetime.now())
    print '----------------------------------------------------------------------------------------------------------------'
    print '                 Before starting , make sure you have the APKs are required for installation.'
    print '\n'

    response = raw_input("           What type of Authentication do you go to use, write Password or Key [P/K]: ")

    if(response == 'p' or response == 'P'):
        # call to function ask_password()
        pwd_response = ask_password()
        print pwd_response

    elif(response == 'k' or response == 'K'):
        print '     -To preload the apks we need to create news directory in the following location : /packages/apps/ directory.'
        print '\n'
        # WORKING_DIRECTORY_6_0_N5
        WORKING             =   raw_input('         Insert name of Working Directory in your server         : ')

        # get name of directory based on names of apks file
        namesapk = apk_list()
        sizename = len(namesapk)
        for j0 in range(sizename):
            print namesapk[j0]

        # DIR1                =   raw_input('         Insert name for first directory                         : ')
        # DIR2                =   raw_input('         Insert name for second directory                        : ')
        #
        # # information
        # print '\n'
        # print '         Insert your Credentials for connect to server and preload files : '
        # USER                =   raw_input('         Insert UserName                                                                 : ')
        # HOST                =   raw_input('         Insert Host                                                                     : ')
        # DIR_KEY_FILE        =   raw_input('         Insert local directory where the key.pem file is located for authentication     : ')
        #
        #
        # # building commands for create two directory
        # command_last    = command0 + DIR1 + command8 + USER + command10 + DIR2 + command9 + WORKING + log
        #
        # # string add
        # s           = '/home/'
        # dirserver1  = '/packages/apps/'
        # slash       = '/'
        #
        # # paths for load files in server
        # dirserver   = s + USER
        # dirserver0  = s + USER + slash
        # dirserver2  = dirserver0 + WORKING + dirserver1 + DIR1
        # dirserver3  = dirserver0 + WORKING + dirserver1 + DIR2
        #
        # # get the path of script
        # path = path_script()
        # # get the path of files .mk extension
        # mkfiles     = mk_list()
        # sizemkfiles = len(mkfiles)
        # g = 0
        # # get the path of files .apk extension
        # apkfiles        = apk_list()
        # sizeapkfiles    = len(apkfiles)
        # f = 0
        #
        # """load to script file"""
        # loadfiles    = scp + DIR_KEY_FILE + SPACE + path + SPACE + USER + charact1 + HOST + charact2 + DIR_UPLOAD + dirserver
        # """Creating directorys"""
        # createdirs    = sshkey + DIR_KEY_FILE + SPACE + USER + charact1 + HOST + command_last
        # """load files .mk"""
        # for g in range(sizemkfiles):
        #     print mkfiles[g]
        #     if(g == 0):
        #         loadfirstmk1    = scp + DIR_KEY_FILE + SPACE + mkfiles[g] + SPACE + USER + charact1 + HOST + charact2 + DIR_UPLOAD + dirserver2
        #     elif(g == 1):
        #         loadfirstmk2    = scp + DIR_KEY_FILE + SPACE + mkfiles[g] + SPACE + USER + charact1 + HOST + charact2 + DIR_UPLOAD + dirserver3
        # """load files .apk"""
        # for f in range(sizeapkfiles):
        #     if(f == 0):
        #         loadfirstapk1   = scp + DIR_KEY_FILE + SPACE + apkfiles[f] + SPACE + USER + charact1 + HOST + charact2 + DIR_UPLOAD + dirserver2
        #     elif(f > 0):
        #         loadfirstapk2   = scp + DIR_KEY_FILE + SPACE + apkfiles[f] + SPACE + USER + charact1 + HOST + charact2 + DIR_UPLOAD + dirserver3
        # print '\n'
        # print loadfiles
        # print createdirs
        # print loadfirstmk1
        # print loadfirstmk2
        # print loadfirstapk1
        # print loadfirstapk2

        # ---this not-----
        # finding directories and files
        # dirfile     = getallfiles()
        # sizefile    = len(dirfile)
        # read_files_mk(dirfile,sizefile)

        # c = 0
        # # secuence for run commands
        # for c in range(6):
        #     if (c == 0):
        #         # load files in server
        #         os.system(loadfiles)
        #     elif (c > 0 and c < 2):
        #         # create new directories
        #         os.system(createdirs)
        #         print 'Directory created!!'
        #     elif (c > 1 and c < 3):
        #         os.system(loadfirstmk1)
        #         print '..ready 1'
        #     elif (c > 2 and c < 4):
        #         os.system(loadfirstmk2)
        #         print '..ready 2'
        #     elif(c > 3 and c < 5):
        #         os.system(loadfirstapk1)
        #         print '..ready 3'
        #     elif(c > 4 and c < 6):
        #         os.system(loadfirstapk2)
        #         print '..ready 4'

        print 'loading successful'


    else:
        print '        ->       Please, choose a option!'

except Exception as e:
    print '__error__ ',e
