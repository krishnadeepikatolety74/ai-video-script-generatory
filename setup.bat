@echo off
REM Video Script Generator - Quick Setup Script for Windows

echo 🎬 Video Script Generator - Setup Script for Windows
echo =====================================================
echo.

REM Check if Docker is installed
docker --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Docker is not installed or not in PATH.
    echo Please install Docker Desktop from https://www.docker.com
    pause
    exit /b 1
)

echo ✅ Docker found
echo.

REM Check if Docker Compose is installed
docker-compose --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Docker Compose is not installed.
    echo Please install Docker Desktop which includes Docker Compose.
    pause
    exit /b 1
)

echo ✅ Docker Compose found
echo.

REM Create directory if it doesn't exist
if not exist "video-script-generator" (
    mkdir video-script-generator
    echo 📁 Created directory: video-script-generator
)

cd /d video-script-generator

REM Check if required files exist
if not exist "docker-compose.yml" (
    echo ❌ docker-compose.yml not found in current directory
    echo Please ensure all required files are in the directory:
    echo   - app.py
    echo   - index.html
    echo   - docker-compose.yml
    echo   - Dockerfile
    echo   - requirements.txt
    pause
    exit /b 1
)

echo ✅ All required files found
echo.

REM Start services
echo 🚀 Starting services...
echo This may take 3-5 minutes the first time (downloading models)
echo.

docker-compose up

echo.
echo ✅ Setup complete!
echo 📱 Access the app at:
echo    http://localhost:5000
echo.
echo Press Ctrl+C to stop the services
pause
