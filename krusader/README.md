# krusader-docker

docker compose file for krusader from djaydev/krusader and binhex/arch-krusader

# create a docker image with docker compose file

## binhex/arch-krusader

git clone the source code and edit the docker-compose.yml file:

    https://gitlab.com/sparzz/krusader.git
    cd krusader
    cd binhex-arch-krusader
    nano docker-compose.yml
    docker-compose up -d

or 

create a krusader-docker dir and create a docker-compose.yml file:

    mkdir /home/$USER/krusader
    touch /home/$USER/krusader/docker-compose.yml
    
edit the docker-compose.yml file:

    nano /home/$USER/krusader/docker-compose.yml
    
copy these lines:

    services:
        container_name: krusader
        image: binhex/arch-krusader
        restart: unless-stopped
        privileged: true
        ports:
          - 5800:5800
          - 6080:6080
        environment:
          - PUID=<your_UID>
          - PGID=<your_GID>
          - TZ=<your_time_zone>
          - TEMP_FOLDER=<path_to_store_krusader_temp_files>
          - WEBPAGE_TITLE=<name shown in browser tab>
          - VNC_PASSWORD=<password for web ui>
        volumes:
          - <path_to_store_config_files>:/config
          - <path_to_your_root_dir>:/<wanted_dir>
          - <path_to_your_home_dir>:/<wanted_dir>
          - /etc/localtime:/etc/localtime:ro
          # optionnal this is to mount a disk or a share
          # you can add multiple share or disk
          - <path_to_your_share_or_mounted_disk>:/<wanted_dir>

after run this command :

    docker-compose up -d

## djaydev/krusader

git clone the source code and edit the docker-compose.yml file:

    https://gitlab.com/sparzz/krusader.git
    cd krusader
    cd djaydev-krusader
    nano docker-compose.yml
    docker-compose up -d

or

create a krusader-docker dir and create a docker-compose.yml file:

    mkdir /home/$USER/krusader
    touch /home/$USER/krusader/docker-compose.yml
    
edit the docker-compose.yml file:

    nano /home/$USER/krusader/docker-compose.yml
    
copy these lines:

    services:
        container_name: krusader
        image: djaydev/krusader
        restart: unless-stopped
        privileged: true
        ports:
          - 5800:5800
          - 5900:5900
        environment:
          - PUID=<your_UID>
          - PGID=<your_GID>
          - TZ=<your_time_zone>
          - TEMP_FOLDER=<path_to_store_krusader_temp_files>
        volumes:
          - <path_to_store_config_files>:/config:rw
          - <path_to_your_root_dir>:/<wanted_dir>:rw
          - <path_to_your_home_dir>:/<wanted_dir>:rw
          - /etc/localtime:/etc/localtime:ro
          # optionnal this is to mount a disk or a share
          # you can add multiple share or disk
          - <path_to_your_share_or_mounted_disk>:/<wanted_dir>:rw

after run this command :

    docker-compose up -d

# acces krusader web interface

in your browser enter:

    <ip_address_of_your_krusader_server>:5800

