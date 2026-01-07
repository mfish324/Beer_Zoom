"""
Beer Zoom Gallery - Dynamic Web Application
A Flask app that automatically shows new photos as they're added
Supports both local storage and Cloudinary cloud storage
"""

from flask import Flask, render_template, send_from_directory, jsonify
from pathlib import Path
from datetime import datetime, timedelta
import os

app = Flask(__name__)

# CONFIGURATION
# Check if Cloudinary is configured (for Railway/Render deployments)
USE_CLOUDINARY = os.environ.get('CLOUDINARY_URL') is not None

if USE_CLOUDINARY:
    import cloudinary
    import cloudinary.api
    print("🌥️  Using Cloudinary for photo storage")
else:
    # Local storage path - edit based on your system
    # - Local PC: r"C:\Users\matto\Pictures\Screenshots\BeerZoom"
    # - PythonAnywhere: Path("/home/yourusername/photos")
    PHOTOS_FOLDER = Path(os.environ.get('PHOTOS_FOLDER', r"C:\Users\matto\Pictures\Screenshots\BeerZoom"))
    app.config['PHOTOS_FOLDER'] = PHOTOS_FOLDER
    print(f"📁 Using local storage: {PHOTOS_FOLDER}")

# Month themes - you can edit these anytime
DEFAULT_THEMES = {
    "January": "New Year, New Beers",
    "February": "Valentine's Brews",
    "March": "Spring Ales Awakening",
    "April": "Hoppy Spring Sessions",
    "May": "May Flowers & Pale Ales",
    "June": "Summer Wheat Season",
    "July": "Independence Brews",
    "August": "Late Summer Lagers",
    "September": "Harvest Ale Celebration",
    "October": "Oktoberfest Extravaganza",
    "November": "Stout Season Begins",
    "December": "Holiday Ales & Cheer"
}

def is_image(filename):
    """Check if file is an image"""
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']
    return any(filename.lower().endswith(ext) for ext in image_extensions)

def get_file_date(filepath):
    """Get the creation or modification date of a file"""
    try:
        timestamp = os.path.getctime(filepath)
    except:
        timestamp = os.path.getmtime(filepath)
    return datetime.fromtimestamp(timestamp)

def get_cloudinary_date(resource):
    """Extract date from filename like Screenshot_2025-12-02_193707_xxx or estimate from number"""
    import re
    public_id = resource.get('public_id', '')

    # Try to extract date from filename pattern: Screenshot_YYYY-MM-DD_HHMMSS
    match = re.search(r'(\d{4}-\d{2}-\d{2})_(\d{6})', public_id)
    if match:
        date_str = match.group(1)
        time_str = match.group(2)
        try:
            return datetime.strptime(f"{date_str}_{time_str}", '%Y-%m-%d_%H%M%S')
        except:
            pass

    # For Screenshot_NNN format, estimate date based on number
    # Assume screenshots span from early 2025, with higher numbers being more recent
    num_match = re.search(r'Screenshot_(\d+)_', public_id)
    if num_match:
        num = int(num_match.group(1))
        # Spread numbers 1-150 across Jan 2025 to Nov 2025 (before dated photos start in Dec)
        # Each screenshot roughly 2 days apart
        base_date = datetime(2025, 1, 1)
        days_offset = min(num * 2, 330)  # Cap at ~Nov 2025
        return base_date + timedelta(days=days_offset)

    # Final fallback
    created_at = resource.get('created_at', '')
    try:
        return datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%SZ')
    except:
        return datetime.now()

def scan_photos_local():
    """Scan the local photos folder and organize by month"""
    photos_by_month = {}
    
    if not PHOTOS_FOLDER.exists():
        return []
    
    for filepath in PHOTOS_FOLDER.iterdir():
        if not filepath.is_file() or not is_image(filepath.name):
            continue
        
        file_date = get_file_date(filepath)
        month_key = file_date.strftime("%Y-%m")
        month_display = file_date.strftime("%B %Y")
        month_name = file_date.strftime("%B")
        
        if month_key not in photos_by_month:
            photos_by_month[month_key] = {
                'display': month_display,
                'month_name': month_name,
                'theme': DEFAULT_THEMES.get(month_name, f"{month_name} Brew Session"),
                'photos': []
            }
        
        photos_by_month[month_key]['photos'].append({
            'filename': filepath.name,
            'date': file_date,
            'label': file_date.strftime("%B %d, %Y"),
            'url': f'/photos/{filepath.name}'
        })
    
    # Sort months (newest first) and photos within each month
    sorted_months = sorted(photos_by_month.items(), key=lambda x: x[0], reverse=True)
    for month_key, month_data in sorted_months:
        month_data['photos'].sort(key=lambda x: x['date'], reverse=True)
    
    return sorted_months

def scan_photos_cloudinary():
    """Scan photos from Cloudinary and organize by month"""
    photos_by_month = {}
    
    try:
        # Get all images from Cloudinary (photos are in root folder)
        result = cloudinary.api.resources(
            type="upload",
            max_results=500
        )
        
        for resource in result.get('resources', []):
            public_id = resource['public_id']
            # Skip sample images and other folders
            if public_id.startswith(('samples/', 'media/', 'cld-sample', 'main-sample')):
                continue

            file_date = get_cloudinary_date(resource)
            month_key = file_date.strftime("%Y-%m")
            month_display = file_date.strftime("%B %Y")
            month_name = file_date.strftime("%B")
            
            if month_key not in photos_by_month:
                photos_by_month[month_key] = {
                    'display': month_display,
                    'month_name': month_name,
                    'theme': DEFAULT_THEMES.get(month_name, f"{month_name} Brew Session"),
                    'photos': []
                }
            
            # Get filename from public_id
            filename = resource['public_id'].split('/')[-1]
            
            photos_by_month[month_key]['photos'].append({
                'filename': filename,
                'date': file_date,
                'label': file_date.strftime("%B %d, %Y"),
                'url': resource['secure_url']
            })
        
        # Sort months (newest first) and photos within each month
        sorted_months = sorted(photos_by_month.items(), key=lambda x: x[0], reverse=True)
        for month_key, month_data in sorted_months:
            month_data['photos'].sort(key=lambda x: x['date'], reverse=True)
        
        return sorted_months
        
    except Exception as e:
        print(f"Error scanning Cloudinary: {e}")
        return []

def scan_photos():
    """Scan photos from the appropriate source"""
    if USE_CLOUDINARY:
        return scan_photos_cloudinary()
    else:
        return scan_photos_local()

@app.route('/')
def index():
    """Main gallery page"""
    months_data = scan_photos()
    total_photos = sum(len(month['photos']) for _, month in months_data)
    return render_template('gallery.html', months_data=months_data, total_photos=total_photos)

@app.route('/api/photos')
def api_photos():
    """API endpoint to get current photos (for auto-refresh)"""
    months_data = scan_photos()
    result = []
    for month_key, month_data in months_data:
        result.append({
            'month': month_data['display'],
            'theme': month_data['theme'],
            'photos': month_data['photos']
        })
    return jsonify(result)

@app.route('/photos/<filename>')
def serve_photo(filename):
    """Serve individual photo files (local storage only)"""
    if USE_CLOUDINARY:
        # Photos are served directly from Cloudinary URLs
        return "Cloudinary photos use direct URLs", 404
    return send_from_directory(app.config['PHOTOS_FOLDER'], filename)

@app.route('/refresh')
def refresh():
    """Manual refresh endpoint"""
    months_data = scan_photos()
    total_photos = sum(len(month['photos']) for _, month in months_data)
    return jsonify({
        'status': 'success',
        'total_months': len(months_data),
        'total_photos': total_photos
    })

if __name__ == '__main__':
    # For local development
    print("🍺 Beer Zoom Gallery Server Starting...")
    if USE_CLOUDINARY:
        print(f"☁️  Photo storage: Cloudinary")
    else:
        print(f"📁 Photo storage: {PHOTOS_FOLDER}")
    print(f"🌐 Open your browser to: http://localhost:5000")
    print("Press Ctrl+C to stop the server")
    print()
    app.run(debug=True, host='0.0.0.0', port=5000)
