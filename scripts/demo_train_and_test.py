"""Demo: create a tiny labeled CSV, train the ML detector, and run a sample prediction.

This script is intended to be run locally with the project venv active. It will:
 - create a small CSV with toy features (+ labels)
 - call the training helper to save a model at backend/ai_detector.pkl
 - load the model and run a prediction on a sample metrics dict

Usage:
  python backend/demo_train_and_test.py
"""
import os
import csv
import tempfile
from train_ml import train
from ml_detector import predict_from_metrics

ROOT = os.path.dirname(__file__)

def make_csv(path):
    # columns: file_entropy,size_mb,run_frac,size_contrib,frame_blur_avg,label
    rows = [
        # AI-like (low entropy, small size, small blur)
        {'file_entropy': 0.05, 'size_mb': 0.99, 'run_frac': 0.0066, 'size_contrib': 0.155, 'frame_blur_avg': 5.0, 'label': 1},
        # real-like
        {'file_entropy': 0.45, 'size_mb': 12.0, 'run_frac': 0.12, 'size_contrib': 0.2, 'frame_blur_avg': 50.0, 'label': 0},
        # another AI-ish
        {'file_entropy': 0.12, 'size_mb': 1.7, 'run_frac': 0.02, 'size_contrib': 0.18, 'frame_blur_avg': 8.0, 'label': 1},
        # another real-ish
        {'file_entropy': 0.6, 'size_mb': 30.0, 'run_frac': 0.2, 'size_contrib': 0.2, 'frame_blur_avg': 80.0, 'label': 0},
    ]
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['file_entropy','size_mb','run_frac','size_contrib','frame_blur_avg','label'])
        writer.writeheader()
        for r in rows:
            writer.writerow(r)

def main():
    csv_path = os.path.join(ROOT, 'demo_data.csv')
    print('Writing demo CSV to', csv_path)
    make_csv(csv_path)
    print('Training model...')
    train(csv_path)
    print('Model trained. Running a test prediction...')
    sample_metrics = {'file_entropy': 0.049, 'size_mb': 0.99, 'run_frac': 0.0066, 'size_contrib': 0.155, 'frame_blur_avg': 5.0}
    res = predict_from_metrics(sample_metrics)
    print('Prediction result (ml):', res)

if __name__ == '__main__':
    main()
