# ✅ Railway Deployment Checklist

Quick reference for deploying Beer Zoom Gallery to Railway.

---

## 📝 Pre-Deployment Checklist

- [ ] GitHub repo created: https://github.com/mfish324/Beer_Zoom.git
- [ ] All files committed and pushed to GitHub
- [ ] Railway account created at [railway.app](https://railway.app)
- [ ] Cloudinary account created at [cloudinary.com](https://cloudinary.com)

---

## 🚀 Deployment Steps

### 1️⃣ Setup Cloudinary (5 minutes)

- [ ] Sign up at cloudinary.com
- [ ] Go to Dashboard → copy your **CLOUDINARY_URL**
  ```
  Format: cloudinary://123456:abc@cloud-name
  ```
- [ ] Save this URL somewhere safe

### 2️⃣ Upload Photos to Cloudinary (5 minutes)

**Option A - Via Dashboard:**
- [ ] Go to Media Library
- [ ] Click Upload
- [ ] Create folder: `beer_zoom`
- [ ] Select and upload all photos
- [ ] Wait for uploads to complete

**Option B - Via Upload Script:**
- [ ] Set environment variable:
  ```bash
  set CLOUDINARY_URL=cloudinary://your-url
  ```
- [ ] Run: `upload_photos.bat` (or `python upload_to_cloudinary.py`)
- [ ] Verify uploads in Cloudinary Media Library

### 3️⃣ Deploy to Railway (10 minutes)

- [ ] Go to [railway.app](https://railway.app)
- [ ] Click **Login with GitHub**
- [ ] Click **New Project**
- [ ] Choose **Deploy from GitHub repo**
- [ ] Select: `mfish324/Beer_Zoom`
- [ ] Wait for initial build (~2-3 min)

### 4️⃣ Configure Environment Variables

- [ ] Click on your service in Railway
- [ ] Go to **Variables** tab
- [ ] Click **+ New Variable**
- [ ] Add:
  ```
  CLOUDINARY_URL=cloudinary://your-url-here
  ```
- [ ] Railway will auto-redeploy (~2 min)

### 5️⃣ Get Your Live URL

- [ ] Go to **Settings** tab
- [ ] Scroll to **Domains** section
- [ ] Click **Generate Domain**
- [ ] Copy your URL: `https://your-app.up.railway.app`
- [ ] Test it in your browser!

### 6️⃣ Share with Friends

- [ ] Send them your Railway URL
- [ ] Tell them it auto-updates every 30 seconds
- [ ] They can bookmark it!

---

## 🎉 You're Live!

Your gallery is now:
- ✅ Live on the internet
- ✅ Auto-updating every 30 seconds
- ✅ Easy to add new photos
- ✅ Automatically deploys from GitHub

---

## 📸 Adding New Photos Later

### Via Cloudinary Dashboard (Easiest):
1. Log into cloudinary.com
2. Go to Media Library
3. Click Upload → Select photos
4. Photos appear in gallery within 30 seconds!

### Via Upload Script:
1. Add photos to: `C:\Users\matto\Pictures\Screenshots\BeerZoom`
2. Run: `upload_photos.bat`
3. Photos sync to Cloudinary
4. Appear in gallery within 30 seconds!

---

## 🔄 Updating Code

When you make changes:
1. Edit files locally
2. `git add .`
3. `git commit -m "Your message"`
4. `git push`
5. Railway auto-deploys!

---

## 🆘 Troubleshooting

**Site not loading:**
- Check Railway → Deployments → View logs
- Verify CLOUDINARY_URL is set in Variables tab

**Photos not showing:**
- Check Cloudinary Media Library - are photos there?
- Make sure photos are in `beer_zoom` folder
- Check browser console (F12) for errors

**Upload script fails:**
- Verify CLOUDINARY_URL is set: `echo %CLOUDINARY_URL%`
- Install cloudinary: `pip install cloudinary`
- Check photo folder exists

---

## 📞 Need Help?

- Railway docs: [docs.railway.app](https://docs.railway.app)
- Cloudinary docs: [cloudinary.com/documentation](https://cloudinary.com/documentation)
- Full guide: See `RAILWAY_GUIDE.md`

---

## 🎯 Next Steps

- [ ] Customize monthly themes in `app.py`
- [ ] Consider adding password protection
- [ ] Set up custom domain (optional)
- [ ] Add more photos regularly!

🍺 **Enjoy your automated beer gallery!** 🍺
