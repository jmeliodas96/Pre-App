# !/usr/bin/python
# Script by Jimmy Mena


# dependences
import subprocess
import os
import argparse

# try this
try:
    # constant
    createdir1 = 'mkdir /home/'
    createdir2 = '/packages/apps/'
    show       = '/home/'
    slash      = '/'
    areyousure = ''

    parser = argparse.ArgumentParser(description='commands for execute task on server')
    # Declare an argument (`--algo`), telling that the corresponding value should be stored in the `algo` field, and using a default value if the argument isn't given
    parser.add_argument('--algo', action="store", dest='dir', default=0)

    parser.add_argument('--algo2', action='store', dest='user', default=0)

    parser.add_argument('--algo4', action='store', dest='dir2', default=0)

    parser.add_argument('--algo3', action='store', dest='working', default=0)

    # Now, parse the command line arguments and store the values in the `args` variable
    args = parser.parse_args()

    # Individual arguments can be accessed as attributes...
    user    = args.user
    dir1    = args.dir
    dir2    = args.dir2
    work    = args.working

    # commands for create two directory
    command     = createdir1 + user + slash + work + createdir2 + dir1
    command1    = createdir1 + user + slash + work + createdir2 + dir2

    #list of commands
    cmd_list = [command, command1, 'uptime']

    print cmd_list

    # get outs and errors generated on execution process
    out = []
    err = []

    # for cmd in cmd_list, iter on cmd_list for execute every commands
    for cmd in cmd_list:
    args = cmd.split()
    proc = subprocess.Popen(args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    (stdoutdata, stderrdata) = proc.communicate()
    out.append(stdoutdata)
    err.append(stderrdata)
    
    print 'out=',out
    print 'err=',err

except Exception as e:
    print ' __error__  ',e
