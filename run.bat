@echo off
echo Starting ReelEyes...
cd backend
python -m pip install Flask Flask-CORS
python app.py
pause