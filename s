Help on module fabric.api in fabric:

NNAAMMEE
    fabric.api - Non-init module for doing convenient * imports from.

FFIILLEE
    /home/riley/.local/lib/python2.7/site-packages/fabric/api.py

DDEESSCCRRIIPPTTIIOONN
    Necessary because if we did this in __init__, one would be unable to import
    anything else inside the package -- like, say, the version number used in
    setup.py -- without triggering loads of most of the code. Which doesn't work so
    well when you're using setup.py to install e.g. ssh!

DDAATTAA
    eennvv = {'disable_known_hosts': False, 'effective_roles'...': False, 'su...
    oouuttppuutt = {'status': True, 'stdout': True, 'warnings': Tru..., 'stderr'...

