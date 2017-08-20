# Fabfile
A basic and very generic Fabric file. Mostly giving myself something to work off of for later.

## Available commands:

    aptinstall  Install a package with apt-get install
    aptremove   Remove a package using apt
    aptupdate   Run apt-update
    aptupgrade  Run apt-get upgrade. Be sure to run apt-get update with aptupdate first
    chmod       Run chmod on file
    chown       Chown a file
    chuser      Change a users password.
    deluser     Delete a user from a host
    dmesg       Get the last 25 entries from dmesg
    getfile     Download a file
    psaux       Runs ps aux|grep on provided input
    putfile     Upload a file from your local machine. putfile:localfile.tar.gz,/remote/dest
    rchmod      Run a recursive chmod on a directory
    reboot      Reboot a server
    restart     Restart a service
    rsync_dir   rsync a directory to another
    status      Check service status ouput
    tailfile    Tail -25 a file,such as a logfile. Use the /full/path/to.file
    targz       Creates a .tar.gz of a directory. Enter the full path.
    uptime      Get server uptime
    useradd     Add a user to a host.
    wget        wget from a url into /home
    ziparchive  Create a .zip archive of a directory. Enter the full 

# Example usage
## Example usage of utilizing command without options
```
fab -H my.server.com aptupdate
```
## Utilizing a function with passable options
```
fab -H my.server.com psaux:systemd
[my.server.com] ps aux returned:
root          1  0.3  0.0 191796  4512 ?        Ss   Jun20 316:32 /usr/lib/systemd/systemd --system --deserialize 21
```
# Other usage
For more on basic usage with Python Fabric,please visit the official documentation at http://www.fabfile.org/

