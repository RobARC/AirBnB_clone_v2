#!/usr/bin/python3
"""  a Fabric script that generates a .tgz archive from the contents of the
     web_static folder of your AirBnB Clone repo, using the function do_pack.
"""

from datetime import datetime
from fabric.api import *


def do_pack():
    """ compress the content web_static folder in a .tgz file """

    now = datetime.now()
    filename = 'versions/web_static_{}{}{}{}{}{}.tgz'.format(now.year,
                                                            now.month,
                                                            now.day,
                                                            now.hour,
                                                            now.minute,
                                                            now.second)
    print("Packing web_static to {}".format(filename))
    local("mkdir -p versions")
    result = local("tar -cvzf {} web_static".format(filename))
    if result.succeeded:
        return (filename)
    else:
        return (None)