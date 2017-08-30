#!/usr/bin/env bash
# 远程拷贝指定目录所有文件，除隐藏文件外至目标机
test6=172.16.217.58
scp -r $(ls -AF |grep '^[^\.]') admin@${test6}:/tmp

# 清理宿主机上所有状态为 Exit 的容器
docker rm -f $(d ps -a | grep Exit | awk '{print $1}')

# 查询并列出 /home/admin/app/test6 下所有大小大于 2M，30天前修改的文件，（并删除）

# 查看主机IPV4端口8080占用情况
netstat -tulpn | grep 8080

# 产看 java 进程 PID
ps -ef | grep java

# 指定 DNS 解析域名
host passport.qxwz-test.com 47.94.112.123

# 查询主机内存使用情况
free -h
free -m

# 释放主机内存
if [[ $free -le 1000  ]]; then
    sync && echo 1 > /proc/sys/vm/drop_caches
    sync && echo 2 > /proc/sys/vm/drop_caches
    sync && echo 3 > /proc/sys/vm/drop_caches
    echo "OK" >> /var/log/mem.log
else
    echo "Not required" >> /var/log/mem.log
fi

# 查询主机磁盘使用情况
df -h

# 查询当前目录所占磁盘的大小
du -sh

# 创建软链接
ln -s /mnt/acs_mnt/nas/nasdata /home/admin/app

# vi
# 退出 wq!
# 全局替换 :1,$s/source/target/g
# 查询配置文件非注释行且非空行 /^[^#|\s+]
# 插入／删除行／复制／剪切／黏贴／跳转到第一行／跳转到最后一行／跳转到指定行／搜索字符

# 网络
service network restart | status | stop | start
# dns 配置
cat /etc/resolv.conf

# 当前目录按照修改时间倒序罗列文件
ll -t

# 查询 CentOS 发行版本／内核
cat /etc/*release
uname -a

# cron tab
cat /etc/crontab


# sed
# awk
# find
# 正则
.+
*
?
\d
\s+
\w
\W
\n
\r
[a-z|A-Z]
^[^#]
^[^$]

# docker
docker pull image-name
docker ps -a | grep container-name
docker rm -f container-name
docker images [image-name]
docker rmi -f image-name
docker run
docker start | stop | restart
docker -t build image-name .
docker exec -ti container-name /bin/bash
docker-compose up -d

# 本地镜像推送远程镜像仓库
sudo docker login --username=g-sd@wzgroup registry.cn-beijing.aliyuncs.com
sudo docker tag [ImageId] registry.cn-beijing.aliyuncs.com/wz-web/backend-service:[镜像版本号]
sudo docker push registry.cn-beijing.aliyuncs.com/wz-web/backend-service:[镜像版本号]

# 导出，导入镜像
docker save sd-nginx > /tmp/sd-nginx.tar
docker load < /tmp/sd-nginx.tar


