#!bin/sh

docker rm -f githook
docker run --name githook -p 12712:5000 -d -v ~/GIT/githook/hook:/home/hook -v ~/GIT/githook/demo:/home/git eric/githook