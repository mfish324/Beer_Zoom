# 🚂 Railway Deployment Guide - Beer Zoom Gallery

Complete step-by-step guide to deploy your Beer Zoom Gallery on Railway with photo storage via Cloudinary.

---

## 🎯 What You'll Get

- ✅ Live website with a permanent URL
- ✅ Auto-updates when you add photos
- ✅ Automatic deployments from GitHub
- ✅ Easy photo uploads via Cloudinary dashboard
- ✅ Free tier with generous limits

---

## 📋 Prerequisites

1. ✅ GitHub account (you have: https://github.com/mfish324/Beer_Zoom.git)
2. ⬜ Railway account ([railway.app](https://railway.app))
3. ⬜ Cloudinary account ([cloudinary.com](https://cloudinary.com)) - for photos

---

## 🚀 Part 1: Setup Cloudinary (Photo Storage)

**Why Cloudinary?**
Railway's file system is temporary - files reset on each deploy. Cloudinary gives you permanent photo storage with easy uploads!

### Step 1: Create Cloudinary Account

1. Go to [cloudinary.com](https://cloudinary.com)
2. Click **Sign Up Free**
3. Complete registration
4. You get **25GB free storage** + 25k transformations/month

### Step 2: Get Your Cloudinary URL

1. Log into Cloudinary dashboard
2. Go to **Dashboard** (home page)
3. Look for **API Environment variable**
4. Copy the entire string that looks like:
   ```
   CLOUDINARY_URL=cloudinary://123456789:abcdefg@your-cloud-name
   ```
5. **Save this!** You'll need it for Railway

### Step 3: Upload Your First Photos

1. In Cloudinary dashboard, go to **Media Library**
2. Click **Upload** button (top right)
3. Select all your BeerZoom photos
4. Optional: Create a folder called `beer_zoom` to organize them
5. Click **Upload**
6. Done! Photos are now in the cloud

---

## 🚂 Part 2: Deploy to Railway

### Step 1: Create Railway Account

1. Go to [railway.app](https://railway.app)
2. Click **Login** → **Login with GitHub**
3. Authorize Railway to access your GitHub

### Step 2: Create New Project

1. Click **New Project**
2. Select **Deploy from GitHub repo**
3. Choose your repository: `mfish324/Beer_Zoom`
4. Railway will detect it's a Python app and start building!

### Step 3: Configure Environment Variables

1. In your Railway project, click on your service
2. Go to **Variables** tab
3. Click **+ New Variable**
4. Add this variable:
   ```
   Name: CLOUDINARY_URL
   Value: cloudinary://123456789:abcdefg@your-cloud-name
   ```
   (Paste the URL you copied from Cloudinary)
5. Railway will automatically redeploy

### Step 4: Wait for Deployment

1. Go to **Deployments** tab
2. Watch the build logs
3. Wait for "✓ Build successful"
4. You'll see "✓ Deployed" when ready (takes ~2-3 minutes)

### Step 5: Get Your URL

1. Go to **Settings** tab
2. Scroll to **Domains**
3. Click **Generate Domain**
4. Your gallery will be live at: `your-app-name.up.railway.app`
5. **Share this URL with friends!** 🍺

---

## 📸 Part 3: Adding New Photos

You have two options for adding photos:

### **Option A: Upload Directly to Cloudinary** ⭐ Recommended

**Best for:** Quick updates, uploading from anywhere

1. Log into [cloudinary.com](https://cloudinary.com)
2. Go to **Media Library**
3. Click **Upload**
4. Select new photos
5. Done! Photos appear in gallery within 30 seconds

**Pros:**
- ✅ Upload from anywhere (phone, computer)
- ✅ Instant
- ✅ No command line needed

---

### **Option B: Auto-Upload Script**

**Best for:** Bulk uploads from your PC

I created a script that automatically uploads photos from your BeerZoom folder to Cloudinary.

1. **Set your Cloudinary URL:**
   ```bash
   # Windows:
   set CLOUDINARY_URL=cloudinary://your-url-here
   
   # Mac/Linux:
   export CLOUDINARY_URL=cloudinary://your-url-here
   ```

2. **Run the upload script:**
   ```bash
   python upload_to_cloudinary.py
   ```

3. The script will:
   - ✅ Check what's already uploaded
   - ✅ Only upload NEW photos (no duplicates)
   - ✅ Show progress for each photo
   - ✅ Photos appear in gallery within 30 seconds

**Example output:**
```
📁 Scanning: C:\Users\matto\Pictures\Screenshots\BeerZoom
☁️  Checking Cloudinary for existing photos...
   Found 15 photos already uploaded

📤 Uploading 3 new photos...
   Uploading: meeting-dec-2024.jpg... ✅
   Uploading: meeting-nov-2024.jpg... ✅
   Uploading: meeting-oct-2024.jpg... ✅

==================================================
✅ Successfully uploaded: 3
==================================================

🍺 Photos will appear in your gallery within 30 seconds!
```

---

## 🔄 Updating Your Code

When you make changes to your code:

1. **Commit changes to GitHub:**
   ```bash
   git add .
   git commit -m "Update feature X"
   git push
   ```

2. **Railway auto-deploys!**
   - Railway detects the push
   - Automatically rebuilds and deploys
   - Takes ~2-3 minutes
   - No manual action needed!

---

## 🎨 Customizing Monthly Themes

1. Open `app.py` in your code editor
2. Find the `DEFAULT_THEMES` dictionary (around line 25)
3. Edit the theme for any month:
   ```python
   DEFAULT_THEMES = {
       "January": "New Year, New Beers",
       "December": "Holiday Ales & Festivities",  # ← Edit this!
       ...
   }
   ```
4. Save, commit, and push to GitHub
5. Railway auto-deploys with your changes!

---

## 💰 Railway Pricing

**Free Tier:**
- $5 free credit per month
- ~500 hours of runtime (enough for 24/7 hosting)
- No credit card required initially

**After Free Tier:**
- Pay-as-you-go: ~$5-10/month for this app
- Only charged for what you use

**Cloudinary is always free** for your usage (25GB storage)

---

## 🔧 Troubleshooting

### **Site not loading**

1. Check Railway logs:
   - Go to **Deployments** → Click latest deployment
   - Look for errors in logs
   
2. Common issues:
   - Missing `CLOUDINARY_URL` variable
   - Port configuration (should auto-detect)

### **Photos not showing**

1. Verify Cloudinary URL is set correctly:
   - Go to **Variables** tab in Railway
   - Check `CLOUDINARY_URL` is there
   
2. Check Cloudinary has your photos:
   - Log into Cloudinary → Media Library
   - Verify photos are uploaded

3. Check browser console:
   - Press F12 in browser
   - Look for errors in Console tab

### **Auto-refresh not working**

- This is normal! The app checks every 30 seconds
- Click the **Refresh Gallery** button for instant update
- Or refresh your browser (F5)

### **Upload script errors**

```bash
# Install Cloudinary package:
pip install cloudinary

# Make sure CLOUDINARY_URL is set:
echo %CLOUDINARY_URL%  # Windows
echo $CLOUDINARY_URL   # Mac/Linux
```

---

## 📊 Monitoring Your App

**Railway Dashboard:**
- View deployments: See build logs and errors
- Check metrics: CPU, memory, network usage
- View logs: Real-time app logs

**Cloudinary Dashboard:**
- Media Library: See all uploaded photos
- Usage: Check storage and bandwidth
- Transformations: Monitor API calls

---

## 🚀 Next Steps

### **Immediate:**
1. ✅ Deploy to Railway (follow Part 2 above)
2. ✅ Upload photos to Cloudinary (Part 3)
3. ✅ Share your Railway URL with friends!

### **Optional Enhancements:**

**Add Password Protection:**
- Keep the gallery private
- I can help you add this!

**Custom Domain:**
- Use your own domain (e.g., `beerzoom.com`)
- Configure in Railway Settings → Domains

**Photo Upload Page:**
- Let friends upload photos through website
- I can add this feature!

**Comments on Photos:**
- Add text comments to each photo
- More interactive experience

---

## 📞 Common Questions

**Q: Can I still test locally?**
A: Yes! Just run `python app.py` and it uses your local folder

**Q: How do I revert to a previous version?**
A: Railway keeps deployment history - click any old deployment to redeploy

**Q: Can I use a different photo service?**
A: Yes, but Cloudinary is easiest. Others include AWS S3, Google Cloud Storage

**Q: What if I run out of Railway credits?**
A: Add a credit card for pay-as-you-go, or use PythonAnywhere (always free)

**Q: How many photos can I have?**
A: Cloudinary free tier: ~5,000-10,000 photos (25GB total)

---

## 🎉 You're All Set!

Your Beer Zoom Gallery is now:
- ✅ Live on the internet
- ✅ Auto-updating
- ✅ Easy to manage
- ✅ Free (within limits)

**Your friends can now visit your Railway URL anytime to see the latest photos!**

Share the link: `https://your-app-name.up.railway.app`

🍺 **Cheers to automated memories!** 🍺

---

## 📚 Quick Reference

**Upload new photos:**
1. Go to cloudinary.com → Media Library
2. Click Upload → Select photos
3. Done!

**Update code:**
1. Edit files locally
2. `git commit` and `git push`
3. Railway auto-deploys

**Check status:**
- Railway dashboard → Deployments
- Your site URL

**Get help:**
- Railway docs: docs.railway.app
- Cloudinary docs: cloudinary.com/documentation
