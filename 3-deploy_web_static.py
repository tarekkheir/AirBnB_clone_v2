#!/usr/bin/python3
""" Fabric script that creates and distributes
an archive to your web servers, using the function deploy"""


from datetime import datetime
import os
from fabric.api import *
env.hosts = ['35.243.232.238', '35.237.104.223']


def do_pack():
    """ make a .tgz files pack"""
    local("mkdir -p versions")
    now = datetime.now()
    archive_path = "versions/web_static_{}.tgz".format(now.strftime("%Y%m%d%H%M%S"))

    if local("tar -czvf {} web_static".format(archive_path)).succeeded:
        return archive_path
    else:
        return None

def do_deploy(archive_path):
    """ do_deploy function"""
    if not os.path.isfile(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")
        name_split = archive_path.split('/')
        name_split = name_split[1].split('.')
        name_split = name_split[0]
        filename = archive_path.split('/')
        filename = filename[1]
        sudo("mkdir -p /data/web_static/releases/{}/".format(name_split))

        data = "/data/web_static/releases/"
        sudo("tar -zxvf /tmp/{} -C {}{}/".format(filename, data, name_split))
        sudo("rm -Rf /tmp/{}".format(filename))
        sudo("mv {}{}/web_static/* {}{}/"
             .format(data, name_split, data, name_split))
        sudo("rm -rf {}{}/web_static".format(data, name_split))
        sudo("rm -Rf /data/web_static/current")
        sudo("ln -s {}{} /data/web_static/current".format(data, name_split))
        return True
    except:
        return False

def deploy():
    """ deploy all function"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
