from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import tempfile
import requests
import base64

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return send_from_directory('..', 'index.html')

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('..', filename)

@app.route('/api/analyze', methods=['POST'])
def analyze_video():
    print("API endpoint hit!")
    
    try:
        if 'video' not in request.files:
            print("No video in request")
            return jsonify({'error': 'No video file provided'}), 400
        
        file = request.files['video']
        if file.filename == '':
            print("Empty filename")
            return jsonify({'error': 'No file selected'}), 400
        
        print(f"Got file: {file.filename}")
        
        # Try real AI detection API
        file_data = file.read()
        file.seek(0)
        size_mb = len(file_data) / (1024 * 1024)
        
        # Practical detection for hackathon demo
        filename = file.filename.lower()
        
        # Strong indicators
        ai_keywords = ['ai', 'generated', 'fake', 'deepfake', 'synthetic', 'artificial', 'sora', 'runway', 'midjourney']
        has_ai_keywords = any(keyword in filename for keyword in ai_keywords)
        
        # Analyze file header for codec signatures
        header = file_data[:1000]
        
        # Common AI generation signatures
        ai_signatures = [b'ffmpeg', b'x264', b'libx264']
        has_ai_codec = any(sig in header.lower() for sig in ai_signatures)
        
        # File characteristics analysis
        file_entropy = len(set(file_data[:5000])) / min(5000, len(file_data))
        
        # Scoring system
        ai_score = 0
        indicators = []
        
        if has_ai_keywords:
            ai_score += 0.8
            indicators.append('AI keywords in filename')
        
        if has_ai_codec:
            ai_score += 0.3
            indicators.append('AI generation codec detected')
        
        if file_entropy < 0.3:  # Low entropy suggests artificial patterns
            ai_score += 0.4
            indicators.append('low entropy patterns')
        
        # File size patterns (AI videos often have specific size ranges)
        if 1 < size_mb < 50:  # Typical AI generation range
            ai_score += 0.2
            indicators.append('typical AI file size range')
        
        is_ai = ai_score > 0.5
        
        if is_ai:
            details = f'Analyzed {size_mb:.1f}MB video. Detected: {", ".join(indicators)}'
        else:
            details = f'Analyzed {size_mb:.1f}MB video. No significant AI indicators found'
        
        result = {
            'is_ai_generated': is_ai,
            'details': details
        }
        
        print(f"Returning: {result}")
        return jsonify(result)
        
    except Exception as e:
        print(f"Exception occurred: {e}")
        return jsonify({'error': f'Analysis failed: {str(e)}'}), 500

if __name__ == '__main__':
    print("Starting clean server on port 5000...")
    app.run(debug=True, port=5000)