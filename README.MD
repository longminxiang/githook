# Git Hook

git hook with docker

##Usage

###1.build Dockerfile
	
	docker build -t eric/githook .
	

###2.run
	
	docker rm -f githook
	docker run --name githook -p 12852:5000 -d -v ~/GIT:/home/git eric/githook
	
###3.setting

	cd ~/GIT
	make files like demo's
	
####3.1 config conf.py

	//your git ssh url
	GIT_URL = "git@git.coding.net:ericlung/EricSite.git"

	//rsa name if use ssh auth
	RSA_PATH = "id_rsa"

####3.2 id_rsa

	ssh-keygen -t rsa -C xx@xx.com

###4.add webhook to git project

	http://xxx.xx:12852/your_project_name
