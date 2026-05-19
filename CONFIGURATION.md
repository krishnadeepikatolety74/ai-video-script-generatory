# Configuration Guide - Video Script Generator

## Environment Variables

### Flask Configuration
```bash
# Host and port
FLASK_HOST=0.0.0.0
FLASK_PORT=5000

# Environment
FLASK_ENV=development  # or production

# Debug mode
FLASK_DEBUG=True  # or False
```

### Ollama Configuration
```bash
# Ollama server connection
OLLAMA_HOST=http://localhost:11434

# Model selection
MODEL_NAME=mistral  # Options: mistral, llama2, neural-chat, openhermes

# Timeout for API calls (seconds)
TIMEOUT=120
```

### Application Configuration
```bash
# Temperature (creativity level: 0.0-1.0)
# Lower = more focused, Higher = more creative
TEMPERATURE=0.7

# Max tokens per response
MAX_TOKENS=500  # Hook, CTA
MAX_TOKENS=300  # Script, Scenes
```

## Model Configuration

### Changing the Model

#### Docker Method:
Edit `docker-compose.yml`:
```yaml
environment:
  - MODEL_NAME=llama2  # Change this
```

Then restart:
```bash
docker-compose down
docker-compose up
```

#### Manual Setup:
Set environment variable:
```bash
# Linux/Mac
export MODEL_NAME=llama2
python app.py

# Windows
set MODEL_NAME=llama2
python app.py
```

### Available Models

```
mistral          - Fast, lightweight, good for scripts
llama2           - Balanced quality and speed
neural-chat      - Optimized for conversations
openhermes       - Highest quality, slowest
dolphin-mixtral  - Experimental, mixed results
```

### Download Models

```bash
# Pull a model
ollama pull llama2

# List available models
ollama list

# Remove a model
ollama rm llama2
```

## Prompt Customization

Edit prompts in `app.py` to match your brand voice:

### Hook Prompt (Line ~30)
```python
prompt = f"""Generate a catchy, attention-grabbing hook (max 20 words) for a video about:
Product: {product_name}
Description: {product_description}
Target Audience: {target_audience}

Hook should start with a question, surprise fact, or bold statement.
Return ONLY the hook text, nothing else."""
```

**Customize by:**
- Change "max 20 words" to your preference
- Add tone instructions: "Make it humorous" or "Keep it professional"
- Specify format: "Use a question" or "Start with an action verb"

### Script Prompt (Line ~40)
```python
prompt = f"""Write a {duration_seconds}-second video script for a promotional video.
...
Keep it concise, engaging, and persuasive. Use simple language.
Include 2-3 scenes maximum."""
```

**Customize by:**
- Add scene requirements: "Include testimonial"
- Specify style: "Conversational tone" or "Storytelling approach"
- Add constraints: "No technical jargon"

### Scene Suggestions Prompt (Line ~65)
```python
prompt = f"""Suggest 3 key visual scenes for a promotional video about:
...
Focus on visually engaging, practical scenes."""
```

**Customize by:**
- Change number of scenes
- Add style: "Cinematic", "Minimalist", "Documentary style"
- Specify elements: "Include product shots", "Show customer benefits"

### CTA Prompt (Line ~80)
```python
prompt = f"""Create a strong call-to-action ending (max 25 words) for a video about:
...
Return ONLY the CTA text."""
```

**Customize by:**
- Change max words
- Specify format: "Include emoji", "Make it urgency-driven"
- Add brand voice: "Professional tone", "Playful and fun"

## Temperature Settings

Temperature controls how creative/random the model is:

```python
# In app.py, change temperature parameter:
response = requests.post(
    f'{OLLAMA_HOST}/api/generate',
    json={
        ...
        'temperature': 0.7,  # Change this
        ...
    }
)
```

**Recommendations:**
```
Scripts & Hooks: 0.7-0.8  (balanced)
CTAs: 0.5-0.6  (focused, direct)
Scenes: 0.8-0.9  (creative)
```

## API Response Time Optimization

### Reduce Response Time

1. **Smaller max_tokens:**
   ```python
   'num_predict': 200  # Instead of 500
   ```

2. **Faster model:**
   ```
   mistral (fastest)
   neural-chat (fast)
   llama2 (balanced)
   openhermes (slowest)
   ```

3. **System optimization:**
   - Close other applications
   - Use dedicated GPU (NVIDIA)
   - Increase RAM
   - Use SSD for disk

### Expected Times (on 4GB RAM)
- Mistral: 15-30 seconds
- Llama2: 30-45 seconds
- OpenHermes: 60+ seconds

## CORS Configuration

If frontend and backend are on different origins, CORS is already configured:

```python
from flask_cors import CORS
CORS(app)  # Allow all origins
```

**Restrict to specific origin:**
```python
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})
```

## Logging Configuration

Add logging to track requests:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@app.route('/api/generate-all', methods=['POST'])
def api_generate_all():
    logger.info(f"Generating script for: {data['productName']}")
    ...
```

## Database Integration (Optional)

To save generated scripts:

```python
# Install: pip install sqlite3
import sqlite3
from datetime import datetime

def save_generation(product_name, hook, script, scenes, cta):
    conn = sqlite3.connect('scripts.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS scripts
                 (id INTEGER PRIMARY KEY, product TEXT, hook TEXT, 
                  script TEXT, scenes TEXT, cta TEXT, created_at TEXT)''')
    c.execute("INSERT INTO scripts VALUES (NULL, ?, ?, ?, ?, ?, ?)",
              (product_name, hook, script, scenes, cta, datetime.now()))
    conn.commit()
    conn.close()

# Call in your endpoints:
save_generation(data['productName'], hook, script, scenes, cta)
```

## Rate Limiting (Optional)

Add request rate limiting:

```python
# Install: pip install Flask-Limiter
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

@app.route('/api/generate-all', methods=['POST'])
@limiter.limit("5 per minute")
def api_generate_all():
    ...
```

## Production Deployment

### Using Gunicorn:

```bash
# Install: pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Environment for Production:

```python
# In app.py
import os

if os.getenv('FLASK_ENV') == 'production':
    app.run(debug=False)
else:
    app.run(debug=True)
```

### Docker Production:

```yaml
# docker-compose.yml
services:
  api:
    ...
    environment:
      - FLASK_ENV=production
    command: gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## Security Considerations

### Input Validation

```python
def validate_input(data):
    if len(data['productName']) > 200:
        return False, "Product name too long"
    if len(data['productDescription']) > 1000:
        return False, "Description too long"
    return True, "Valid"
```

### Rate Limiting (see above)

### HTTPS (in production)

```python
# Use reverse proxy like Nginx with SSL
```

### Environment Secrets

```bash
# Use .env file (don't commit to git)
OLLAMA_HOST=http://ollama:11434
API_KEY=your_secret_key
```

## Monitoring

### Health Check Endpoint

Already included:
```
GET /health
Returns: {"status": "healthy", "ollama": "connected"}
```

### Add Metrics:

```python
from prometheus_client import Counter, Histogram, make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware

request_count = Counter('requests_total', 'Total requests')
request_duration = Histogram('request_duration_seconds', 'Request duration')

@app.route('/api/generate-all', methods=['POST'])
def api_generate_all():
    request_count.inc()
    # ... rest of code
```

## Troubleshooting Configuration

### Model Loading Slowly

```bash
# Preload model
ollama pull mistral

# Or in code, warm up:
call_ollama("Test", 10)
```

### Out of Memory

Reduce model size:
```
Use: mistral (4GB)
Avoid: openhermes (7GB)
```

### API Timeout

Increase timeout:
```python
TIMEOUT = 180  # 3 minutes instead of 2
```

---

## Quick Reference Commands

```bash
# List all configuration
env | grep -E "OLLAMA|FLASK|MODEL"

# Test Ollama
curl http://localhost:11434/api/tags

# View Flask logs
docker-compose logs -f api

# Restart services
docker-compose restart

# Test API
curl -X POST http://localhost:5000/health
```

---

For more help, see README.md
