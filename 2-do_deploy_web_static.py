#!/usr/bin/python3
""" Fabric script that distributes an archive
to your web servers, using the function do_deploy"""


import os
from fabric.api import *
env.hosts = ['35.243.232.238', '35.237.104.223']


def do_deploy(archive_path):
    """ do_deploy function"""
    if not os.path.isfile(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")
        sudo("mkdir -p /data/web_static/releases/")
        name_split = archive_path.split('/')
        name_split = name_split[1].split('.')
        name_split = name_split[0]
        filename = archive_path.split('/')
        filename = filename[1]

        data = "/data/web_static/releases/"
        sudo("tar -zxvf /tmp/{} -C {}{}".format(filename, data, name_split))
        sudo("rm -Rf /tmp/{}".format(filename))
        sudo("mv {}{}/web_static/* {}releases/{}".format(data, name_split, data, name_split))
        sudo("rm -rf {}{}/web_static".format(data, name_split))
        sudo("rm -Rf /data/web_static/current")
        sudo("ln -s {}{} /data/web_static/current".format(data, name_split))
        return True
    except:
        return False
