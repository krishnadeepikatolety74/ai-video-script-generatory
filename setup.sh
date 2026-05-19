#!/bin/bash

# Video Script Generator - Quick Setup Script
# Works on Linux and macOS

set -e

echo "🎬 Video Script Generator - Setup Script"
echo "=========================================="
echo ""

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed."
    echo "Please install Docker from https://www.docker.com"
    exit 1
fi

echo "✅ Docker found"

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed."
    echo "Please install Docker Compose from https://docs.docker.com/compose/install/"
    exit 1
fi

echo "✅ Docker Compose found"
echo ""

# Create directory if it doesn't exist
if [ ! -d "video-script-generator" ]; then
    mkdir video-script-generator
    echo "📁 Created directory: video-script-generator"
fi

cd video-script-generator

# Check if files exist
if [ ! -f "docker-compose.yml" ]; then
    echo "❌ docker-compose.yml not found in current directory"
    echo "Please ensure all required files are in the directory:"
    echo "  - app.py"
    echo "  - index.html"
    echo "  - docker-compose.yml"
    echo "  - Dockerfile"
    echo "  - requirements.txt"
    exit 1
fi

echo "✅ All required files found"
echo ""

# Start services
echo "🚀 Starting services..."
echo "This may take 3-5 minutes the first time (downloading models)"
echo ""

docker-compose up

echo ""
echo "✅ Setup complete!"
echo "📱 Access the app at:"
echo "   http://localhost:5000"
echo ""
echo "Press Ctrl+C to stop the services"
