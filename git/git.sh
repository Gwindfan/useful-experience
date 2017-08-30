#!/usr/bin/env bash

# git pull 与 git fetch 的区别
git pull
git fetch
git checkout -f xxx.py

git clone xxx.git

git add .

git commit -m 'message'

git push -u  origin master

git rm xxx.py

git branch feature-xxx-bruce

git checkout feature-xxx-bruce

git merge master