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
# Silence the default fabric output
env.warn_only = True
env.output_prefix = False

if sys.argv[1] == '--show=everything':
    print(red("Running in verbose mode..."))
else:
    state.output.running = True
    state.output.output = False
    state.output.warnings = False

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
        logme(green("restart %s successful" % (svc)))
    else:
        logme(red("Failed to restart %s" % svc))

@task
def status(svc):
    """
    Check service status ouput
    """
    stat = sudo("service %s status" % (svc))
    logme(green("service %s status returned:\n" % svc)  + str(stat))

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
    state.output.output = True
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
    state.output.output = True
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
    state.output.output = True
    if not sudo("adduser %s" % (newuser)).failed:
        logme(green("Add user %s success!" % (newuser)))
    else:
        logme(red("Failed to adduser %s" % (newuser)))

@task
def chuser(user):
    """
    Change a users password.
    """
    state.output.output = True
    if not sudo("passwd %s" % (passwd)).failed:
        logme(green("Successfully changed password for user %s" % (user)))
    else:
        logme(red("Failed to change password for %s" % (user)))

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
    state.output.output = True
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

@task
def ziparchive(src):
    """
    Create a .zip archive of a directory. Enter the full path
    """
    zipper = sudo("zip -r %s.zip %s" % (src, src))
    logme(green("zip -r returned:\n") + str(zipper))

@task
def wget(url):
    """
    wget from a url into /home
    """
    state.output.output = True
    if not sudo("cd /home && wget %s" % (url)).failed:
        logme(green("wget complete"))
    else:
        logme(red("wget failed!"))

@task
def putfile(src, dest):
    """
    Upload a file from your local machine. putfile:localfile.tar.gz,/remote/dest
    """
    state.output.output = True
    put(local_path=src, remote_path=dest)

@task
def getfile(src):
    """
    Download a file
    """
    state.output.output = True
    get(remote_path=src, local_path="~/", use_sudo=True)

@task
def shutdown():
    """
    Sends a shutdown command
    """
    sudo("shutdown -P now")

@task
def zpr():
    """
    Runs puppet agent -t
    """
    state.output.output = True
    sudo("puppet agent -t")

@task
def zpe():
    """
    Enables puppet on remote host
    """
    sudo("puppet agent --enable")

@task
def zpd():
    """
    Disable puppet
    """
    reason = 'reasons'
    sudo("puppet agent --disable %s" % reason)
