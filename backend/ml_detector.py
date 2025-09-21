"""Minimal ML detector scaffold.

This module provides a small feature extractor and a wrapper around a scikit-learn
classifier. Training is optional; if no model is present the detector falls back
to heuristic analyzer.
"""
import os
import pickle
from typing import Dict, Any

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'ai_detector.pkl')

def extract_features_from_metrics(metrics: Dict[str, Any]) -> Dict[str, float]:
    # Simple mapping of analyzer metrics to numeric features
    return {
        'file_entropy': float(metrics.get('file_entropy', 0.0)),
        'size_mb': float(metrics.get('size_mb', 0.0)),
        'run_frac': float(metrics.get('run_frac', 0.0)),
        'size_contrib': float(metrics.get('size_contrib', 0.0)),
        'frame_blur_avg': float(metrics.get('frame_blur_avg', 0.0)),
    }

def load_model():
    if not os.path.exists(MODEL_PATH):
        return None
    with open(MODEL_PATH, 'rb') as f:
        return pickle.load(f)

def predict_from_metrics(metrics: Dict[str, Any]):
    model = load_model()
    if model is None:
        return None
    feats = extract_features_from_metrics(metrics)
    X = [[feats['file_entropy'], feats['size_mb'], feats['run_frac'], feats['size_contrib'], feats['frame_blur_avg']]]
    y_prob = model.predict_proba(X)[0,1] if hasattr(model, 'predict_proba') else None
    y_pred = model.predict(X)[0]
    return {'ml_pred': bool(y_pred), 'ml_prob': float(y_prob) if y_prob is not None else None}
