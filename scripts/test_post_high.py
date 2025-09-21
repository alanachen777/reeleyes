import requests
import tempfile
from pathlib import Path

def main():
    # Create a small synthetic file with repeated bytes to trigger heuristics
    data = b'a' * 1024
    tf = tempfile.NamedTemporaryFile(delete=False, suffix='.bin')
    tf.write(data)
    tf.flush()
    tf.close()

    url = 'http://127.0.0.1:5000/api/analyze'
    files = {'video': open(tf.name, 'rb')}
    data = {'sensitivity': 'high'}
    try:
        r = requests.post(url, files=files, data=data, timeout=10)
        print('status', r.status_code)
        print(r.json())
    except Exception as e:
        print('request failed:', e)
    finally:
        files['video'].close()
        Path(tf.name).unlink(missing_ok=True)

if __name__ == '__main__':
    main()
