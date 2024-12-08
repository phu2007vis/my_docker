

#!/bin/sh

# Set up directories
echo "Setting up directories..."
mkdir  ~/key
mkdir  ~/.ssh

# Navigate to the key directory
cd ~/key

# Install gdown and download keys
echo "Installing gdown and downloading keys..."
pip install --quiet gdown
python -m gdown 1pHH5Rlpk-gKVzXo5hSYxomKzLI7P8e9g
mv 1 key
python -m gdown 1wgVWoi6KuPBS8x9yKyyqyNTsMNQkfaVk
mv 1.pub key.pub

# Set up SSH
echo "Setting up SSH..."
cd /app
eval "$(ssh-agent -s)"
chmod 600 ~/key/key
ssh-add ~/key/key
mkdir /root/.ssh
ssh-keyscan -t ecdsa github.com >> /root/.ssh/known_hosts

# Clone the repository
echo "Cloning repository..."
if ! git clone git@github.com:HoangHa2305/study_center.git /app/study_center; then
  echo "Failed to clone repository. Please check your SSH key and permissions."
  exit 1
fi

# Install dependencies and run the application
cd /app/study_center/face_recognition
echo "Installing dependencies..."
pip install -r requirements_server.txt --no-cache-dir
