#!/usr/bin/env python

from subprocess import Popen, PIPE
PASSWORD    =   '101196'
HOST        =   '10.11.10.63'
USER        =   'serch'

process = Popen(['cat', 'sshpass -p '101196' ssh serch@10.11.10.63'], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()
# print stdout
