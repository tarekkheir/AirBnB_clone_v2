#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo, using the function do_pack"""


from datetime import datetime
from fabric.api import local


def do_pack():
    """ make a .tgz files pack"""
    local("mkdir -p versions")
    now = datetime.now()
    archive_path = "web_static_{}.tgz".format(now.strftime("%Y%m%d%H%M%S"))

    if local("tar -czvf versions/{} web_static"
             .format(archive_path)).succeeded:
        return archive_path
    else:
        return None
