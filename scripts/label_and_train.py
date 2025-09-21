"""Interactive helper: label extracted metrics and train the ML model.

Usage:
  python label_and_train.py collected_metrics.csv

The script will prompt for a label (0 or 1) for each filename in the CSV and then call
`train_ml.train()` to produce `backend/ai_detector.pkl`.
"""
import sys
import csv
import os
from train_ml import train

ROOT = os.path.dirname(__file__)

def label_csv(in_csv, out_csv):
    rows = []
    with open(in_csv, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames if reader.fieldnames else []
        for r in reader:
            fname = r.get('filename', '<unknown>')
            print('\nFilename:', fname)
            print('Metrics:', {k: v for k, v in r.items() if k != 'filename'})
            while True:
                val = input('Enter label for this file (1 for AI, 0 for real, s to skip): ').strip().lower()
                if val in ('0','1'):
                    r['label'] = int(val)
                    break
                if val == 's':
                    r['label'] = ''
                    break
                print('Please enter 0, 1, or s')
            rows.append(r)

    # ensure output columns
    out_fields = list(fieldnames) + ['label'] if 'label' not in fieldnames else fieldnames
    with open(out_csv, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=out_fields)
        writer.writeheader()
        for r in rows:
            writer.writerow(r)

def main():
    if len(sys.argv) < 2:
        print('Usage: label_and_train.py collected_metrics.csv')
        return
    in_csv = sys.argv[1]
    if not os.path.exists(in_csv):
        print('Input CSV not found:', in_csv)
        return
    out_csv = os.path.join(ROOT, 'collected_metrics_labeled.csv')
    label_csv(in_csv, out_csv)
    print('Labeled CSV written to', out_csv)
    print('Training model from labeled CSV...')
    train(out_csv)

if __name__ == '__main__':
    main()
