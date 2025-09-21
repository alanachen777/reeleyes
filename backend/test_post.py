import requests
import sys

def main():
    fpath = 'backend/collected_videos/Download (1).mp4'
    url = 'http://127.0.0.1:5000/api/analyze'
    with open(fpath,'rb') as f:
        files = {'video': (fpath, f, 'video/mp4')}
        data = {'sensitivity': 'high', 'debug_metrics': 'true'}
        r = requests.post(url, files=files, data=data)
        print('Status', r.status_code)
        print(r.text)

if __name__ == '__main__':
    main()
