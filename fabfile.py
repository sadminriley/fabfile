#!/usr/bin/env python
import os
import sys
from fabric import state
from fabric.colors import *
from fabric.api import *
from fabric.contrib.console import *

__author__ = "Riley - riley@fasterdevops.com" 
__version__ = "0.1"

# Fab roles and settings

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
    sudo("service %s restart" % (svc))

@task
def psaux(grep):
    """
    Runs ps aux|grep on provided input
    """
    auxer = sudo("ps aux|grep %s" % grep)
    logme(green("ps aux returned: \n") + str(auxer))
