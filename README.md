# Welcome to my project of cloud fondation course 
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
# Pull dockerimage and host website
1. Pull docker image from my dockerhub ( you can get more information in this https://hub.docker.com/r/phuoc20207/cloud_basic)
```bash
sudo docker pull phuoc20207/cloud_basic
```
2. Clone my code
```bash
cd /home/ubuntu
git clone https://github.com/phu2007vis/my_docker.git
cd my_docker
```
3. Set up enviroment variable
```bash
export endpoint=$(curl http://checkip.amazonaws.com)
sed -i "s|endpoint|$endpoint|g" docker-compose.yaml
```
4. Run docker image
```bash
sudo docker compose up -d
```
# Notice (very important wanning)
1. Assert your ec2 is t3.small and 15gb  disk at least
2. Choose the ubuntu vm ( very important because of type of command line it just work in linux ubuntu)
3. Add inbound rule : custom tcp 3000 anywherer ( container in ec2 expose a port 3000 and route to port 80 to application inside the container)
4. Assert your subnet of ec2 is public otherwise you can't connect to ec2
5. Because the model deeplearning is heavy so it will take about 5 minutes to boot the web site and pull the image

# All bin bash (paste to user data when lauching intances)

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

# Any question please contact via  this  email
## 21013187@st.*-uni.edu.vn 
## Nguyen Xuan Phuoc
