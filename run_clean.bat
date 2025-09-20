@echo off
echo Starting Clean ReelEyes...
cd backend
python -m pip install requests
python clean_app.py
pause