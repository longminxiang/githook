from flask import Flask
import subprocess
import time
import os
import sys

app = Flask(__name__)

_GIT_DIR = "/home/git/"
_CONF_NAME = "conf"


def _conf_module(path):
    if not path in sys.path:
        sys.path.append(path)
    if not _CONF_NAME in sys.modules:
        return __import__(_CONF_NAME)
    else:
        eval('import ' + _CONF_NAME)
        return eval('reload(%s)' % _CONF_NAME)


@app.route('/')
def home():
    return "hello world!"


@app.route('/<pname>')
def githook(pname):
    ppath = _GIT_DIR + pname
    if not os.path.exists(ppath):
        return "no project path"
    gpath = ppath + "/" + pname
    if os.path.exists(gpath):
        subprocess.Popen(['git ' 'pull'], cwd=gpath, shell=True)
        time.sleep(.1)
    else:
        cpath = ppath + "/" + _CONF_NAME + ".py"
        if not os.path.exists(cpath):
            return "no config file"
        conf = _conf_module(ppath)
        subprocess.Popen("git clone %s" % conf.GIT_URL, cwd=ppath, shell=True)
        time.sleep(.1)
    return 'Thanks'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
