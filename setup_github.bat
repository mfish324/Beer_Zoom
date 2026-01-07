@echo off
echo ========================================
echo  Beer Zoom Gallery - GitHub Setup
echo ========================================
echo.
echo This script will help you push to GitHub
echo.
echo Step 1: Make sure you're in the Beer_Zoom folder
echo         (If not, exit and run: cd path\to\Beer_Zoom)
echo.
pause
echo.
echo Step 2: Initializing git repository...
git init
git branch -M main
echo.
echo Step 3: Adding remote repository...
git remote add origin https://github.com/mfish324/Beer_Zoom.git
echo.
echo Step 4: Adding all files...
git add .
echo.
echo Step 5: Creating commit...
git commit -m "Initial commit: Beer Zoom Gallery web app"
echo.
echo Step 6: Pushing to GitHub...
echo (You may be prompted for GitHub credentials)
git push -u origin main
echo.
echo ========================================
echo Done! Check https://github.com/mfish324/Beer_Zoom
echo ========================================
pause
