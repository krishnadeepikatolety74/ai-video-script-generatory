# ⚡ Quick Start Checklist - 3 Hour Deployment

Complete this in order for fastest setup.

---

## 🎯 PHASE 1: Preparation (10 minutes)

- [ ] Have all project files in one folder:
  - `app.py`
  - `index.html`
  - `requirements.txt`
  - `docker-compose.yml`
  - `Dockerfile`

- [ ] System check:
  - [ ] Docker Desktop installed? (https://docker.com)
  - [ ] 10GB free disk space?
  - [ ] 4GB+ RAM available?
  - [ ] Internet connection active?

---

## 🚀 PHASE 2: Launch (5 minutes)

### Option A: Docker (Recommended - Fastest)

```bash
# 1. Navigate to project folder
cd /path/to/video-script-generator

# 2. Start everything
docker-compose up
```

**Wait for:**
- ✅ "Ollama API running on 0.0.0.0:11434"
- ✅ "Running on http://0.0.0.0:5000"

### Option B: Manual Setup

```bash
# 1. Install Ollama from https://ollama.ai
# 2. Start Ollama in new terminal
ollama serve

# 3. Download model in new terminal
ollama pull mistral

# 4. Install Python packages
pip install -r requirements.txt

# 5. Start Flask
python app.py

# 6. Open browser
open index.html  # or double-click in file explorer
```

---

## ✅ PHASE 3: Verification (10 minutes)

### Test 1: Health Check
- [ ] Go to: http://localhost:5000/health
- [ ] See: `{"status":"healthy","ollama":"connected"}`

### Test 2: Quick Generation
- [ ] Open: http://localhost:5000
- [ ] Fill form with sample data:
  - Product: "SmartWater Bottle"
  - Description: "AI-powered water bottle with hydration tracking"
  - Audience: "Fitness enthusiasts"
  - Goal: "Drive sales"

- [ ] Click "Generate All"
- [ ] Wait 30-60 seconds
- [ ] See results appear

### Test 3: Copy Function
- [ ] Click "Copy" on any result
- [ ] Paste in text editor
- [ ] Verify content copied correctly

---

## 📝 PHASE 4: Customization (Optional - 10 minutes)

### Customize for Your Brand

Edit `app.py` prompts (around these lines):

**Hook (line ~30):** Add your brand voice
```python
prompt = f"""Generate a catchy hook for:
Product: {product_name}
...
[ADD YOUR INSTRUCTIONS HERE]"""
```

**Script (line ~40):** Adjust tone
```python
prompt = f"""Write a script...
[ADD STYLE INSTRUCTIONS]"""
```

### Change Model (if slow)

Edit `docker-compose.yml`:
```yaml
environment:
  - MODEL_NAME=mistral  # Change this line
```

Restart:
```bash
docker-compose restart
```

---

## 🎬 PHASE 5: Production Use (30 minutes)

### Create Your First Script

1. **Fill in product info**
   - Real product name
   - Detailed description (2-3 sentences)
   - Specific target audience
   - Clear campaign goal

2. **Generate all components**
   - Click "Generate All"
   - Takes 30-90 seconds depending on model

3. **Review & Edit**
   - Copy hook to document
   - Adjust script for your video style
   - Review scene suggestions
   - Refine CTA for your platform

4. **Use in Your Workflow**
   - Import script into video editor (Adobe Premiere, Final Cut, DaVinci)
   - Follow scene suggestions for visual planning
   - Record voiceover using hook/script
   - Add CTA at the end
   - Export and publish

---

## 🐛 Quick Troubleshooting

### "Connection refused"
```bash
# Make sure Docker/services are running
docker-compose ps

# If not running:
docker-compose up
```

### "Generation taking >2 minutes"
```bash
# Try faster model
# Edit docker-compose.yml: MODEL_NAME=mistral
# Or close other apps to free RAM
```

### "Port already in use"
```bash
# Kill process on port 5000
# Docker: docker-compose down
# Manual: lsof -i :5000 | grep LISTEN | awk '{print $2}' | xargs kill
```

### "Ollama not responding"
```bash
# Check if Ollama has model downloaded
ollama list

# If empty, download one:
ollama pull mistral
```

---

## 📊 Expected Performance

| Task | Time | Notes |
|------|------|-------|
| First launch | 3-5 min | Downloads model |
| Generate hook | 5-15 sec | Quick |
| Generate script | 20-45 sec | Longest |
| Generate scenes | 15-30 sec | Medium |
| Generate CTA | 5-15 sec | Quick |
| **Generate All** | **30-90 sec** | Fastest overall |

---

## 🎯 Success Criteria

Your system is ready when ALL are ✅:

- [ ] Services start without errors
- [ ] Health check returns "healthy"
- [ ] Web interface loads in browser
- [ ] Form submission works
- [ ] Results display within 2 minutes
- [ ] Copy button works
- [ ] Generated content is relevant
- [ ] No error messages in console

---

## 📚 Next: Learn & Optimize

After successful deployment:

1. **Read** `README.md` for full documentation
2. **Check** `TESTING.md` for test examples
3. **Review** `CONFIGURATION.md` for customization
4. **Optimize** based on your needs

---

## 🚨 If Something Goes Wrong

### Check Logs
```bash
# Docker logs
docker-compose logs -f

# Or check system terminal
# Look for error messages
```

### Reset Everything
```bash
# Stop services
docker-compose down

# Remove volumes (deletes models)
docker-compose down -v

# Start fresh
docker-compose up
```

### Get Help
1. Check `README.md` troubleshooting section
2. Review `TESTING.md` for validation
3. Check `CONFIGURATION.md` for setup options

---

## ⏱️ Timeline Summary

| Phase | Task | Time |
|-------|------|------|
| 1 | Prep & check | 10 min |
| 2 | Launch services | 5 min |
| 3 | Verify working | 10 min |
| 4 | Customize (optional) | 10 min |
| 5 | First script | 30 min |
| **TOTAL** | **Ready to use** | **~60-90 min** |

---

## 🎉 Ready to Go!

Once verified, you can:
- ✅ Generate scripts in 30-60 seconds
- ✅ Customize for any product
- ✅ Export for video editing
- ✅ Use offline (no API keys needed)
- ✅ Deploy to team/company

---

## 💡 Pro Tips

1. **Batch Generate** - Run multiple products in a row
2. **Keep Notes** - Save prompts that work well
3. **Edit Boldly** - AI is starting point, not final
4. **Test Early** - Verify output quality before using
5. **Monitor Speed** - Faster model = less quality trade-off

---

## 🔄 Daily Use Workflow

1. Open browser: `http://localhost:5000`
2. Fill product form
3. Click "Generate All" (30-60 sec wait)
4. Copy results
5. Paste into video editor
6. Edit and customize
7. Create video
8. Publish

**Repeat for next product!**

---

Done! You're all set. 🎬

For detailed help, see README.md
