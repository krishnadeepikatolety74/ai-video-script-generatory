# Testing Guide - Video Script Generator

## Quick Test Examples

Use these examples to test your setup and understand the system's capabilities.

---

## Test 1: Fitness Product (Quick Test)

### Input:
```
Product Name: SmartFit Watch
Description: A wearable fitness tracker with heart rate monitoring, sleep tracking, and AI-powered workout recommendations. Water-resistant up to 50m.
Target Audience: Fitness enthusiasts aged 20-40
Campaign Goal: Drive sales
Duration: 30 seconds
```

### Expected Output:

**Hook:**
```
"Train smarter, not harder — your personal fitness coach on your wrist"
```

**Script:**
```
[SCENE 1] - ACTIVE WORKOUT
VOICEOVER: "Every heartbeat tells a story. SmartFit Watch turns your daily activity into actionable insights."

[SCENE 2] - NIGHT RECOVERY
VOICEOVER: "Sleep better. Train harder. Our AI learns what works for YOU."

[SCENE 3] - PRODUCT SHOWCASE
VOICEOVER: "Water-resistant, intelligent, yours. SmartFit Watch — fitness evolved."
```

**Scenes:**
```
1. Dynamic workout montage - person exercising with watch visible
2. Sleep tracking animation - watch on nightstand, sleep data visualization
3. Close-up of watch with real metrics display - heart rate, steps, calories
```

**CTA:**
```
"Get your SmartFit Watch today — Shop now at smartfit.com"
```

---

## Test 2: Eco Product (Brand Building)

### Input:
```
Product Name: EcoCup
Description: Reusable coffee cup made from 100% recycled plastic with insulated design. Keeps drinks hot for 6 hours.
Target Audience: Environmentally conscious professionals
Campaign Goal: Increase brand awareness
Duration: 30 seconds
```

### Expected Output Characteristics:
- Focus on environmental impact
- Professional, sophisticated tone
- Emphasis on sustainability
- Call to action about making a difference

---

## Test 3: Food Product (Entertainment)

### Input:
```
Product Name: ChocoBites
Description: Premium chocolate snacks with organic ingredients, no artificial additives. Perfect for guilt-free indulgence.
Target Audience: Health-conscious food lovers
Campaign Goal: Launch new product
Duration: 15 seconds
```

### Expected Output Characteristics:
- Short, punchy script
- Emphasis on taste and quality
- Focus on "guilt-free" aspect
- Energetic, engaging tone

---

## API Testing with cURL

### Test Hook Generation:
```bash
curl -X POST http://localhost:5000/api/generate-hook \
  -H "Content-Type: application/json" \
  -d '{
    "productName": "SmartFit Watch",
    "productDescription": "Wearable fitness tracker with heart rate monitoring",
    "targetAudience": "Fitness enthusiasts"
  }'
```

### Test Full Generation:
```bash
curl -X POST http://localhost:5000/api/generate-all \
  -H "Content-Type: application/json" \
  -d '{
    "productName": "SmartFit Watch",
    "productDescription": "Wearable fitness tracker with AI recommendations",
    "targetAudience": "Fitness enthusiasts aged 20-40",
    "campaignGoal": "Drive sales",
    "duration": 30
  }'
```

### Test Health Check:
```bash
curl http://localhost:5000/health
```

Expected response:
```json
{"status": "healthy", "ollama": "connected"}
```

---

## Manual Testing Checklist

### Phase 1: Setup Verification
- [ ] Ollama service is running (`ollama serve`)
- [ ] Model is downloaded (`ollama list` shows a model)
- [ ] Flask server is running (no errors in console)
- [ ] Frontend loads in browser without errors

### Phase 2: API Testing
- [ ] Health check endpoint returns "healthy"
- [ ] Hook generation works (returns valid JSON)
- [ ] Script generation works (takes 15-60 seconds)
- [ ] Scene generation works (returns list format)
- [ ] CTA generation works (short text)
- [ ] All-in-one endpoint works (returns 4 fields)

### Phase 3: UI Testing
- [ ] Form submits with valid data
- [ ] Status messages appear during generation
- [ ] Results display correctly in results panel
- [ ] Copy button works for each result
- [ ] Clear form button resets all fields
- [ ] Quick action buttons work individually

### Phase 4: Quality Testing
- [ ] Hook is attention-grabbing (under 20 words)
- [ ] Script is appropriate for duration (30s or 60s)
- [ ] Scenes are visual and actionable
- [ ] CTA is clear and action-oriented
- [ ] All content matches product/audience

---

## Performance Testing

### Measure Generation Time:

```bash
# Using time command (Linux/Mac)
time curl -X POST http://localhost:5000/api/generate-all \
  -H "Content-Type: application/json" \
  -d '{...}'

# Expected times (in seconds):
# Mistral: 15-30s
# Llama2: 30-45s
# OpenHermes: 60+s
```

### Monitor System Resources:

```bash
# Docker resource usage
docker stats

# System resources (Mac/Linux)
top
free -h

# System resources (Windows)
tasklist
```

---

## Test Product Examples

### Technology Products:
```
Product: CloudSync Pro
Description: Cloud storage solution with real-time sync, 256-bit encryption, unlimited versioning
Target Audience: Business professionals and developers
Campaign Goal: Drive sales
```

### Health & Wellness:
```
Product: VitaminMax
Description: Daily vitamin supplement with 15 essential nutrients, plant-based formula
Target Audience: Health-conscious millennials
Campaign Goal: Build community engagement
```

### Fashion:
```
Product: EcoJeans
Description: Sustainable denim made from organic cotton, ethical manufacturing
Target Audience: Fashion-conscious Gen Z consumers
Campaign Goal: Increase brand awareness
```

### Home & Garden:
```
Product: SmartPlant
Description: IoT plant monitor with soil moisture sensors and growth analytics
Target Audience: Urban gardening enthusiasts
Campaign Goal: Launch new product
```

---

## Expected Quality Indicators

### Good Hook ✅
- Starts with attention-grabber (question, statement, or benefit)
- 15-20 words max
- Specific to product
- Creates curiosity or resonates with audience

### Good Script ✅
- Clear progression through 2-3 scenes
- Voiceover matches video duration
- Benefits-focused
- Simple, clear language
- Action-oriented

### Good Scenes ✅
- Visually actionable (not just descriptions)
- Show product in use
- Highlight key benefits
- Appropriate for 30-60 second video

### Good CTA ✅
- Clear action (buy, visit, download, etc.)
- Includes where/how
- Urgent or compelling
- 20-25 words max
- Brand-specific

---

## Troubleshooting Tests

### If generation is slow (>90 seconds):
```bash
# Check if Ollama is responding
curl http://localhost:11434/api/tags

# Check system resources
docker stats  # For Docker
free -h       # For Linux
```

### If results are low quality:
```bash
# Try a different model
# In docker-compose.yml, change MODEL_NAME
# Or run: ollama pull llama2
```

### If API returns errors:
```bash
# Check Flask logs
docker-compose logs api

# Test endpoint directly
curl -v http://localhost:5000/health
```

### If frontend shows "Connection refused":
```bash
# Verify Flask is running
curl http://localhost:5000

# Verify CORS is enabled
# Check browser console for CORS errors
```

---

## Batch Testing Script

### Test multiple products at once:

```bash
#!/bin/bash

products=(
  '{"productName":"SmartWatch","productDescription":"Fitness tracker","targetAudience":"Athletes","campaignGoal":"Drive sales"}'
  '{"productName":"EcoCup","productDescription":"Reusable cup","targetAudience":"Eco-conscious","campaignGoal":"Awareness"}'
  '{"productName":"ChocoBites","productDescription":"Healthy chocolate","targetAudience":"Health lovers","campaignGoal":"Launch"}'
)

for product in "${products[@]}"; do
  echo "Testing: $product"
  curl -X POST http://localhost:5000/api/generate-all \
    -H "Content-Type: application/json" \
    -d "$product"
  echo -e "\n\n"
  sleep 5  # Wait between requests
done
```

---

## Acceptance Criteria

Your system is ready for production when:

- [ ] All 5 endpoints return valid JSON responses
- [ ] Generation time is under 120 seconds per request
- [ ] UI is responsive and displays results correctly
- [ ] Generated content is relevant to input data
- [ ] Copy-to-clipboard functionality works
- [ ] No console errors in browser or terminal
- [ ] Health check endpoint shows "healthy"
- [ ] At least 3 test products produce quality output

---

## Load Testing (Optional)

### Test with multiple concurrent requests:

```bash
# Install Apache Bench
# apt-get install apache2-utils (Linux)
# brew install httpd (Mac)

# Test 10 concurrent requests
ab -n 10 -c 10 http://localhost:5000/health

# Note: Ollama processes requests sequentially
# Multiple concurrent /generate-all requests will queue
```

---

## Browser Console Testing

Open browser DevTools (F12) and check console for errors:

```javascript
// Test API connection
fetch('http://localhost:5000/health')
  .then(r => r.json())
  .then(d => console.log('Connected:', d))
  .catch(e => console.error('Error:', e))

// Test full generation
fetch('http://localhost:5000/api/generate-all', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({
    productName: 'TestProduct',
    productDescription: 'Test description',
    targetAudience: 'Test audience',
    campaignGoal: 'Drive sales'
  })
})
  .then(r => r.json())
  .then(d => console.log('Result:', d))
  .catch(e => console.error('Error:', e))
```

---

## Next Steps After Testing

1. ✅ Verify all tests pass
2. ✅ Customize prompts for your brand voice
3. ✅ Deploy to production (see CONFIGURATION.md)
4. ✅ Monitor performance
5. ✅ Gather user feedback
6. ✅ Iterate on prompts based on feedback

---

For issues, check the troubleshooting section in README.md
