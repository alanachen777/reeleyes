from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import tempfile

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return send_from_directory('../frontend', 'index.html')

@app.route('/feed')
def feed():
    return send_from_directory('../frontend', 'feed.html')

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('../frontend', filename)

@app.route('/logo/<path:filename>')
def logo_files(filename):
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    logo_dir = os.path.join(base_dir, 'logo')
    return send_from_directory(logo_dir, filename)

def analyze_video_simple(file_data, filename):
    """Simple AI detection for hackathon demo"""
    size_mb = len(file_data) / (1024 * 1024)
    filename_lower = filename.lower()
    
    # Check for AI keywords in filename
    ai_keywords = ['ai', 'generated', 'fake', 'deepfake', 'synthetic', 'artificial', 'sora', 'runway', 'midjourney']
    has_ai_keywords = any(keyword in filename_lower for keyword in ai_keywords)
    
    # Check file header for codec signatures
    header = file_data[:1000].lower()
    ai_signatures = [b'ffmpeg', b'x264', b'libx264']
    has_ai_codec = any(sig in header for sig in ai_signatures)
    
    # Calculate entropy (uniqueness of bytes)
    sample = file_data[:5000]
    file_entropy = len(set(sample)) / min(5000, len(sample)) if sample else 0
    
    # Scoring
    score = 0
    indicators = []
    
    if has_ai_keywords:
        score += 0.8
        indicators.append('AI keywords in filename')
    
    if has_ai_codec:
        score += 0.3
        indicators.append('AI generation codec detected')
    
    if file_entropy < 0.3:
        score += 0.4
        indicators.append('low entropy patterns')
    
    if 1 < size_mb < 50:
        score += 0.2
        indicators.append('typical AI file size range')
    
    is_ai = score > 0.5
    
    return {
        'is_ai_generated': is_ai,
        'details': f'Analyzed {size_mb:.1f}MB video. ' + (f'Detected: {", ".join(indicators)}' if is_ai else 'No significant AI indicators found')
    }

@app.route('/api/analyze', methods=['POST'])
def analyze_video():

    
    try:
        if 'video' not in request.files:
            return jsonify({'error': 'No video file provided'}), 400
        
        file = request.files['video']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
    
        
        file_data = file.read()
        result = analyze_video_simple(file_data, file.filename)
        

        return jsonify(result)
        
    except Exception as e:

        return jsonify({'error': f'Analysis failed: {str(e)}'}), 500

if __name__ == '__main__':

    app.run(debug=True, port=5000)