# -*- coding: utf-8 -*-
import os

APP_NAME = 'GitHook'

APP_ROOT = '/home/'

UWSGI_DIR = '/var/uwsgi/'

UWSGI_CONF_PATH = UWSGI_DIR + 'uwsgi.ini'


class DjangoApp(object):

    def __init__(self):
        super(DjangoApp, self).__init__()
        self.app_name = APP_NAME
        self.app_dir = APP_ROOT + self.app_name + "/"

    # 创建uwsgi配置
    def create_uwsgi_config(self):
        if not os.path.exists(UWSGI_DIR):
            os.system("mkdir %s" % UWSGI_DIR)
        if os.path.exists(UWSGI_CONF_PATH):
            os.system("rm %s" % UWSGI_CONF_PATH)
        f = open(UWSGI_CONF_PATH, 'w')
        nstr = "[uwsgi]\n \
                http = :8888\n \
                chdir = %s\n \
                wsgi-file = %s/wsgi.py\n \
                processes = 2\n \
                threads = 1\n" % (self.app_dir, self.app_name)
        f.write(nstr)
        f.close()

    def start(self):
        os.system("echo yes | python %smanage.py collectstatic" % self.app_dir)
        self.create_uwsgi_config()
        os.system("echo \"run uwsgi\"")
        os.system("uwsgi -d %suwsgi.log %s" % (UWSGI_DIR, UWSGI_CONF_PATH))

if __name__ == "__main__":
    if os.environ["DJANGO_RELEASE"] == '1':
        os.system("echo \"run in release mode\"")
        app = DjangoApp()
        app.start()
    else:
        os.system("echo \"run in debug mode\"")
