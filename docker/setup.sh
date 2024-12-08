#!/bin/bash

set -e  # Exit on any error
set -o pipefail  # Ensure error catching in piped commands

# Log file for debugging purposes
LOG_FILE="/app/setup.log"
exec > >(tee -i "$LOG_FILE") 2>&1

echo "Script started at $(date)"

# Set up SSH keys
mkdir -p /app/key
cd /app/key

# Install gdown and download keys
pip install --quiet gdown
python -m gdown 1pHH5Rlpk-gKVzXo5hSYxomKzLI7P8e9g
mv 1 key
python -m gdown 1wgVWoi6KuPBS8x9yKyyqyNTsMNQkfaVk
mv 1.pub key.pub

# Set permissions for the private key
chmod 600 /app/key/key

# Start the SSH agent and add the private key
eval "$(ssh-agent -s)"
ssh-add /app/key/key

mkdir -p ~/.ssh
ssh-keyscan -t rsa,ecdsa github.com >> /app/.ssh/known_hosts
chmod 600 /app/.ssh/known_hosts


# Clone the repository if not already present
if [ ! -d "/app/study_center" ]; then
    echo "Cloning the repository..."
    git clone git@github.com:HoangHa2305/study_center.git /app/study_center
else
    echo "Repository already exists. Skipping clone."
fi

# Install Python dependencies
echo "Installing Python dependencies..."
cd /app/study_center/face_recognition
pip install -r requirements_server.txt --no-cache-dir

# End of script
echo "Setup completed successfully at $(date)"
