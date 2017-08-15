#!/usr/bin/env python
import os
import sys
from fabric import state
from fabric.colors import *
from fabric.api import *
from fabric.contrib.console import *

__author__ = "Riley - riley@fasterdevops.com" 
__version__ = "0.1"
"""

Fabric tasks to help with system administration
https://github.com/sadminriley/fabfile

"""

# TODO - Add fabric roles 

def logme(logstr):
    """
    helper function to provide output from fabric commands
    """
    print(white('[') + yellow(env.host_string) + white(']') + ' ' + logstr)

def sudo(cmd):
    """
    Runs all commands via sudo
    """
    return run('sudo %s' % (cmd))

@task
def uptime():
    """
    Get server uptime
    """
    theuptime = sudo("uptime")
    logme(green("Uptime is:\n") + str(theuptime))

@task
def restart(svc):
    """
    Restart a service
    """
    if not sudo("service %s restart" % (svc)).failed:
        logthis(green("restart %s successful" % (svc))
    else:
        logthis(red("Failed to restart %s" % (svc))

@task
def psaux(grep):
    """
    Runs ps aux|grep on provided input
    """
    auxer = sudo("ps aux|grep %s" % grep)
    logme(green("ps aux returned: \n") + str(auxer))

@task
def aptupdate():
    """
    Run apt-update
    """
    sudo("apt-get update")

@task
def aptupgrade():
    """
    Run apt-get upgrade. Be sure to run apt-get update with aptupdate first
    """
    sudo("apt-get upgrade")

@task 
def aptinstall(pkgname):
    """
    Install a package with apt-get install 
    """
    aptin = sudo("apt install %s" % pkgname)
    logme(green("apt install returned: \n") + str(aptin))

@task
def aptremove(pkgname):
    """
    Remove a package using apt
    """
    aptremove = sudo("apt remove %s" % pkgname)
    logme(green("apt remove returned: \n") + str(aptremove))

