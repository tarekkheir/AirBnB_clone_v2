#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
sudo apt-get update
sudo apt-get install -y nginx

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

sudo touch /data/web_static/releases/test/index.html
sudo chmod 666 /data/web_static/releases/test/index.html

echo "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" >> /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/listen 80 default_server;/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-available/default
sudo service nginx restart
