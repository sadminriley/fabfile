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

def ping(host):
    """
    Ping function
    """
    try:
        import pyping
    except ImportError as e:
        import pip
        pip.main(['install', 'pyping'])
    # Not quite sure what I'm going to do with this yet, but I'll leave this here for now.
    # Potentially a helper function to ping remote hosts pre or post function execution

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
        logme(green("restart %s successful" % (svc)))
    else:
        logme(red("Failed to restart %s" % svc))

@task
def status(svc):
    """
    Check service status ouput
    """
    stat = sudo("service %s status" % (svc))
    logme(green("service %s status returned:\n") + str(stat))

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
    aptrm = sudo("apt remove %s" % pkgname)
    logme(green("apt remove returned: \n") + str(aptrm))

@task
def useradd(newuser):
    """
    Add a user to a host.
    """
    if not sudo("adduser %s" % (newuser)).failed:
        logme(green("Add user %s success!" % (newuser)))
    else:
        logme(red("Failed to adduser %s" % (newuser)))

@task
def chuser(user):
    """
    Change a users password.
    """
    if not sudo("passwd %s" % (passwd)).failed:
        logme(green("Successfully changed password for user %s" % (user)))
    else:
        logme(red("Failed to change password for %s" % (user)))

@task
def chuser(userch):
    """
    Change a users password.
    """
    if not sudo("passwd %s" % (userch)).failed:
        logme(green("Successfully changed password for %s" % (userch)))
    else:
        logme(red("Failed to change %s password" % (userch)))

@task
def deluser(rmuser):
    """
    Delete a user from a host
    """
    if not sudo("userdel %s" % (rmuser)).failed:
	logme(green("Deleted user %s successfully" % (rmuser)))
    else:
        logme(red("Failed to delete user %s" % (rmuser)))

@task
def reboot():
    """
    Reboot a server
    """
    sudo("reboot")

@task
def rsync_dir(srcdir, user, host, remotedir):
    """
    rsync a directory to another
    """
    if not sudo("screen -S rsync -dm bash -c 'rsync -azP %s %s@%s:%s; exec $SHELL' " % (srcdir, user, host, remotedir)).failed:
        logme(green("rsync of %s to %s started" % (srcdir, host)))
    else:
        logme(red("Failed to start rsync in screen! Make sure screen is installed"))

@task
def chmod(perms, file):
    """
    Run chmod on file
    """
    if not sudo("chmod %d %s" % (perms, file)).failed:
        logme(green("chmod %d %s success" % (perms, file)))
    else:
        logme(red("chmod failed! Chmod manually"))

@task
def rchmod(perms, dir):
    """
    Run a recursive chmod on a directory
    """
    if not sudo("chmod -R %d %s" % (perms, dir)).failed:
        logme(green("chmod -R %d %s success" % (perms, dir)))
    else:
        logme(red("Chmod -R failed! Chmod manually"))

@task
def chown(user, file):
    """
    Chown a file
    """
    if not sudo("chown %s:%s %s" % (user, user, file)).failed:
        logme(green("chown of %s to %s success!" % (file, user)))
    else:
        logme(red("Chown failed! Chown manually"))

@task
def dmesg():
    """
    Get the last 25 entries from dmesg
    """
    sysdmesg = sudo("dmesg |tail -25")
    logme(green("dmesg returned: \n") + str(sysdmesg))

@task
def tailfile(file):
    """
    Tail -25 a file,such as a logfile. Use the /full/path/to.file
    """
    tailer = sudo("tail -25 %s" % (file))
    logme(green("Tail -25 returned:\n" + str(tailer)))

