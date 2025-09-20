from flask import Flask, request, jsonify
import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model # sub for deepfake model in both

app = Flask(__name__)

# Load your Deep-Fake-Detector-v2-Model
MODEL_PATH = 'Deep-Fake-Detector-v2-Model.h5'
model = load_model(MODEL_PATH)

def preprocess_image(image_path):
    # Adjust preprocessing to match model's input requirements
    img = cv2.imread(image_path)
    img = cv2.resize(img, (224, 224))  # resize this to model input size
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    return img

def detect_ai_generated_content(filepath):
    ext = filepath.lower().split('.')[-1]
    if ext in ['jpg', 'jpeg', 'png']:
        img = preprocess_image(filepath)
        pred = model.predict(img)
        return pred[0][0] > 0.5  # Adjust threshold as needed?
    elif ext in ['mp4', 'mov', 'avi']:
        cap = cv2.VideoCapture(filepath)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        ai_frames = 0
        checked_frames = 0
        for i in range(0, frame_count, max(1, frame_count // 10)):
            cap.set(cv2.CAP_PROP_POS_FRAMES, i)
            ret, frame = cap.read()
            if not ret:
                continue
            temp_path = "temp_frame.jpg"
            cv2.imwrite(temp_path, frame)
            img = preprocess_image(temp_path)
            pred = model.predict(img)
            if pred[0][0] > 0.5:
                ai_frames += 1
            checked_frames += 1
            os.remove(temp_path)
        cap.release()
        return ai_frames > checked_frames // 2
    else:
        return None

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['media']
    filename = file.filename
    filepath = os.path.join('uploads', filename)
    file.save(filepath)

    result = detect_ai_generated_content(filepath)
    os.remove(filepath)
    if result is None:
        output = "Unsupported file type"
    else:
        output = "AI Generated" if result else "Human Created"
    return jsonify({'result': output})

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(debug=True)
