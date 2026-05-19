# 🎬 Video Script Generator - Free AI Edition

A lightweight, fast video promotional script generator powered by **Ollama** (100% free, no API costs). Generate engaging hooks, scripts, scene suggestions, and call-to-actions in seconds.

## Features

✅ **Free & Open Source** - No paid API requirements  
✅ **Fast Generation** - 30-60 seconds per complete script  
✅ **Local Processing** - Runs entirely on your machine  
✅ **Multiple Components** - Hook + Script + Scenes + CTA  
✅ **Lightweight UI** - Minimal CSS, fast loading  
✅ **Flexible Output** - Copy & customize generated content  

## Prerequisites

You need one of the following:

### Option 1: Docker (Easiest - Recommended)
- Docker Desktop installed
- 10GB free disk space (for Ollama model)
- 4GB+ RAM

### Option 2: Manual Setup
- Python 3.8+
- Ollama installed locally
- 10GB free disk space (for model)

---

## Quick Start (Docker - 3 Steps)

### Step 1: Install Docker
Download from https://www.docker.com/products/docker-desktop

### Step 2: Clone/Setup Project
```bash
# Create project directory
mkdir video-script-generator
cd video-script-generator

# Copy all provided files into this directory:
# - app.py
# - index.html
# - requirements.txt
# - docker-compose.yml
# - Dockerfile
```

### Step 3: Start Everything
```bash
docker-compose up
```

Wait for Ollama to download the model (this takes 3-5 minutes the first time).

**Access the app at:** http://localhost:3000 or http://localhost:5000

---

## Manual Setup (Without Docker)

### Step 1: Install Ollama
Download from https://ollama.ai

```bash
# After installation, start Ollama service
ollama serve
```

### Step 2: Download a Model
In a new terminal:
```bash
# Download Mistral (fastest, 4GB)
ollama pull mistral

# OR download Llama2 (better quality, 4GB)
ollama pull llama2

# OR download Neural Chat (balanced, 4GB)
ollama pull neural-chat
```

### Step 3: Install Python Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run Flask Server
```bash
python app.py
```

Server runs on: http://localhost:5000

### Step 5: Open Frontend
Open `index.html` in your browser (or use a local server):
```bash
# Simple Python server
python -m http.server 8000
# Then visit http://localhost:8000
```

---

## How to Use

### 1. Fill Product Details
- **Product Name**: e.g., "SmartWater Bottle"
- **Product Description**: Features, benefits, unique selling points
- **Target Audience**: Who are you selling to?
- **Campaign Goal**: What do you want to achieve?

### 2. Choose Duration
- 15 seconds (for ads)
- 30 seconds (standard)
- 60 seconds (long-form)

### 3. Generate Content
- **Generate All**: Get hook + script + scenes + CTA (recommended)
- **Individual Buttons**: Generate specific components

### 4. Use Results
- Copy any section to clipboard
- Edit as needed
- Use for video production, social media, ads

---

## API Endpoints

The Flask backend provides REST endpoints:

### Generate Hook
```bash
POST /api/generate-hook
{
  "productName": "SmartWater",
  "productDescription": "AI-powered water bottle that tracks hydration",
  "targetAudience": "Fitness enthusiasts"
}
```

### Generate Script
```bash
POST /api/generate-script
{
  "productName": "SmartWater",
  "productDescription": "AI-powered water bottle that tracks hydration",
  "targetAudience": "Fitness enthusiasts",
  "campaignGoal": "Drive sales",
  "duration": 30
}
```

### Generate Scenes
```bash
POST /api/generate-scenes
{
  "productName": "SmartWater",
  "productDescription": "AI-powered water bottle that tracks hydration",
  "campaignGoal": "Drive sales"
}
```

### Generate CTA
```bash
POST /api/generate-cta
{
  "productName": "SmartWater",
  "campaignGoal": "Drive sales",
  "targetAudience": "Fitness enthusiasts"
}
```

### Generate All Components
```bash
POST /api/generate-all
{
  "productName": "SmartWater",
  "productDescription": "AI-powered water bottle that tracks hydration",
  "targetAudience": "Fitness enthusiasts",
  "campaignGoal": "Drive sales",
  "duration": 30
}
```

---

## Model Selection

Choose the best model for your needs:

| Model | Speed | Quality | Size | RAM Required |
|-------|-------|---------|------|--------------|
| **Mistral** (default) | ⚡⚡⚡ Fast | ⭐⭐⭐ Good | 4GB | 4GB+ |
| **Llama2** | ⚡⚡ Medium | ⭐⭐⭐⭐ Excellent | 4GB | 6GB+ |
| **Neural-Chat** | ⚡⚡ Medium | ⭐⭐⭐⭐ Excellent | 4GB | 6GB+ |
| **OpenHermes** | ⚡ Slower | ⭐⭐⭐⭐⭐ Best | 7GB | 8GB+ |

### Change Model
Edit `docker-compose.yml` or set environment variable:
```bash
# For docker-compose
MODEL_NAME=llama2

# For manual setup
export MODEL_NAME=llama2
python app.py
```

---

## Troubleshooting

### "Connection refused" on localhost:5000
- Check if Flask is running: `python app.py`
- Check if Ollama is running
- Verify ports: `http://localhost:5000` for API, `http://localhost:11434` for Ollama

### "Ollama disconnected" message
- Start Ollama: `ollama serve`
- Download a model: `ollama pull mistral`
- Restart Flask: `python app.py`

### Slow generation (>2 minutes)
- Your system might be low on RAM
- Close other applications
- Try a faster model: `ollama pull mistral`
- Check: `docker stats` (for Docker) to see resource usage

### Model not downloading
- Check internet connection
- Ensure sufficient disk space (10GB+ free)
- Try: `ollama pull mistral` directly
- Check logs: `ollama logs` or Docker logs

### Port already in use
- Change port in `app.py`: `app.run(port=5001)`
- Or kill the process: `lsof -i :5000` then `kill -9 <PID>`

---

## Performance Tips

1. **First Generation is Slow** - Model loads into memory, future calls are faster
2. **Use Mistral Model** - Best balance of speed and quality
3. **Increase RAM** - 8GB+ recommended for faster generation
4. **Use Docker** - More efficient than manual setup
5. **Close Background Apps** - Free up system resources

---

## Customization

### Modify Prompts
Edit the prompt templates in `app.py`:
- `generate_hook()` - Line ~30
- `generate_script()` - Line ~40
- `generate_scenes()` - Line ~60
- `generate_cta()` - Line ~80

### Change UI
Edit `index.html` style section to customize colors, fonts, layout

### Add More Endpoints
Add new routes in `app.py` following the same pattern

---

## File Structure

```
video-script-generator/
├── app.py                 # Flask backend
├── index.html             # Web frontend
├── requirements.txt       # Python dependencies
├── docker-compose.yml     # Docker orchestration
├── Dockerfile             # Container config
└── README.md              # This file
```

---

## Example Workflow

1. **Start the app**
   ```bash
   docker-compose up
   ```

2. **Open browser**
   - http://localhost:5000

3. **Fill in details**
   - Product: "Eco Water Bottle"
   - Description: "Sustainable, reusable water bottle made from 100% recycled plastic"
   - Audience: "Environmentally conscious millennials"
   - Goal: "Drive sales"

4. **Click "Generate All"**
   - Wait 30-60 seconds

5. **Get results**
   - Hook: "Every sip saves the planet — introducing the bottle that cares as much as you do"
   - Script: 30-second promotional script
   - Scenes: 3 visual recommendations
   - CTA: "Shop now at EcoBottles.com — make every drop count"

6. **Copy and use**
   - Paste into your video editor
   - Modify as needed
   - Create your video

---

## System Requirements

### Minimum
- CPU: Quad-core
- RAM: 4GB
- Storage: 15GB free
- OS: Windows 10+, macOS 10.14+, Linux

### Recommended
- CPU: 6+ cores
- RAM: 8GB+
- Storage: 20GB free
- GPU: Optional (NVIDIA makes generation faster)

---

## Environment Variables

Set these to customize behavior:

```bash
# Ollama connection
OLLAMA_HOST=http://localhost:11434

# Model to use
MODEL_NAME=mistral

# Flask environment
FLASK_ENV=development

# API timeout (seconds)
TIMEOUT=120
```

---

## Docker Compose Troubleshooting

### See real-time logs
```bash
docker-compose logs -f
```

### Stop everything
```bash
docker-compose down
```

### Remove everything (including model)
```bash
docker-compose down -v
```

### Rebuild containers
```bash
docker-compose up --build
```

---

## Advanced: Using GPU (NVIDIA Only)

For significantly faster generation on NVIDIA GPUs:

1. Install NVIDIA Container Runtime
2. Modify `docker-compose.yml`:

```yaml
  ollama:
    image: ollama/ollama:latest
    runtime: nvidia
    environment:
      - NVIDIA_VISIBLE_DEVICES=all
```

3. Restart: `docker-compose down && docker-compose up`

---

## License

Free to use and modify for your projects.

## Support

- Check troubleshooting section above
- Review Flask/Ollama documentation
- Check Ollama status: http://localhost:11434/api/tags

---

## Tips for Best Results

1. **Be Specific** in product description
2. **Clear Target Audience** helps personalization
3. **Match Goal** to your actual campaign intent
4. **Edit Results** - AI is a starting point, not final product
5. **Try Different Models** to find best fit
6. **Test with Examples** first before real use

---

Happy script generating! 🎬
