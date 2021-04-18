#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo, using the function do_pack"""


from datetime import datetime
from fabric.api import local


def do_pack():
    """ make a .tgz files pack"""
    local("mkdir -p versions")
    now = datetime.now()
    archive_path = "versions/web_static_{}{}{}{}{}{}.tgz".format(now.year, now.month,
                                                        now.day, now.hour,
                                                        now.minute, now.second)

    if local("tar -czvf {} web_static"
             .format(archive_path)).succeeded:
        return archive_path
    else:
        return None
