#!/usr/bin/python3
''' a Fabric script (based on the file 1-pack_web_static.py) that distributes
    an archive to your web servers, using the function do_deploy
'''


import os
from fabric.api import *


env.hosts = ['34.74.177.231', '54.157.63.160']


def do_pack():
    '''
        Creating an archive with the file in web_static folder
    '''
    now = datetime.now()
    filename = "versions/web_static_{}{}{}{}{}{}.tgz".format(now.year,
                                                             now.month,
                                                             now.day,
                                                             now.hour,
                                                             now.minute,
                                                             now.second)
    print("Packing web_static to versions/{}".format(filename))
    local("mkdir -p versions")
    result = local("tar -vczf {} web_static".format(filename))
    if result.succeeded:
        return (filename)
    else:
        return None


def do_deploy(archive_path):
    """ Deploys an archive to web servers """

    if not os.path.exists(archive_path):
        return False
    f_name = archive_path.split("/")[1]
    if not os.path.exists(archive_path):
        return False

    result = put(archive_path, "/tmp/")
    if result.failed:
        return False

    run("mkdir -p /data/web_static/releases/{}".format(f_name[:-4]))

    cmd = "tar -xzf /tmp/{} -C /data/web_static/releases/{}". \
          format(f_name, f_name[:-4])
    result = run(cmd)
    if result.failed:
        return False

    result = run("rm /tmp/{}".format(f_name))
    if result.failed:
        return False

    run("cp -rp /data/web_static/releases/{}/web_static/*\
        /data/web_static/releases/{}/".format(f_name[:-4], f_name[:-4]))

    run("rm -rf /data/web_static/releases/{}/web_static/".format(f_name[:-4]))
    result = run("rm /data/web_static/current")
    if result.failed:
        return False

    path = "/data/web_static/releases/{}".format(f_name[:-4])
    cmd = "ln -sf {} /data/web_static/current".format(path)
    result = run(cmd)
    if result.failed:
        return False
    return True
