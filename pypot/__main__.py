"""
Pypot.

Simple Honeypot logger

Usage:
  pypot <config_filepath>

Options:
  <config_filepath>    Path to config options .ini file
  -h --help            Show this screen.
"""
import configparser
import sys
from pypot import HoneyPot
import configparser
import sys
from pypot import HoneyPot


if len(sys.argv) < 2 or sys.argv[0] in ['-h', '--help']:
    print(__doc__)
    sys.exit(1)


config_filepath = 'pypot.ini'
config = configparser.ConfigParser()
config.read(config_filepath)

ports = config.get('default', 'ports', raw=True, fallback="3331,3332,3333,3334,3335,5552")
host = config.get('default', 'host', raw=True, fallback="0.0.0.0")
log_filepath = config.get('default', 'logfile', raw=True, fallback="/home/kali/Pycharm/Pypot/pypot/pypot.log")


ports_list = []
try:
    ports_list = ports.split(',')
except Exception as e:
    print('[-] Error parsing ports: %s.\nExiting.', ports)
    sys.exit(1)

honeypot = HoneyPot(host, ports_list, log_filepath)
honeypot.run()
