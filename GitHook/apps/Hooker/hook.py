# -*- coding: utf-8 -*-
import os


def add_rsa_key(git_host, rsa_key):
    """
    添加ssh rsa key

    :param git_host string  git项目host
    :param rsa_key  string  rsa private key
    """
    _rsa_path = "/root/.ssh/id_rsa"
    _rsa_conf_path = "/root/.ssh/config"

    if os.path.exists(_rsa_path):
        os.system("rm %s" % _rsa_path)
    if os.path.exists(_rsa_conf_path):
        os.system("rm %s" % _rsa_conf_path)
    os.system("echo -e \"%s\" >> %s" % (rsa_key, _rsa_path))
    os.system("chmod 0600 %s" % _rsa_path)
    os.system("echo -e \"Host %s\n\tStrictHostKeyChecking no\n\" >> %s" % (git_host, _rsa_conf_path))


def git_clone_or_pull(path, name, url):
    """
    clone or pull
    如果已有项目，pull

    :param path string  项目路径
    :param name string  项目名称
    :param url  string  项目URL
    """
    if not os.path.exists(path):
        os.system("mkdir " + path)
    pro_dir = os.path.join(path, name)
    if os.path.exists(pro_dir):
        os.system("cd %s && git pull" % pro_dir)
    else:
        os.system("cd %s && git clone %s" % (path, url))
