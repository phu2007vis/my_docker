#!/bin/bash

set -e  # Exit on any error
set -o pipefail  # Ensure error catching in piped commands

mkdir /app/key
cd /app/key

pip install gdown
python -m gdown 1pHH5Rlpk-gKVzXo5hSYxomKzLI7P8e9g
mv 1 key
python -m gdown 1wgVWoi6KuPBS8x9yKyyqyNTsMNQkfaVk
mv 1.pub key.pub
cd /app
eval "$(ssh-agent -s)"
chmod  700 /app/key/key
ssh-add /app/key/key 
cd /app
mkdir ~/.ssh
ssh-keyscan -t ecdsa github.com >> ~/.ssh/known_hosts
git clone git@github.com:HoangHa2305/study_center.git
cd /app/study_center/face_recognition
