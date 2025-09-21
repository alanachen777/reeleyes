from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import tempfile
import requests
import base64

from analyzer import analyze_video_bytes
from ml_detector import predict_from_metrics

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return send_from_directory('../frontend', 'index.html')

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('../frontend', filename)


# Serve repository-level static directories like logo/ explicitly so paths like
# /logo/ReelEyes.png work regardless of which frontend folder is being served.
@app.route('/logo/<path:filename>')
def logo_files(filename):
    # Resolve absolute path to the repo-level logo directory
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    logo_dir = os.path.join(base_dir, 'logo')
    return send_from_directory(logo_dir, filename)

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
        
        # Read file bytes once and analyze with the analyzer module
        file_data = file.read()
        file.seek(0)

        # Optional client flags
        ignore_size = request.form.get('ignore_size', 'false').lower() in ('1', 'true', 'yes')
        sensitivity = request.form.get('sensitivity', 'medium')
        debug_metrics = request.form.get('debug_metrics', 'false').lower() in ('1', 'true', 'yes')

        analysis = analyze_video_bytes(file_data, filename=file.filename, ignore_size=ignore_size, sensitivity=sensitivity)

        # Provide a human-friendly summary alongside numeric confidence
        confidence = analysis['confidence']
        indicators = analysis['indicators']
        size_mb = analysis['size_mb']
        metrics = analysis.get('metrics', None)

        # Instead of a hard boolean based on size, return confidence and let frontend threshold
        # But lower server-side threshold when sensitivity is high
        threshold = 0.6
        if sensitivity and sensitivity.lower() == 'high':
            threshold = 0.45

        result = {
            'confidence': confidence,
            'is_ai_generated': confidence >= threshold,
            'indicators': indicators,
            'size_mb': size_mb,
            'ignored_size': ignore_size,
            'sensitivity': sensitivity,
        }

        if debug_metrics and metrics is not None:
            result['metrics'] = metrics

        # include ML prediction if a model is available
        ml_res = predict_from_metrics(metrics or {})
        if ml_res is not None:
            result['ml'] = ml_res

        print(f"Returning: {result}")
        return jsonify(result)
        
    except Exception as e:
        print(f"Exception occurred: {e}")
        return jsonify({'error': f'Analysis failed: {str(e)}'}), 500

if __name__ == '__main__':
    print("Starting clean server on port 5000...")
    app.run(debug=True, port=5000)