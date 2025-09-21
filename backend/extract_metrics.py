"""Batch-extract metrics from videos into a CSV for training.

Usage:
  python extract_metrics.py /path/to/video/folder output.csv

This uses the analyzer to compute metrics for each file and writes rows ready for training.
"""
import os
import sys
import csv
from analyzer import analyze_video_bytes

def process_folder(folder, out_csv):
    rows = []
    for fname in os.listdir(folder):
        path = os.path.join(folder, fname)
        if not os.path.isfile(path):
            continue
        with open(path, 'rb') as f:
            data = f.read()
        res = analyze_video_bytes(data, filename=fname, ignore_size=False, sensitivity='high')
        metrics = res.get('metrics', {})
        row = {
            'filename': fname,
            'file_entropy': metrics.get('file_entropy', 0.0),
            'size_mb': metrics.get('size_mb', 0.0),
            'run_frac': metrics.get('run_frac', 0.0),
            'size_contrib': metrics.get('size_contrib', 0.0),
            'frame_blur_avg': metrics.get('frame_blur_avg', 0.0),
        }
        rows.append(row)

    fieldnames = ['filename','file_entropy','size_mb','run_frac','size_contrib','frame_blur_avg']
    with open(out_csv, 'w', newline='', encoding='utf-8') as csvf:
        writer = csv.DictWriter(csvf, fieldnames=fieldnames)
        writer.writeheader()
        for r in rows:
            writer.writerow(r)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: extract_metrics.py /path/to/videos out.csv')
        sys.exit(1)
    process_folder(sys.argv[1], sys.argv[2])
