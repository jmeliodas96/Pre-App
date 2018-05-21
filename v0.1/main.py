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

# presentation for user
def presentation():
    # start and welcome to user
    print '\n'
    print ("                                                    IMOX TECHNOLOGIES                 ")
    print "             Welcome to Script for preload WIN Platform APKs files   : ", str(datetime.datetime.now())
    print '--------------------------------------------------------------------------------------------------------------------'
    print '                 Before starting , make sure you have the APKs files that are required for preload process.'
    print '\n'

# if user use password
def ask_password():
    print '\n'
    print '     -To preload the apks we need to create news directories in the following location : /packages/apps/.'

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

# get all files in subdirectories with extension .mk and .apk
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
    # apk_re  = re.compile('.[a]+[p]+[k].*')
    apk_re  = re.compile('.[a]+[p]+[k]')

    sizecontent = len(content)

    d = 0
    # iter on apk
    for d in range(sizecontent):
        apk_search = apk_re.search(content[d])
        if apk_search:
            apk.append(content[d])
    return apk


"""functions, for parse path of directory where is located files apk and get name,
    for example : Comio_System_Helper_7.0.0_WD.apk, get System_Helper.*.*.* """
def get_helper_name(apk_path_list):
    n = 0
    sizelist = len(apk_path_list)
    re_name_apk = re.compile('.[(?y)].+[a-z].+[(0-9)].[(0-9)].[^(?WD)]')

    for n in range(sizelist):
        search_name = re_name_apk.search(apk_path_list[n])
        if search_name:
            new = apk_path_list[n]

    searchObj = re.search(re_name_apk, new)
    name = searchObj.group()
    return name

def get_fota_name(apk_path_list):
    m = 0
    sizelist = len(apk_path_list)
    re_name_apk = re.compile('.[(?O)].+[A].+[(0-9)].[(0-9)].[^(?WD)]')

    for m in range(sizelist):

        search_name = re_name_apk.search(apk_path_list[m])
        if search_name:
            new = apk_path_list[m]
    searchObj = re.search(re_name_apk, new)
    name = searchObj.group()
    return name


# parse content in mk files
def get_content_mk(out):
    new_out = []
    for out in out.split('\n'):
        new_out.append(out)

    return new_out


# read the files found in subdirectories
def read(dirfile):

    f= open(dirfile,"r")
    if (f.mode == "r"):
        out =  f.read()
        new_out_mk  =   get_content_mk(out)

    else:
        print 'no its read'
    return new_out_mk

"""
    function for show information about changes
"""
def show_information_changes(pos, content_one):
    first = []
    possize     = len(pos)
    size1       = len(content_one)
    for p in range(0,possize):
        for i in range(size1):
            if(pos[p] == i):
                fst       =   str(i) + str(SPACE) + str(charact2) + str(SPACE) + str(content_one[i])
                first.append(fst)
    return first

def send_content(dirserver2, dirserver3, mkfiles, sizemkfiles, DIR1, DIR2):
    show     =   ParseAndroidsmk(mkfiles, sizemkfiles, DIR1, DIR2)
    sizeshow = len(show)
    print '\n'
    print '         Your files will located in a new directory, into your server look like : '
    print '             First               :   ',dirserver2
    print '             Second              :   ',dirserver3
    print '\n'
    print '         The changes in files Android.mk it was  : '

    si = ''
    split = '\n'
    for g in range(0, sizemkfiles):
        # print mkfiles[g]
        if(g == 0):
            print '         For First Android.mk file, located in your local system     :  '
            for j in range(0, sizeshow):
                if(j == 0):
                    si = str(show[j])
                    size = len(si)
                    for line in si.split('['):
                        print '                                     in line',line
                        for line in si.split(']'):
                            print '                                     in line',line
        elif(g > 0):
            print '         For Second Android.mk file located in your local system      :  '
            for j in range(0, sizeshow):
                if(j > 0):
                    si = str(show[j])
                    size = len(si)
                    for line in si.split(','):
                        print '                                     in line',line
        print '\n'

"""Function ParseAndroidsmk(), this get the path of files Android.mk and open for read and parse line by line for iter over content
    and found a expression regular conditional, if its true this replace the content for information about every apk file"""
def ParseAndroidsmk(mkfiles, sizemkfiles, DIR1, DIR2):
    """
        note:
                The LOCAL_MODULE := , take the name from name of the folder content apk and mk files.
                The LOCAL_SRC_FILES :=, take the name from name of apk file.
                The LOCAL_CERTIFICATE :=, take the name from certificate information.
    """

    # variables, accounters, arrays
    i = 0
    j = 0
    g = 0
    line = '\n'
    pos     =   []
    pos2    =   []
    # Expression regular for found parameters to replace
    module_re           =   re.compile("^[A-Z].[A-Z].[A-Z].[A-Z].[A-Z].[A-Z].[ ]\B")
    src_re              =   re.compile("^[A-Z].[A-Z].[A-Z].[A-Z].[A-Z].[A-Z].[(?-SRC)].[FILES]\W")
    certificate_re      =   re.compile(".[A-Z].+[A-Z].[A-Z].[AO].[(?-F)]\W.+[:=]\B")


    # print mk_content
    for g in range(sizemkfiles):
        # print mkfiles[g]
        if(g == 0):
            first_mk = mkfiles[g]
        elif(g > 0):
            second_mk = mkfiles[g]

    # first Android.mk
    content_one =   read(first_mk)
    size1       =   len(content_one)

    # second Android.mk
    content_two =   read(second_mk)
    size2       =   len(content_two)

    # content[i]
    test1   = DIR1
    # test3   = 'K2konnect_FOTA_7.0.8_F.apk'
    # test4   = 'platform'

    # content2[j]
    # test2   = DIR2

    # certificate = []

    # new LOCAL_MODULE, this recieved a parameter, the name of folder that containing the files for every apk file
    LOCAL_MODULE        =   'LOCAL_MODULE := '
    LOCAL_SRC_FILES     =   'LOCAL_SRC_FILES := '
    # LOCAL_CERTIFICATE   =   'LOCAL_CERTIFICATE := '
    # Building news line in files Android.mk
    LOCAL_MODULE        =   LOCAL_MODULE + test1
    # LOCAL_SRC_FILES     =   LOCAL_SRC_FILES + test3
    # LOCAL_CERTIFICATE   =   LOCAL_CERTIFICATE + test4

    # reading first content
    for i in range(size1):
        new_search_mk       =   module_re.search(content_one[i])
        second_search_mk    =   certificate_re.search(content_one[i])
        three_search_mk     =   src_re.search(content_one[i])

        if new_search_mk:
            pos.append(i)
            # replace in the content in this position
            content_one[i]  = LOCAL_MODULE
        elif second_search_mk:
            # content_one[i]  =   LOCAL_CERTIFICATE
            pos.append(i)
        elif three_search_mk:
            # content_one[i]  =   LOCAL_SRC_FILES
            pos.append(i)

    # reading second content
    for j in range(size2):
        new_search_mk   =   module_re.search(content_two[j])
        second_search_mk    =   certificate_re.search(content_two[j])
        three_search_mk     =   src_re.search(content_two[j])

        if new_search_mk:
            pos2.append(j)
            # content_two[j]  =   LOCAL_SRC_FILES
        elif second_search_mk:
            pos2.append(j)
            # content_two[j]  =   LOCAL_SRC_FILES
        elif three_search_mk:
            pos2.append(j)
            # content_two[j]  =   LOCAL_SRC_FILES


    # send paramaters to show information about lines modifyed to the end-user
    first_content   =   show_information_changes(pos, content_one)
    second_content  =   show_information_changes(pos2, content_two)

    # here, hold new content to rewrite, mkfiles
    file = open('fota/Androidv1.mk','wb')
    for i in range(size1):
        file.write(content_one[i] + line)
    file.close()

    # supremo array
    father_array = []
    for h in range(0, sizemkfiles):

        if(h == 0):
            father_array.append(first_content)
        elif (h > 0):
            father_array.append(second_content)

    return father_array

def main():
    """Try this baby :)"""
    try:

        # call to presentation function
        presentation()
        response = raw_input("     -What type of Authentication do you go to use, write Password or Key [P/K]: ")

        # evaluate if user use password or Key authentication way.
        if(response == 'p' or response == 'P'):
            # call to function ask_password()
            pwd_response = ask_password()
            print pwd_response

        elif(response == 'k' or response == 'K'):
            print '     -To preload the apks we need to create news directory in the following location /packages/apps/.'
            print '\n'


            # get WORKING_DIRECTORY_6_0_N5
            WORKING             =   raw_input('         Insert name of Working Directory in your server         : ')
            # get name of directory based on names of apks file
            namesapk    = apk_list()

            # data for iter on namesapk and build the commands
            nm_apk = []
            size        = len(namesapk)
            l           = 0

            # get names for set in new directory
            helper      = get_helper_name(namesapk)
            fota        = get_fota_name(namesapk)
            # giving names for news directory
            DIR1                =   helper
            DIR2                =   fota
            # store helper and fota names in dictionary nm_apk=[]
            for l in range(size):
                if(l == 0):
                    nm_apk.append(helper)
                elif(l > 0):
                    nm_apk.append(fota)

            print nm_apk

            # information
            print '\n'
            print '         Insert your Credentials for connect to server and preload files : '
            USER                =   raw_input('         Insert UserName                                                                 : ')
            HOST                =   raw_input('         Insert Host                                                                     : ')
            DIR_KEY_FILE        =   raw_input('         Insert local directory where the key.pem file is located for authentication     : ')
            print '\n'


            # building commands for create two directory
            command_last    = command0 + DIR1 + command8 + USER + command10 + DIR2 + command9 + WORKING + log

            # string add
            s           = '/home/'
            dirserver1  = '/packages/apps/'
            slash       = '/'

            # path for load script file in server
            dirserver   = s + USER
            dirserver0  = s + USER + slash
            # path for load
            dirserver2  = dirserver0 + WORKING + dirserver1 + DIR1
            dirserver3  = dirserver0 + WORKING + dirserver1 + DIR2

            # get the path of script
            path = path_script()
            # get the path of files .mk extension
            mkfiles     = mk_list()
            sizemkfiles = len(mkfiles)
            g = 0

            # get the path of files .apk extension
            apkfiles        = apk_list()
            sizeapkfiles    = len(apkfiles)
            f = 0

            # parse data in files mk and replace the parameters and return an array of position for show to the user...
            content    =   send_content(dirserver2, dirserver3, mkfiles, sizemkfiles, DIR1, DIR2)

            """load to script file"""
            loadfiles    = scp + DIR_KEY_FILE + SPACE + path + SPACE + USER + charact1 + HOST + charact2 + DIR_UPLOAD + dirserver
            """Creating directorys"""
            createdirs    = sshkey + DIR_KEY_FILE + SPACE + USER + charact1 + HOST + command_last
            """load files .mk"""
            for g in range(sizemkfiles):
                if(g == 0):
                    loadfirstmk1    = scp + DIR_KEY_FILE + SPACE + mkfiles[g] + SPACE + USER + charact1 + HOST + charact2 + DIR_UPLOAD + dirserver2
                elif(g > 0):
                    loadfirstmk2    = scp + DIR_KEY_FILE + SPACE + mkfiles[g] + SPACE + USER + charact1 + HOST + charact2 + DIR_UPLOAD + dirserver3
            """load files .apk"""
            for f in range(sizeapkfiles):
                if(f == 0):
                    loadfirstapk1   = scp + DIR_KEY_FILE + SPACE + apkfiles[f] + SPACE + USER + charact1 + HOST + charact2 + DIR_UPLOAD + dirserver2
                elif(f > 0):
                    loadfirstapk2   = scp + DIR_KEY_FILE + SPACE + apkfiles[f] + SPACE + USER + charact1 + HOST + charact2 + DIR_UPLOAD + dirserver3

            """ Secuence for execute process and finish task """
            # c = 0
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

            print '\n'
            print '         -Preloading process successful.'
            print '\n'


        else:
            print '        ->       Please, choose a option!'

    except Exception as e:
        print '\n'
        print '         __error__ : ',e



if __name__ == '__main__':
    main()
