# 🍺 Beer Zoom Gallery - Complete Package

Your monthly Zoom beer meetings deserve an awesome photo gallery! This package gives you everything you need to create either a **static website** or a **live auto-updating website**.

---

## 📦 What's Included

### **For Static HTML Gallery:**
- `beer-zoom-gallery.html` - Original standalone HTML gallery
- `organize_photos.py` - Script to scan photos and generate HTML
- `run_organizer.bat` - Quick-run script for Windows

### **For Live Web Application:**
- `app.py` - Flask web server (auto-updates!)
- `templates/gallery.html` - Dynamic template
- `requirements.txt` - Python dependencies
- `start_server.bat` - Local server launcher
- `DEPLOYMENT_GUIDE.md` - How to host online

---

## 🎯 Which Version Should You Use?

### **Option A: Static HTML** (Simple sharing)
**Use if:** You want to zip/email the gallery or host on basic file storage

**Pros:**
- ✅ No server needed
- ✅ Works offline
- ✅ Simple to share

**Cons:**
- ❌ Manual updates (re-run script each time)
- ❌ Everyone needs to re-download for new photos

**Setup:**
1. Run `run_organizer.bat` (or `python organize_photos.py`)
2. Copy your photos to the same folder as the HTML
3. Open `beer-zoom-gallery.html` in browser
4. Share the folder via Dropbox/Drive/zip file

---

### **Option B: Live Website** (Recommended!)
**Use if:** You want a permanent URL that auto-updates

**Pros:**
- ✅ Auto-updates every 30 seconds
- ✅ Permanent URL to share
- ✅ Friends see new photos immediately
- ✅ No manual re-sharing

**Cons:**
- ❌ Requires web hosting (but free options available!)
- ❌ Initial setup takes 10-20 minutes

**Setup:**
1. Test locally: Run `start_server.bat` → visit `http://localhost:5000`
2. Deploy online: Follow `DEPLOYMENT_GUIDE.md` (recommended: PythonAnywhere or Railway)
3. Share your permanent URL with friends
4. Add photos → they appear automatically!

---

## 🚀 Quick Start Guide

### **First Time Setup:**

1. **Put your photos** in: `C:\Users\matto\Pictures\Screenshots\BeerZoom`

2. **Choose your version:**

   **For Static HTML:**
   ```bash
   # Double-click: run_organizer.bat
   # Or run: python organize_photos.py
   # Then open beer-zoom-gallery.html
   ```

   **For Live Website (Local Testing):**
   ```bash
   # Double-click: start_server.bat
   # Or run: python app.py
   # Then visit: http://localhost:5000
   ```

3. **Deploy online** (if using live version):
   - See `DEPLOYMENT_GUIDE.md` for detailed instructions
   - Recommended: PythonAnywhere (free, easy)

---

## 📂 Folder Structure

```
beer-zoom-gallery/
├── app.py                      # Flask web server
├── templates/
│   └── gallery.html           # Dynamic HTML template
├── beer-zoom-gallery.html     # Static HTML version
├── organize_photos.py         # Photo organizer script
├── requirements.txt           # Python dependencies
├── start_server.bat           # Windows server launcher
├── run_organizer.bat          # Windows script runner
├── README.md                  # This file
└── DEPLOYMENT_GUIDE.md        # Hosting instructions
```

---

## 🎨 Customizing Monthly Themes

### **Static HTML:**
Open `beer-zoom-gallery.html` in text editor → find `monthsData` → edit `theme:` lines

### **Live Website:**
Open `app.py` → find `DEFAULT_THEMES` dictionary → edit month themes

Example:
```python
DEFAULT_THEMES = {
    "January": "New Year, New Beers",
    "February": "Your Custom Theme Here",
    ...
}
```

---

## 📸 Adding New Photos

### **Static HTML:**
1. Add photos to BeerZoom folder
2. Run `run_organizer.bat`
3. Re-share the HTML file

### **Live Website:**
1. Add photos to BeerZoom folder (if local)
2. Or upload to hosting service
3. Photos appear automatically in ~30 seconds!

---

## 🌐 Hosting Recommendations

| Service | Cost | Setup Time | Best For |
|---------|------|------------|----------|
| **PythonAnywhere** | Free | 15 min | First time hosting |
| **Railway** | Free tier | 10 min | Modern, GitHub sync |
| **Render** | Free tier | 10 min | Simple & reliable |
| **DigitalOcean** | $5/month | 30 min | Full control |

See `DEPLOYMENT_GUIDE.md` for detailed instructions!

---

## 💡 Features

### Current Features:
- ✅ Beer-themed design (amber, gold, barrel colors)
- ✅ Vintage brewery aesthetics
- ✅ Photos sorted by date (newest first)
- ✅ Custom monthly themes
- ✅ Responsive (works on phones/tablets)
- ✅ Hover effects and animations
- ✅ Auto-refresh (live version only)

### Potential Additions (in DEPLOYMENT_GUIDE.md):
- Upload photos through the website
- Password protection
- Comments on photos
- Download buttons
- Social sharing

---

## 🔧 Requirements

- **Python 3.6+** (for running scripts/server)
- **Flask** (for live version only)
- **Modern web browser** (Chrome, Firefox, Safari, Edge)

---

## 📝 File Descriptions

### Core Files:
- **app.py** - The Flask web application that serves photos dynamically
- **templates/gallery.html** - HTML template with Jinja2 variables for dynamic content
- **beer-zoom-gallery.html** - Standalone static HTML (no server needed)

### Helper Files:
- **organize_photos.py** - Scans photos, reads dates, generates static HTML
- **requirements.txt** - Python package dependencies
- **start_server.bat** - One-click server starter for Windows
- **run_organizer.bat** - One-click photo organizer for Windows

### Documentation:
- **README.md** - This overview file
- **DEPLOYMENT_GUIDE.md** - Step-by-step hosting instructions

---

## 🆘 Troubleshooting

**Python not found:**
- Install from [python.org](https://www.python.org/downloads/)

**Flask not installed:**
- Run: `pip install -r requirements.txt`

**Photos not showing:**
- Verify folder path matches your system
- Ensure photos and HTML are in same folder (static version)

**Server won't start:**
- Check if port 5000 is already in use
- Try: `python app.py` manually to see errors

**Auto-refresh not working:**
- Check browser console (F12) for errors
- Verify server is running
- Check network connection

---

## 🎉 You're All Set!

Choose your version:
- **Static HTML**: Great for quick sharing, no hosting needed
- **Live Website**: Best user experience, auto-updates, professional

Either way, your beer memories will look awesome! 🍻

---

## 📞 Need Help?

1. Check `DEPLOYMENT_GUIDE.md` for hosting questions
2. Check browser console (F12) for errors
3. Check server logs (if using live version)

---

🍺 **Cheers to great times with great friends!** 🍺
