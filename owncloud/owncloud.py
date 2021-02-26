#!/usr/bin/python

import os
import time

root_password = str(input('enter your mariadb root password: ')).strip()

database_password = str(input('enter your mariadb database password: ')).strip()

database_user = str(input('enter your database user: ')).strip()

database_name = str(input('enter your database name: ')).strip()

network = str(input('enter your network name you would like to create: ')).strip()

tz = str(input('enter your time zone ex.: America/Toronto: ')).strip()

mariadb_container_name = str(input('enter the container name you wish to have for mariadb: ')).strip()

owncloud_container_name = str(input('enter the container name you wish to have for owncloud: ')).strip()

mariadb_dir = str(input('enter your working dir for mariadb docker ex.: /home/$USER/mariadb: ')).strip()

owncloud_dir = str(input('enter your working dir for owncloud docker ex.: /home/$USER/owncloud: ')).strip()

puid = str(input('enter your PUID: ')).strip()

guid = str(input('enter your GUID: ')).strip()

time.sleep(2)

print('your mariadb root password is: ' + root_password + \
'\nyour mariadb database password is: ' + database_password + \
'\nyour database user is : ' + database_user + \
'\nyour your database name is: ' + database_name + \
'\nyour network name is: ' + network + \
'\nyour time zone is: ' + tz + \
'\nyour mariadb container name is: ' + mariadb_container_name + \
'\nyour owncloud container name is: ' + owncloud_container_name + \
'\nyour mariadb working dir is: ' + mariadb_dir + \
'\nyour owncloud working dir is: ' + owncloud_dir + \
'\nyour PUID is: ' + puid + \
'\nyour GUID is: ' + guid)

time.sleep(5)

print('create mariadb and owncloud working dir')

os.system('mkdir -p -v ' + mariadb_dir)
os.system('mkdir -p -v ' + mariadb_dir + '/data')
os.system('mkdir -p -v ' + owncloud_dir)
os.system('mkdir -p -v ' + owncloud_dir + '/apps')
os.system('mkdir -p -v ' + owncloud_dir + '/config')
os.system('mkdir -p -v ' + owncloud_dir + '/data')

time.sleep(2)

print('create docker network')

time.sleep(2)

os.system('docker network create ' + network)

time.sleep(2)

print('create mariadb docker')

time.sleep(2)

os.system('docker create \
--name=' + mariadb_container_name + ' \
--network=' + network + ' \
-e PUID=' + puid + ' \
-e PGID=' + guid + ' \
-e MYSQL_ROOT_PASSWORD='+ root_password + ' \
-e TZ=' + tz + ' \
-e MYSQL_DATABASE='+ database_name + ' \
-e MYSQL_USER='+ database_user + ' \
-e MYSQL_PASSWORD='+ database_password + ' \
-p 3306:3306 \
-v ' + mariadb_dir + '/data:/config \
--restart unless-stopped \
linuxserver/mariadb')

time.sleep(2)

print('create owncloud docker')

time.sleep(2)

os.system('docker create \
--name=' + owncloud_container_name + ' \
--network=' + network + ' \
-p 8080:80 \
-v ' + owncloud_dir + '/apps:/var/www/html/apps \
-v ' + owncloud_dir + '/config:/var/www/html/config \
-v ' + owncloud_dir + '/data:/var/www/html/data \
--link ' + mariadb_container_name + ':mysql \
--restart unless-stopped \
owncloud:latest')

time.sleep(2)

print('start mariadb docker')

time.sleep(2)

os.system('docker start ' + mariadb_container_name)

time.sleep(2)

print('start owncloud docker')

time.sleep(2)

os.system('docker start ' + owncloud_container_name)
