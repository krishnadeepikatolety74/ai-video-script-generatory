# pyrefly: ignore [missing-import]
from dotenv import load_dotenv
# pyrefly: ignore [missing-import]
import os
# pyrefly: ignore [missing-import]
from flask import Flask,jsonify,request
# pyrefly: ignore [missing-import]
from flask import render_template
# pyrefly: ignore [missing-import]
from groq import Groq
# pyrefly: ignore [missing-import]
from flask_cors import CORS
# pyrefly: ignore [missing-import]
from datetime import datetime
load_dotenv()
app=Flask(__name__)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))  

def call_ai(prompt):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="llama-3.3-70b-versatile"
        )

        return chat_completion.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"

def generate_hook(product_name, product_description, target_audience):
    """Generate attention-grabbing hook"""
    prompt = f"""Generate a catchy, attention-grabbing hook (max 20 words) for a video about:
Product: {product_name}
Description: {product_description}
Target Audience: {target_audience}

Hook should start with a question, surprise fact, or bold statement.
Return ONLY the hook text, nothing else."""
    
    return call_ai(prompt)

def generate_script(product_name, product_description, target_audience, campaign_goal, duration_seconds=30):
    """Generate complete video script"""
    
    prompt = f"""Write a {duration_seconds}-second video script for a promotional video.

Product: {product_name}
Description: {product_description}
Target Audience: {target_audience}
Campaign Goal: {campaign_goal}
Duration: {duration_seconds} seconds (approximately {int(duration_seconds / 3)} sentences)

Format the script as:
[SCENE #] - SCENE DESCRIPTION
VOICEOVER/DIALOGUE: [What is said]

Keep it concise, engaging, and persuasive. Use simple language.
Include 2-3 scenes maximum."""

    return call_ai(prompt)

def generate_scenes(product_name, product_description, campaign_goal):
    """Generate visual scene suggestions"""
    
    prompt = f"""Suggest 3 key visual scenes for a promotional video about:
Product: {product_name}
Description: {product_description}
Campaign Goal: {campaign_goal}

Format as a numbered list with scene descriptions (2-3 sentences each).
Focus on visually engaging, practical scenes."""

    return call_ai(prompt)

def generate_cta(product_name, campaign_goal, target_audience):
    """Generate call-to-action ending"""
    
    prompt = f"""Create a strong call-to-action ending (max 25 words) for a video about:
Product: {product_name}
Campaign Goal: {campaign_goal}
Target Audience: {target_audience}

The CTA should be clear, compelling, and action-oriented.
Include where to find/buy the product if applicable.
Return ONLY the CTA text."""

    return call_ai(prompt)

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/generate-hook', methods=['POST'])
def api_generate_hook():
    """API endpoint for hook generation"""
    data = request.json
    
    if not all(k in data for k in ['productName', 'productDescription', 'targetAudience']):
        return jsonify({'error': 'Missing required fields'}), 400
    
    hook = generate_hook(
        data['productName'],
        data['productDescription'],
        data['targetAudience']
    )
    
    return jsonify({'hook': hook, 'timestamp': datetime.now().isoformat()}), 200

@app.route('/api/generate-script', methods=['POST'])
def api_generate_script():
    """API endpoint for script generation"""
    data = request.json
    
    required = ['productName', 'productDescription', 'targetAudience', 'campaignGoal']
    if not all(k in data for k in required):
        return jsonify({'error': 'Missing required fields'}), 400
    
    duration = data.get('duration', 30)
    
    script = generate_script(
        data['productName'],
        data['productDescription'],
        data['targetAudience'],
        data['campaignGoal'],
        duration
    )
    
    return jsonify({'script': script, 'timestamp': datetime.now().isoformat()}), 200

@app.route('/api/generate-scenes', methods=['POST'])
def api_generate_scenes():
    """API endpoint for scene suggestions"""
    data = request.json
    
    required = ['productName', 'productDescription', 'campaignGoal']
    if not all(k in data for k in required):
        return jsonify({'error': 'Missing required fields'}), 400
    
    scenes = generate_scenes(
        data['productName'],
        data['productDescription'],
        data['campaignGoal']
    )
    
    return jsonify({'scenes': scenes, 'timestamp': datetime.now().isoformat()}), 200

@app.route('/api/generate-cta', methods=['POST'])
def api_generate_cta():
    """API endpoint for CTA generation"""
    data = request.json
    
    required = ['productName', 'campaignGoal', 'targetAudience']
    if not all(k in data for k in required):
        return jsonify({'error': 'Missing required fields'}), 400
    
    cta = generate_cta(
        data['productName'],
        data['campaignGoal'],
        data['targetAudience']
    )
    
    return jsonify({'cta': cta, 'timestamp': datetime.now().isoformat()}), 200

@app.route('/api/generate-all', methods=['POST'])
def api_generate_all():
    """API endpoint to generate all components at once"""
    data = request.json
    
    required = ['productName', 'productDescription', 'targetAudience', 'campaignGoal']
    if not all(k in data for k in required):
        return jsonify({'error': 'Missing required fields'}), 400
    
    duration = data.get('duration', 30)
    
    # Generate all components
    hook = generate_hook(
        data['productName'],
        data['productDescription'],
        data['targetAudience']
    )
    
    script = generate_script(
        data['productName'],
        data['productDescription'],
        data['targetAudience'],
        data['campaignGoal'],
        duration
    )
    
    scenes = generate_scenes(
        data['productName'],
        data['productDescription'],
        data['campaignGoal']
    )
    
    cta = generate_cta(
        data['productName'],
        data['campaignGoal'],
        data['targetAudience']
    )
    
    return jsonify({
        'hook': hook,
        'script': script,
        'scenes': scenes,
        'cta': cta,
        'timestamp': datetime.now().isoformat()
    }), 200


@app.route('/test-ai')
def test_ai():
    hook = generate_hook(
        "iPhone 14 Pro Max",
        "The latest iPhone with A16 Bionic chip, ProRAW camera system, and Dynamic Island",
        "Tech enthusiasts, Apple users, professionals"
    )
    return jsonify({'hook': hook})  

if __name__ == '__main__':
    app.run(debug=True)
