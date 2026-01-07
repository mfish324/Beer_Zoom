@echo off
echo ========================================
echo  Beer Zoom Gallery - Photo Uploader
echo ========================================
echo.
echo This will upload photos from your BeerZoom folder to Cloudinary
echo.
echo Make sure you have set your CLOUDINARY_URL:
echo   set CLOUDINARY_URL=cloudinary://your-url-here
echo.
pause
echo.
echo Installing cloudinary package...
pip install cloudinary
echo.
echo Uploading photos...
echo.
python upload_to_cloudinary.py
echo.
echo ========================================
pause
