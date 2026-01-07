# 🍺 Beer Zoom Gallery - Live Website Deployment Guide

Transform your photo gallery into a **live website** that automatically updates when you add new photos!

## 🌟 Key Features of the Live Version

✅ **Auto-updates** - New photos appear automatically (checks every 30 seconds)
✅ **No manual HTML editing** - Just drop photos in the folder
✅ **Live for everyone** - Friends see updates immediately
✅ **Manual refresh button** - Force reload to check for new photos
✅ **Professional hosting** - Runs on a real web server

---

## 🚀 Deployment Options

### **Option 1: Run Locally on Your PC (Quick Test)**

**Best for:** Testing before deploying publicly

1. Install Flask:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the server:
   ```bash
   python app.py
   ```

3. Open in browser: `http://localhost:5000`

4. Share on your local network:
   - Find your PC's IP address (run `ipconfig` on Windows)
   - Friends on same WiFi can visit: `http://YOUR-IP:5000`

**Pros:** Free, immediate
**Cons:** Only works when your PC is on, only accessible on local network

---

### **Option 2: PythonAnywhere (FREE Hosting)**

**Best for:** Free, permanent hosting with minimal setup

#### Steps:

1. **Sign up** at [pythonanywhere.com](https://www.pythonanywhere.com) (Free account)

2. **Upload files:**
   - Go to "Files" tab
   - Upload `app.py`, `requirements.txt`, and the `templates` folder
   - Create a `photos` folder and upload your BeerZoom images

3. **Set up web app:**
   - Go to "Web" tab → "Add a new web app"
   - Choose "Flask"
   - Choose Python 3.10
   - Set working directory to where you uploaded files

4. **Install requirements:**
   - Go to "Consoles" tab
   - Open a Bash console
   - Run: `pip install -r requirements.txt`

5. **Configure paths:**
   - Edit `app.py` to point to your photos folder on PythonAnywhere:
   ```python
   PHOTOS_FOLDER = Path("/home/yourusername/photos")
   ```

6. **Reload web app** in the Web tab

Your site will be live at: `https://yourusername.pythonanywhere.com`

**To update photos:** Upload new images via the Files tab. They'll appear within 30 seconds!

**Pros:** Free, reliable, easy
**Cons:** 100MB storage on free tier, ads on free plan

---

### **Option 3: Railway.app (Modern Cloud Hosting)**

**Best for:** Professional deployment with GitHub integration

#### Steps:

1. **Create a GitHub repository:**
   - Create a new repo on GitHub
   - Upload all files (`app.py`, `requirements.txt`, `templates/`)
   - Add your photos to a `photos/` folder

2. **Sign up at [railway.app](https://railway.app)**

3. **Deploy:**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository
   - Railway will auto-detect Flask and deploy!

4. **Configure:**
   - Update `app.py` to read from `/app/photos` (Railway's file path)
   - Set environment variable: `PORT=8080`

5. **Add photos later:**
   - Push to GitHub → automatic deployment
   - Or use Railway's volume storage for persistent files

Your site will be live at a Railway URL (e.g., `yourapp.up.railway.app`)

**Pros:** Free tier available, professional, GitHub sync
**Cons:** Free tier has limited hours per month

---

### **Option 4: Render.com (Simple & Free)**

**Best for:** Easy deployment with good free tier

#### Steps:

1. **Create GitHub repo** with your files

2. **Sign up at [render.com](https://render.com)**

3. **Create Web Service:**
   - Click "New +" → "Web Service"
   - Connect your GitHub repo
   - Settings:
     - **Build Command:** `pip install -r requirements.txt`
     - **Start Command:** `python app.py`

4. **Add photo storage:**
   - Render offers persistent disks
   - Mount at `/mnt/photos`
   - Update `app.py` path to `/mnt/photos`

5. **Upload photos:**
   - Use Render's shell or SFTP to upload photos

Your site will be live at: `https://yourapp.onrender.com`

**Pros:** Good free tier, reliable
**Cons:** Spins down after inactivity (takes ~30s to wake)

---

### **Option 5: DigitalOcean App Platform**

**Best for:** If you want more control and don't mind paying a bit

- $5/month for basic plan
- Full Linux server
- SSH access to upload photos directly
- Most reliable option

---

## 📸 Adding Photos After Deployment

### PythonAnywhere:
- Upload via Files tab → appears in 30 seconds

### Railway/Render/GitHub-based:
- **Option A:** Push to GitHub (automatic deploy)
- **Option B:** Use cloud storage (Dropbox/Google Drive API)
- **Option C:** Build an upload page (see Advanced section)

---

## 🔧 Advanced: Add Photo Upload Feature

Want to upload photos through the website itself? Add this to `app.py`:

```python
from flask import request, redirect
from werkzeug.utils import secure_filename

@app.route('/upload', methods=['GET', 'POST'])
def upload_photo():
    if request.method == 'POST':
        if 'photo' not in request.files:
            return 'No file uploaded'
        
        file = request.files['photo']
        if file.filename:
            filename = secure_filename(file.filename)
            file.save(PHOTOS_FOLDER / filename)
            return redirect('/')
    
    return '''
    <html><body>
    <h1>Upload Photo</h1>
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="photo" accept="image/*">
        <button type="submit">Upload</button>
    </form>
    </body></html>
    '''
```

**Security note:** Add authentication for production use!

---

## 🔒 Optional: Add Password Protection

To protect your gallery, add this to `app.py`:

```python
from functools import wraps
from flask import request, Response

def check_auth(username, password):
    return username == 'beerfriends' and password == 'yourpassword'

def authenticate():
    return Response('Login required', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

# Add @requires_auth before @app.route('/')
@app.route('/')
@requires_auth
def index():
    ...
```

---

## 📊 Comparison Table

| Option | Cost | Setup Time | Auto-updates | Best For |
|--------|------|------------|--------------|----------|
| **Local PC** | Free | 5 min | Yes | Testing only |
| **PythonAnywhere** | Free | 15 min | Yes | Best free option |
| **Railway** | Free tier | 10 min | Yes | Modern deployment |
| **Render** | Free tier | 10 min | Yes | Simple & reliable |
| **DigitalOcean** | $5/mo | 30 min | Yes | Full control |

---

## 💡 My Recommendation

**For you (Matt):** Start with **PythonAnywhere** (free) or **Railway** (modern)

Both give you:
- ✅ Live URL your friends can visit
- ✅ Photos update automatically
- ✅ No need to keep your PC running
- ✅ Easy photo uploads

---

## 🆘 Troubleshooting

**Photos not showing?**
- Check the `PHOTOS_FOLDER` path in `app.py`
- Ensure photos are in the correct folder on the server
- Check file permissions

**Site not loading?**
- Check server logs (each platform has a logs viewer)
- Verify `requirements.txt` installed correctly
- Confirm Flask is running on correct port

**Auto-refresh not working?**
- Open browser console (F12) to see errors
- Check if API endpoint `/api/photos` is accessible
- Verify the gallery is checking every 30 seconds

---

## 🎉 That's It!

Once deployed, your friends can:
1. Visit your permanent URL
2. See all photos organized by month
3. Auto-refresh to see new photos as you add them
4. No downloads or manual files needed!

🍺 Cheers to automated beer memories! 🍺
