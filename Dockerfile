FROM longminxiang/centos7

MAINTAINER Eric Lung <longminxiang@163.com>

RUN (yum -y install MySQL-python git gcc libjpeg-turbo-devel libpng-devel &&\
yum clean all)

COPY ./GitHook/requirements.txt /home/GitHook/
COPY ./opt /opt

RUN (pip install -r /home/GitHook/requirements.txt)

RUN (sed -i '2 s/^/python \/opt\/conf.py\n/' /run.sh)

EXPOSE 8888