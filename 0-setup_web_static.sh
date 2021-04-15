#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
sudo apt-get update && apt-get upgrade
sudo apt-get intall -y nginx
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

sudo touch /data/web_static/releases/test/index.html
sudo chmod 666 /data/web_static/releases/test/index.html

content = "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

echo $content >> /data/web_static/releases/test/index.html

ln -s /data/web_static/current /data/web_static/releases/test/
sudo chown -R ubuntu:ubuntu /data/
sed -i 's/ location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-available/default
sudo service nginx restart
