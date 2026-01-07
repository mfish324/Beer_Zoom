# 🍺 Beer Zoom Gallery - Auto Photo Organizer

This tool automatically scans your Screenshots folder, reads the dates from each photo, and creates a beautiful beer-themed gallery organized by month!

## Quick Start

### Step 1: Run the Organizer

**Easy way (Windows):**
- Double-click `run_organizer.bat`

**Or run manually:**
```
python organize_photos.py
```

### Step 2: Copy Photos to HTML Folder

After running the script, you'll have a file called `beer-zoom-gallery.html`

**Important:** Copy all your screenshot images to the SAME FOLDER as the HTML file so they display correctly!

### Step 3: Open and View

Double-click `beer-zoom-gallery.html` to open it in your browser!

## How It Works

The script will:
1. ✅ Scan `C:\Users\matto\Pictures\Screenshots\BeerZoom`
2. ✅ Read the creation/modification date from each image file
3. ✅ Organize photos by month in reverse chronological order (newest first)
4. ✅ Auto-sort photos within each month (newest first)
5. ✅ Generate the HTML gallery with all photos included
6. ✅ Apply monthly themes (you can edit these later!)

## Editing Monthly Themes

Want to customize the theme for each month?

1. Open `beer-zoom-gallery.html` in any text editor (Notepad, VS Code, etc.)
2. Find the JavaScript section with `monthsData`
3. Change any `theme:` line to your preferred text
4. Save and refresh in your browser

Example:
```javascript
{
    month: "December 2024",
    theme: "Holiday Ales & Cheer",  // ← Change this!
    photos: [
        ...
    ]
},
```

## Adding More Photos Later

1. Add new screenshots to your Screenshots folder
2. Run `organize_photos.py` again (or double-click `run_organizer.bat`)
3. Copy any new images to the same folder as the HTML
4. Refresh your browser!

## Sharing with Friends

**Option 1: Google Drive / Dropbox**
- Upload the HTML file and ALL screenshots to a shared folder
- Share the folder link
- Friends can open the HTML file directly

**Option 2: Zip and Email**
- Put the HTML file and all screenshots in one folder
- Right-click → "Send to" → "Compressed (zipped) folder"
- Email or share the zip file

**Option 3: Web Hosting**
- Upload to any web host
- Perfect if you have your own website!

## Troubleshooting

**"No such file or directory" error:**
- Check that the path in `organize_photos.py` matches your Screenshots folder
- Edit line 6 in the Python script if your path is different

**Images not showing:**
- Make sure ALL screenshot files are in the same folder as the HTML file
- The script shows you which files it found - copy those specific files

**"Python not found" error:**
- Install Python from python.org
- Or just manually edit the HTML file (see instructions in the file)

## Requirements

- Python 3.6 or higher (no extra packages needed!)
- Windows, Mac, or Linux

---

🍺 **Cheers to good times and great friends!** 🍺
