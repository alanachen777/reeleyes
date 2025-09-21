"""Training helper for the minimal ML detector.

Usage (optional): collect a CSV with columns file_entropy,size_mb,run_frac,size_contrib,frame_blur_avg,label
and run this script to train a random forest classifier and save it to `ai_detector.pkl`.
"""
import os
import sys
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

ROOT = os.path.dirname(__file__)
MODEL_PATH = os.path.join(ROOT, 'ai_detector.pkl')

def train(csv_path: str):
    df = pd.read_csv(csv_path)
    X = df[['file_entropy','size_mb','run_frac','size_contrib','frame_blur_avg']].fillna(0)
    y = df['label']
    clf = RandomForestClassifier(n_estimators=100, random_state=0)
    clf.fit(X, y)
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(clf, f)
    print('Saved model to', MODEL_PATH)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: train_ml.py data.csv')
        sys.exit(1)
    train(sys.argv[1])
