#!/usr/bin/env bash
#Sets up a webserver
apt-get update -y
apt-get install nginx -y
mkdir -p /data/web_static/releases
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test
echo "Working!"> /data/web_static/releases/test/index.html
ln -snf /data/web_static/releases/test/ /data/web_static/current
chown ubuntu:ubuntu -R /data
ALS="\\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n"
sed -i '/^\sserver_name/ a'"$ALS"'' /etc/nginx/sites-enabled/default
nginx -s reload
exit 0
