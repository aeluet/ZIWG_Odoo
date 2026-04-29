1. Ubuntu instantzia sortu AWS 20 GiB inguruko almazenamendua jarri
2. Sarrera erregelak gehitu
    Type: Custom TCP

    Port Range: 8069

    Source: 0.0.0.0/0

   eta
   
    Type: Custom TCP

    Port Range: 80 

    Source: 0.0.0.0/0
   
3. Klonatu errepositorioa AWS Instantzian
4. Instalatu Docker
````
  # Add Docker's official GPG key:
    sudo apt update
    sudo apt install ca-certificates curl
    sudo install -m 0755 -d /etc/apt/keyrings
    sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
    sudo chmod a+r /etc/apt/keyrings/docker.asc
    
    # Add the repository to Apt sources:
    sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
    Types: deb
    URIs: https://download.docker.com/linux/ubuntu
    Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
    Components: stable
    Architectures: $(dpkg --print-architecture)
    Signed-By: /etc/apt/keyrings/docker.asc
    EOF
    
    sudo apt update
    ````
    Azken bertsioa instalatu
    
    ````
    sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    ````
    
5. Docker kontenedoreak deskargatu
    
    ````
    sudo docker compose up
    ````
    
6. Docker kontenedoreak hasi
    
    ````
    sudo docker compose start
    ````
7. Odoo-ra sartu instantziaren IP Publikoa erabiliz, hasieratu Laravel aplikazioaren email eta pasahitz berdinak erabiliz, ikusi .env
8. Inzidentziak aktibatu aplikazio atalean.
