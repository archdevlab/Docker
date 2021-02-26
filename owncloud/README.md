# owncloud

owncloud docker build with mariadb for mysql server

# setup environment

mariadb:

    mkdir /home/$USER/mariadb \
    /home/$USER/mariadb/data

owncloud:

    mkdir /home/$USER/owncloud \
    /home/$USER/owncloud/apps \
    /home/$USER/owncloud/config \
    /home/$USER/owncloud/data

# create docker network

you will need to create a docker network so the mariadb docker and owncloud docker can communicate 

    docker network create <your_network_name>

# create mariadb docker

I recommend to put a data base user, data base name and a database password! It is optionnal but it's for security!

    docker create \
    --name=mariadb \
    --network=<your_network_name> \
    -e PUID=1000 \
    -e PGID=1000 \
    -e MYSQL_ROOT_PASSWORD=ROOT_ACCESS_PASSWORD \
    -e TZ=America/Toronto \
    -e MYSQL_DATABASE=USER_DB_NAME \
    -e MYSQL_USER=MYSQL_USER \
    -e MYSQL_PASSWORD=DATABASE_PASSWORD \
    -p 3306:3306 \
    -v /<path_to>/mariadb/data:/config \
    --restart unless-stopped \
    linuxserver/mariadb

# create owncloud docker

    docker create \
    --name=owncloud \
    --network=<your_network_name> \
    -p 8080:80 \
    -v /<path_to>/owncloud/apps:/var/www/html/apps \
    -v /<path_to>/owncloud/config:/var/www/html/config \
    -v /<path_to>/owncloud/data:/var/www/html/data \
    --link mariadb:mysql \
    --restart unless-stopped \
    owncloud:latest

# start mariadb and owncloud docker

    docker start mariadb owncloud
    
# acces owncloud web interface

in your browser enter:

    <ip_address_of_your_owncloud_server>:8080

# link mariadb data base with owncloud

![762B11F4-5BA3-4F7E-A9A0-BD0C165484DC](https://user-images.githubusercontent.com/68618182/88479950-d48af100-cf20-11ea-9c20-dd4e238e4301.png)

Database user: 

    <your_database_user>

Database password: 

    <your_database_password>

Database name: 

    <your_database_name>

localhost:

    <your_mariadb_server_address>:3306
