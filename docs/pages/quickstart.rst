bethpypot Quickstart
================
bethpypot is a simple TCP honeypot written in python
Installation
------------

    python -m pip install bethpypot

Running
-------

    python -m pip install bethpypot

Debian package
--------------

Download the package from github release, or
Build the Debian package with:

    dpkg-deb --build ./deb bethpypot-1.0.0.deb

Install the Debian package with:

    sudo apkg -i bethpypot-1.0.0.deb

Config defaults to '/etc/bethpypot.ini'.
Logs will be available in '/var/log/bethpypot.log'.

Source Code
-----------
https://github.com/beit-lachma/bethpypot

Documentation
-------------
https://bethpypot.rtfd.io