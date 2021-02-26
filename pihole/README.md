# pihole-docker

pihole docker-compose.yml
    
# docker-compose.yml

git clone the source code and edit the docker-compose.yml:

    git clone https://gitlab.com/sparzz/pihole.git
    cd pihole
    nano docker-compose.yml
    docker-compose up -d

or

create the docker-compose.yml file yourself:

    mkdir /home/$USER/pihole-docker
    touch /home/$USER/pihole-docker/docker-compose.yml
  
edit the docker-compose.yml file:

    nano /home/$USER/pihole-docker/docker-compose.yml
    
copy these lines:

    services:
        container_name: pihole
        image: pihole/pihole:latest
        ports:
          - 53:53/tcp
          - 53:53/udp
          - 67:67/udp
          - 80:80/tcp
          - 443:443/tcp
        environment:
          TZ: <your_time_zone>
        volumes:
           - ./etc-pihole/:/etc/pihole/
           - ./etc-dnsmasq.d/:/etc/dnsmasq.d/
        dns:
          - 127.0.0.1
          - 1.1.1.1
        cap_add:
          - NET_ADMIN
        restart: unless-stopped

after run this command:

    docker-compose up -d

# change pihole default password

    docker exec -it pihole pihole -a -p
        
# acces the pihole web interface

in your browser enter:

    <ip_address_of_your_pihole_server>/admin
