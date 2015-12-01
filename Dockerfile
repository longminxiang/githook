FROM index.alauda.cn/ericlung/python

COPY ./hook /home/hook

RUN (apt-get update &&\ 
apt-get --yes --force-yes install git &&\
pip install flask &&\
cd /etc/ssh &&\
cp ssh_config ssh_config_backup &&\
echo "    StrictHostKeyChecking no\n"\
>> ssh_config)

VOLUME ["/home/hook"]
VOLUME ["/home/git"]
EXPOSE 5000
CMD ["python", "/home/hook/githook.py"]