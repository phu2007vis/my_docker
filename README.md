# Install docker
1. Add Docker's official GPG key:
```bash
sudo apt-get update -y
sudo apt-get install ca-certificates curl -y
sudo install -m 0755 -d /etc/apt/keyrings 
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc 
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

2. Add the repository to Apt sources:
```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update -y
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y
```
# Pull dockerimage and run docker image
# Notice assert your ec2 is t3.small and 15gb  disk at least 
```bash
sudo docker pull phuoc20207/cloud_basic
cd /home/ubuntu
git clone https://github.com/phu2007vis/my_docker.git
cd my_docker
export endpoint=$(curl http://checkip.amazonaws.com)
sed -i "s|endpoint|$endpoint|g" docker-compose.yaml
sudo docker compose up -d
```

# All bin bash (paste to user data when lauching intances)
# Choose the ubuntu vm ( very important because of type of command line it just work in linux ubuntu) 
### Because the model deeplearning is heavy so it will take about 5 minutes to boot the web site and pull the image

```bash
#!/bin/bash
sudo apt-get update -y
sudo apt-get install ca-certificates curl -y
sudo install -m 0755 -d /etc/apt/keyrings 
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc 
sudo chmod a+r /etc/apt/keyrings/docker.asc
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update -y
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y
sudo docker pull phuoc20207/cloud_basic
cd /home/ubuntu
git clone https://github.com/phu2007vis/my_docker.git
cd my_docker
export endpoint=$(curl http://checkip.amazonaws.com)
sed -i "s|endpoint|$endpoint|g" docker-compose.yaml
sudo docker compose up -d
```
# How to test app ( notice http not htttps)
#### If you cannot connect to website connect to ec2 and go to /var/log/cloud_log_init.log to check the error
Connect to 
http://public_ip:3000

# App from 21013187@st.phenikaa-uni.edu.vn Nguyen Xuan Phuoc
