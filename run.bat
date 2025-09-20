@echo off
echo Starting ReelEyes...
cd backend
echo Installing dependencies...
python -m pip install --no-build-isolation -r requirements.txt
if %errorlevel% neq 0 (
    echo Error installing dependencies
    pause
    exit /b 1
)
echo Starting server...
python app.py
if %errorlevel% neq 0 (
    echo Error starting server
    pause
    exit /b 1
)
pause