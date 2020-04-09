#!/usr/bin/python3
"""Fabricfile that moves web_static contents from AirBnB_v2 repo"""
from fabric.api import local, hide
from datetime import datetime


def do_pack():
    """Compresses folder in tgz format"""

    time = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    name = "web_static"
    loc = "versions"
    with hide('running'):
        local("mkdir -p versions", capture=False)
        local("echo \"Packing {} to {}/{}_{}.tgz\""
              .format(name, loc, name, time))
    result = local("tar -cvzf {}/{}_{}.tgz web_static"
                   .format(loc, name, time))
    if not result.failed:
        return "{}/{}_{}.tgz".format(loc, name, time)
    else:
        return None
