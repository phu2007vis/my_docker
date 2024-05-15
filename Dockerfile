# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./main /app/main
COPY requirements.txt requirements.txt

# Install wget
RUN apt-get update && apt-get install -y wget

# Download the required file using wget
RUN wget -O /app/main/vgg_transformer.pth https://vocr.vn/data/vietocr/config/vgg_transformer.yml

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade vietocr

# Change working directory to /app/main
WORKDIR /app/main
