#!/usr/bin/python3
"""Fabricfile that distributes web_static contents from AirBnB_v2 folder"""
from fabric.api import local, hide, put, run, env, sudo, settings
from datetime import datetime
env.hosts = ['35.231.116.248', '54.83.93.155']


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


def do_deploy(archive_path):
    """Sends archive_path to web server"""

    try:
        f = open(archive_path)
        f.close()
    except:
        return False
    root = "/data/web_static"
    arc_lst = archive_path.split("/")
    res_f = list()
    result = put("{}".format(archive_path), "/tmp")
    res_f.append(result.succeeded)
    run("mkdir -p {}/releases/{}".format(root, arc_lst[1].split(".")[0]))
    result = run("tar -xzf /tmp/{} -C {}/releases/{} --strip=1"
                 .format(arc_lst[1], root, arc_lst[1].split(".")[0]))
    res_f.append(result.succeeded)
    result = run("rm -f {}/current /tmp/{}".format(root, arc_lst[1]))
    res_f.append(result.succeeded)
    result = run("ln -snf {}/releases/{} {}/current"
                 .format(root, arc_lst[1].split(".")[0], root))
    res_f.append(result.succeeded)
    result = sudo("nginx -s reload")
    res_f.append(result.succeeded)
    if False not in res_f:
        return True
    else:
        return False


def deploy():
    """creates and distributes a version of web_static"""

    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
