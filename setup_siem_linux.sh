#!/bin/bash

echo "🔧 Basic SIEM Setup Script (Linux VM)"
echo "Developed by Pavan Teja - GitHub: @Pavansoc"

# Update and install dependencies
echo "📦 Updating system and installing dependencies..."
sudo apt update && sudo apt upgrade -y
sudo apt install -y git python3 python3-pip docker.io docker-compose

# Enable Docker service
echo "🚀 Starting and enabling Docker..."
sudo systemctl start docker
sudo systemctl enable docker

# Optional: Allow Docker without sudo
echo "👤 Adding current user to Docker group..."
sudo usermod -aG docker $USER
newgrp docker

# Clone the repo
echo "📁 Cloning the SIEM project from GitHub..."
git clone https://github.com/Pavansoc/basic-siem.git
cd basic-siem || exit

# Build and run containers
echo "🐳 Building and running Docker containers..."
docker-compose up --build
