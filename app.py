"""
Beer Zoom Gallery - Dynamic Web Application
A Flask app that automatically shows new photos as they're added to the folder
"""

from flask import Flask, render_template, send_from_directory, jsonify
from pathlib import Path
from datetime import datetime
import os

app = Flask(__name__)

# CONFIGURATION
PHOTOS_FOLDER = Path(r"C:\Users\matto\Pictures\Screenshots\BeerZoom")
app.config['PHOTOS_FOLDER'] = PHOTOS_FOLDER

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

def scan_photos():
    """Scan the photos folder and organize by month"""
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
            'label': file_date.strftime("%B %d, %Y")
        })
    
    # Sort months (newest first) and photos within each month
    sorted_months = sorted(photos_by_month.items(), key=lambda x: x[0], reverse=True)
    for month_key, month_data in sorted_months:
        month_data['photos'].sort(key=lambda x: x['date'], reverse=True)
    
    return sorted_months

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
    """Serve individual photo files"""
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
    print(f"📁 Scanning: {PHOTOS_FOLDER}")
    print(f"🌐 Open your browser to: http://localhost:5000")
    print("Press Ctrl+C to stop the server")
    app.run(debug=True, host='0.0.0.0', port=5000)
