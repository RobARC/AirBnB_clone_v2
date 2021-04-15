#!/usr/bin/python3
''' a Fabric script (based on the file 1-pack_web_static.py) that distributes
    an archive to your web servers, using the function do_deploy
'''


import os
from fabric.api import *


env.hosts = ['37.74.177.231, 54.157.63.160']


def do_deploy(archive_path):
    """ Deploys an archive to web servers """

    if not os.path.exists(archive_path):
        return False
    try:
        file_name = archive_path.split("/")[1]
        no_ext = file_name.split(".")[0]
        path = "/data/web_static/releases"
        with cd("/"):
            put(archive_path, 'tmp')
        run('mkdir -p {}{}'.format(path, no_ext))
        run('tar -xzf /tmp{} -C {}{}/.'.format(file_name, path, no_ext))
        run('rm /tmp/{}'.format(file_name))
        run('mv {0}{1}/'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except Exception:
        return False
