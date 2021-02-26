# openvpn-as-docker

openvpn-as docker command

# command to build the docker images

## terminal command 

create openvpn dir:

    mkdir /home/$USER/openvpn

create the openvpn-as docker:

    docker create \
    --name=openvpn-as \
    --cap-add=NET_ADMIN \
    -e PUID=<your_uid> \
    -e PGID=<your_gid> \
    -e TZ=<your_time_zone> \
    -e INTERFACE=bridge \
    -p 943:943 \
    -p 9443:9443 \
    -p 1194:1194/udp \
    -v <path_to_where_you_want_to_store_data>:/config \
    --restart unless-stopped \
    linuxserver/openvpn-as

## docker-compose

git clone the source code, create directory to store openvpn data and edit the docker-compose.yml file:

    mkdir /home/$USER/openvpn
    git clone https://gitlab.com/sparzz/openvpn-as.git
    cd openvpn-as
    nano docker-compose.yml
    docker-compose up -d

or

create a docker-compose.yml file and a directory to store openvpn data:

    mkdir /home/$USER/openvpn-docker
    mkdir /home/$USER/openvpn
    touch /home/$USER/openvpn-docker/docker-compose.yml

edit the docker-compose.yml file:

    nano /home/$USER/openvpn-docker/docker-compose.yml
    
 copy these lines:

    services:
        image: linuxserver/openvpn-as
        container_name: openvpn-as
        cap_add:
          - NET_ADMIN
        environment:
          - PUID=<your_uid>
          - PGID=<your_gid>
          - TZ=<your_time_zone>
          - INTERFACE=bridge #optional
        volumes:
          - <path_to_where_you_want_to_store_data>:/config
        ports:
          - 943:943
          - 9443:9443
          - 1194:1194/udp
        restart: unless-stopped

after run this command:

    docker-compose up -d

# acces the openvpn-as web interface

in your browser enter:

    https://<ip_address_of_your_openvpn-as_server>:943/admin
