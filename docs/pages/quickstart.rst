pypot Quickstart
================
bethpypot is a simple TCP honeypot written in python
Installation
------------

    python -m pip install pypot

Running
-------

    python -m pip install pypot

Debian package
--------------

Download the package from github release, or
Build the Debian package with:

    dpkg-deb --build ./deb pypot-1.0.0.deb

Install the Debian package with:

    sudo apkg -i pypot-1.0.0.deb

Config defaults to '/etc/pypot.ini'.
Logs will be available in '/var/log/pypot.log'.

Source Code
-----------
https://github.com/beit-lachma/Pypot/tree/master

Documentation
-------------
https://pypot.rtfd.io
