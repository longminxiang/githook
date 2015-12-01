# -*- coding: utf-8 -*-
from flask import Flask
import subprocess
import os
import sys

app = Flask(__name__)

_GIT_DIR = "/home/git/"
_CONF_NAME = "conf"
_SSH_ROOT = "/root/.ssh"


def _import_conf_module(path):
    if not path in sys.path:
        sys.path.append(path)
    return __import__(_CONF_NAME)


@app.route('/')
def home():
    return "hello world!"


@app.route('/<pname>', methods=['GET', 'POST'])
def githook(pname):
    # 项目目录
    ppath = _GIT_DIR + pname
    if not os.path.exists(ppath):
        return "no project path"
    # 导入conf模块
    conf = _import_conf_module(ppath)
    # 设置ssh
    if conf.RSA_PATH:
        subprocess.call(["mkdir", _SSH_ROOT], cwd=ppath)
        subprocess.call(["cp", conf.RSA_PATH, _SSH_ROOT], cwd=ppath)
    # git目录
    gpath = ppath + "/" + pname
    if os.path.exists(gpath):
        # 如果存在项目，pull
        subprocess.call(["git", "pull"], cwd=gpath)
    else:
        # 不存在，clone
        subprocess.call(["git", "clone", conf.GIT_URL], cwd=ppath)
    return 'Thanks'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
