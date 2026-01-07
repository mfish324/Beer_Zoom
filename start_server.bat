@echo off
echo ========================================
echo  Beer Zoom Gallery - Web Server
echo ========================================
echo.
echo Installing dependencies...
pip install -r requirements.txt
echo.
echo Starting web server...
echo.
echo ^>^> Open your browser to: http://localhost:5000
echo ^>^> Press Ctrl+C to stop the server
echo.
echo ========================================
echo.
python app.py
pause
