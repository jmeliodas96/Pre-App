# import sys
# print "This is the name of the script: ", sys.argv[0]
# print "Number of arguments: ", len(sys.argv)
# print "The arguments are: " , str(sys.argv)

import argparse
# Define the parser
i = 0

limit = 5
command = ''

def name_directories():

    #
    # parser = argparse.ArgumentParser(description='Short sample app')
    # # Declare an argument (`--algo`), telling that the corresponding value should be stored in the `algo` field, and using a default value if the argument isn't given
    # parser.add_argument('--algo', action="store", dest='algo', default=0)
    # # Now, parse the command line arguments and store the values in the `args` variable
    # args = parser.parse_args()
    # # Individual arguments can be accessed as attributes...
    # DIR1 = args.algo
    # return DIR1
    #

    parser = argparse.ArgumentParser(description='Short sample app')
    # Declare an argument (`--algo`), telling that the corresponding value should be stored in the `algo` field, and using a default value if the argument isn't given
    parser.add_argument('--dir', action="store", dest='dir', default=0)

    parser.add_argument('--user', action='store', dest='user', default=0)
    # Now, parse the command line arguments and store the values in the `args` variable
    args = parser.parse_args()
    # Individual arguments can be accessed as attributes...
    user    = args.dir
    dir1    = args.user

    command = user + dir1

    return command

# for i in range(limit):
#     # getting string
#     # if (i == 0):
#     # get = name_directories()
#     # print get
#     # else:
#     # print '--------'
#     #

get = name_directories()
print get

# import argparse
#
# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')
#
# args = parser.parse_args()
# print args.accumulate(args.integers)
