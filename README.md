# Fabfile
A basic and very generic Fabric file. Mostly giving myself something to work off of for later.

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

