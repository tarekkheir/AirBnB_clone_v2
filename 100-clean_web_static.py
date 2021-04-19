#!/usr/bin/python3
""" Fabric script that deletes out-of-date
archives, using the function do_clean"""


import os
import glob
from fabric.api import *
env.hosts = ['35.243.232.238', '35.237.104.223']


def do_clean(number=0):
    """ delete files function"""
    if int(number) == 0 or int(number) == 1:
        number = 1
    else:
        number = int(number)

    local("ls -1tr versions | tail -n {} | xargs -d '\n' rm -Rf --"
          .format(number))
    local("ls -1tr  /data/web_static/releases | tail -n {}\
          | xargs -d '\n' rm -Rf --"
          .format(number))
