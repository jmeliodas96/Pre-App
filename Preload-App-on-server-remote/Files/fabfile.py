# from fabric.api import run, env
#
# env.hosts = ['host1', 'host2']
#
# def taskA():
#     run('ls')
#
# def taskB():
#     run('whoami')
from fabric.api import run

def host_type():
    run('uname -s')
