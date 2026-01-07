import os
from datetime import datetime
from pathlib import Path
import json

# CONFIGURATION - EDIT THESE PATHS
SCREENSHOTS_FOLDER = r"C:\Users\matto\Pictures\Screenshots\BeerZoom"
OUTPUT_HTML = r"beer-zoom-gallery.html"

# Month themes - you can customize these later in the HTML file
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

def get_file_date(filepath):
    """Get the creation or modification date of a file"""
    try:
        # Try to get creation time (works on Windows)
        timestamp = os.path.getctime(filepath)
    except:
        # Fall back to modification time
        timestamp = os.path.getmtime(filepath)
    return datetime.fromtimestamp(timestamp)

def is_image(filename):
    """Check if file is an image"""
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']
    return any(filename.lower().endswith(ext) for ext in image_extensions)

def organize_photos_by_month(screenshots_folder):
    """Scan folder and organize photos by month"""
    photos_by_month = {}
    
    # Scan the folder
    for filename in os.listdir(screenshots_folder):
        filepath = os.path.join(screenshots_folder, filename)
        
        # Skip if not a file or not an image
        if not os.path.isfile(filepath) or not is_image(filename):
            continue
        
        # Get the file date
        file_date = get_file_date(filepath)
        month_key = file_date.strftime("%Y-%m")
        month_display = file_date.strftime("%B %Y")
        
        # Initialize month if needed
        if month_key not in photos_by_month:
            photos_by_month[month_key] = {
                'display': month_display,
                'month_name': file_date.strftime("%B"),
                'photos': []
            }
        
        # Add photo to the month
        photos_by_month[month_key]['photos'].append({
            'filename': filename,
            'date': file_date,
            'label': file_date.strftime("%B %d, %Y")
        })
    
    # Sort months in reverse chronological order (newest first)
    sorted_months = sorted(photos_by_month.items(), key=lambda x: x[0], reverse=True)
    
    # Sort photos within each month by date (newest first)
    for month_key, month_data in sorted_months:
        month_data['photos'].sort(key=lambda x: x['date'], reverse=True)
    
    return sorted_months

def generate_html(photos_data, output_path):
    """Generate the HTML file with organized photos"""
    
    # Build the monthsData JavaScript array
    months_js = "const monthsData = [\n"
    
    for month_key, month_data in photos_data:
        month_name = month_data['month_name']
        theme = DEFAULT_THEMES.get(month_name, f"{month_name} Brew Session")
        
        months_js += f"    {{\n"
        months_js += f"        month: \"{month_data['display']}\",\n"
        months_js += f"        theme: \"{theme}\",\n"
        months_js += f"        photos: [\n"
        
        for photo in month_data['photos']:
            months_js += f"            {{ filename: \"{photo['filename']}\", label: \"{photo['label']}\" }},\n"
        
        months_js += f"        ]\n"
        months_js += f"    }},\n"
    
    months_js += "];\n"
    
    # Read the HTML template
    html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Monthly Brew Sessions 🍺</title>
    <link href="https://fonts.googleapis.com/css2?family=Alfa+Slab+One&family=Bebas+Neue&family=Outfit:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --beer-gold: #F4A623;
            --beer-amber: #D87B00;
            --beer-dark: #8B4513;
            --foam-white: #FFF8DC;
            --cream: #FFF5E1;
            --dark-wood: #3E2723;
            --barrel-oak: #5D4037;
            --hop-green: #7CB342;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Outfit', sans-serif;
            background: linear-gradient(135deg, var(--barrel-oak) 0%, var(--dark-wood) 100%);
            color: var(--foam-white);
            min-height: 100vh;
            position: relative;
            overflow-x: hidden;
        }

        /* Beer foam texture overlay */
        body::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-image: 
                radial-gradient(circle at 20% 30%, rgba(244, 166, 35, 0.08) 0%, transparent 50%),
                radial-gradient(circle at 80% 70%, rgba(216, 123, 0, 0.06) 0%, transparent 50%);
            pointer-events: none;
            z-index: 0;
        }

        /* Grain texture */
        body::after {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 400 400' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='0.03'/%3E%3C/svg%3E");
            pointer-events: none;
            z-index: 1;
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 40px 20px;
            position: relative;
            z-index: 2;
        }

        /* Header */
        header {
            text-align: center;
            margin-bottom: 60px;
            padding: 40px 20px;
            background: linear-gradient(180deg, rgba(244, 166, 35, 0.15) 0%, transparent 100%);
            border-radius: 20px;
            border: 3px solid var(--beer-gold);
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
            position: relative;
            animation: slideDown 0.8s ease-out;
        }

        @keyframes slideDown {
            from {
                opacity: 0;
                transform: translateY(-30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        h1 {
            font-family: 'Alfa Slab One', cursive;
            font-size: clamp(2.5rem, 8vw, 5rem);
            color: var(--beer-gold);
            text-shadow: 
                3px 3px 0 var(--beer-amber),
                6px 6px 0 var(--beer-dark),
                8px 8px 20px rgba(0, 0, 0, 0.8);
            letter-spacing: 2px;
            margin-bottom: 10px;
            line-height: 1.1;
        }

        .tagline {
            font-family: 'Bebas Neue', cursive;
            font-size: clamp(1.2rem, 3vw, 2rem);
            color: var(--foam-white);
            letter-spacing: 4px;
            text-transform: uppercase;
            opacity: 0.9;
        }

        .beer-mug {
            font-size: 3rem;
            display: inline-block;
            animation: cheers 2s ease-in-out infinite;
        }

        @keyframes cheers {
            0%, 100% { transform: rotate(0deg); }
            25% { transform: rotate(-15deg); }
            75% { transform: rotate(15deg); }
        }

        /* Month Section */
        .month-section {
            margin-bottom: 80px;
            opacity: 0;
            animation: fadeInUp 0.6s ease-out forwards;
            animation-delay: calc(var(--index) * 0.1s);
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .month-header {
            background: linear-gradient(135deg, var(--beer-amber) 0%, var(--beer-dark) 100%);
            padding: 30px 40px;
            border-radius: 15px 15px 0 0;
            border: 2px solid var(--beer-gold);
            border-bottom: none;
            position: relative;
            overflow: hidden;
        }

        .month-header::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255, 255, 255, 0.1) 0%, transparent 70%);
            animation: shimmer 3s ease-in-out infinite;
        }

        @keyframes shimmer {
            0%, 100% { transform: translate(-25%, -25%); }
            50% { transform: translate(0%, 0%); }
        }

        .month-title {
            font-family: 'Bebas Neue', cursive;
            font-size: 2.5rem;
            color: var(--foam-white);
            letter-spacing: 3px;
            margin-bottom: 10px;
            position: relative;
            z-index: 1;
        }

        .month-theme {
            font-family: 'Outfit', sans-serif;
            font-size: 1.2rem;
            color: var(--cream);
            font-weight: 300;
            font-style: italic;
            position: relative;
            z-index: 1;
        }

        .month-theme::before {
            content: '🍺';
            margin-right: 10px;
        }

        /* Photos Grid */
        .photos-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            padding: 40px;
            background: rgba(93, 64, 55, 0.3);
            border-radius: 0 0 15px 15px;
            border: 2px solid var(--beer-gold);
            border-top: none;
            backdrop-filter: blur(10px);
        }

        .photo-card {
            position: relative;
            overflow: hidden;
            border-radius: 12px;
            background: rgba(0, 0, 0, 0.5);
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            cursor: pointer;
        }

        .photo-card:hover {
            transform: translateY(-8px) scale(1.02);
            box-shadow: 0 15px 40px rgba(244, 166, 35, 0.3);
        }

        .photo-card img {
            width: 100%;
            height: 250px;
            object-fit: cover;
            display: block;
            transition: transform 0.4s ease;
        }

        .photo-card:hover img {
            transform: scale(1.1);
        }

        .photo-label {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            background: linear-gradient(to top, rgba(0, 0, 0, 0.9), transparent);
            padding: 15px;
            color: var(--foam-white);
            font-size: 0.9rem;
            transform: translateY(100%);
            transition: transform 0.3s ease;
        }

        .photo-card:hover .photo-label {
            transform: translateY(0);
        }

        .stats {
            background: rgba(139, 69, 19, 0.3);
            border: 2px solid var(--hop-green);
            border-radius: 15px;
            padding: 20px 30px;
            margin-bottom: 40px;
            backdrop-filter: blur(10px);
            text-align: center;
            font-family: 'Bebas Neue', cursive;
            font-size: 1.5rem;
            color: var(--beer-gold);
            letter-spacing: 2px;
        }

        /* Instructions Panel */
        .instructions {
            background: rgba(139, 69, 19, 0.3);
            border: 2px dashed var(--beer-gold);
            border-radius: 15px;
            padding: 30px;
            margin-top: 60px;
            backdrop-filter: blur(10px);
        }

        .instructions h2 {
            font-family: 'Bebas Neue', cursive;
            font-size: 2rem;
            color: var(--beer-gold);
            letter-spacing: 2px;
            margin-bottom: 20px;
        }

        .instructions ol, .instructions ul {
            margin-left: 30px;
            line-height: 1.8;
            color: var(--cream);
        }

        .instructions li {
            margin-bottom: 12px;
        }

        .instructions code {
            background: rgba(0, 0, 0, 0.5);
            padding: 2px 8px;
            border-radius: 4px;
            color: var(--beer-gold);
            font-family: 'Courier New', monospace;
        }

        /* Footer */
        footer {
            text-align: center;
            padding: 40px 20px;
            margin-top: 60px;
            color: var(--cream);
            font-size: 0.9rem;
            opacity: 0.7;
        }

        /* Responsive */
        @media (max-width: 768px) {
            .photos-grid {
                grid-template-columns: 1fr;
                padding: 20px;
            }
            
            h1 {
                font-size: 2.5rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🍻 MONTHLY BREW SESSIONS 🍻</h1>
            <p class="tagline">Zoom Meetings • Good Friends • Cold Beers</p>
        </header>

        <div class="stats">
            <span id="total-months">0</span> Months of Memories • 
            <span id="total-photos">0</span> Photos
        </div>

        <div id="gallery">
            <!-- Gallery will be populated by JavaScript -->
        </div>

        <div class="instructions">
            <h2>🍺 How to Edit Themes & Add More Photos</h2>
            <ol>
                <li><strong>Editing Themes:</strong> 
                    <ul>
                        <li>Open this HTML file in any text editor (Notepad, VS Code, etc.)</li>
                        <li>Find the <code>monthsData</code> array in the JavaScript section below</li>
                        <li>Change the <code>theme</code> text for any month</li>
                        <li>Save and refresh the page</li>
                    </ul>
                </li>
                <li><strong>Adding New Photos:</strong> 
                    <ul>
                        <li>Add new screenshots to: <code>''' + SCREENSHOTS_FOLDER + '''</code></li>
                        <li>Run the <code>organize_photos.py</code> script again</li>
                        <li>This will regenerate the HTML with all photos organized by date</li>
                    </ul>
                </li>
                <li><strong>Sharing:</strong> 
                    <ul>
                        <li>Copy this HTML file and all your screenshot images to the same folder</li>
                        <li>Share via Google Drive, Dropbox, or zip and email</li>
                        <li>Anyone can view by opening the HTML file in a browser</li>
                    </ul>
                </li>
            </ol>
        </div>

        <footer>
            🍺 Cheers to friendship and good times! 🍺<br>
            <small>Gallery auto-generated from your Screenshots folder</small>
        </footer>
    </div>

    <script>
        // ============================================
        // PHOTO DATA - Auto-generated from your Screenshots folder
        // You can edit the 'theme' for each month!
        // ============================================
        
        ''' + months_js + '''

        // ============================================
        // GALLERY RENDERING CODE (NO NEED TO EDIT)
        // ============================================
        
        function renderGallery() {
            const gallery = document.getElementById('gallery');
            gallery.innerHTML = '';
            
            let totalPhotos = 0;

            monthsData.forEach((monthData, index) => {
                totalPhotos += monthData.photos.length;
                
                const section = document.createElement('div');
                section.className = 'month-section';
                section.style.setProperty('--index', index);

                const header = document.createElement('div');
                header.className = 'month-header';
                header.innerHTML = `
                    <h2 class="month-title">${monthData.month}</h2>
                    <p class="month-theme">${monthData.theme}</p>
                `;

                const grid = document.createElement('div');
                grid.className = 'photos-grid';

                monthData.photos.forEach(photo => {
                    const card = document.createElement('div');
                    card.className = 'photo-card';
                    card.innerHTML = `
                        <img src="${photo.filename}" alt="${photo.label}" onerror="this.src='data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%22300%22 height=%22250%22%3E%3Crect fill=%22%23333%22 width=%22300%22 height=%22250%22/%3E%3Ctext x=%2250%25%22 y=%2250%25%22 dominant-baseline=%22middle%22 text-anchor=%22middle%22 fill=%22%23999%22 font-family=%22Arial%22 font-size=%2214%22%3E${photo.filename}%3C/text%3E%3Ctext x=%2250%25%22 y=%2260%25%22 dominant-baseline=%22middle%22 text-anchor=%22middle%22 fill=%22%23999%22 font-family=%22Arial%22 font-size=%2212%22%3ENot found%3C/text%3E%3C/svg%3E'">
                        <div class="photo-label">${photo.label}</div>
                    `;
                    grid.appendChild(card);
                });

                section.appendChild(header);
                section.appendChild(grid);
                gallery.appendChild(section);
            });
            
            // Update stats
            document.getElementById('total-months').textContent = monthsData.length;
            document.getElementById('total-photos').textContent = totalPhotos;
        }

        // Render gallery on page load
        renderGallery();
    </script>
</body>
</html>'''
    
    # Write the HTML file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"\n✅ HTML gallery generated successfully!")
    print(f"📁 Output: {output_path}")
    print(f"\nOpen {output_path} in your web browser to view your gallery!")

def main():
    print("🍺 Beer Zoom Gallery Photo Organizer")
    print("=" * 50)
    
    # Check if screenshots folder exists
    if not os.path.exists(SCREENSHOTS_FOLDER):
        print(f"❌ Error: Screenshots folder not found at:")
        print(f"   {SCREENSHOTS_FOLDER}")
        print("\nPlease edit the SCREENSHOTS_FOLDER path at the top of this script.")
        return
    
    print(f"📂 Scanning: {SCREENSHOTS_FOLDER}")
    
    # Organize photos by month
    photos_data = organize_photos_by_month(SCREENSHOTS_FOLDER)
    
    if not photos_data:
        print("❌ No image files found in the screenshots folder!")
        return
    
    # Print summary
    total_photos = sum(len(month['photos']) for _, month in photos_data)
    print(f"\n📸 Found {total_photos} photos across {len(photos_data)} months")
    print("\nMonths found (newest to oldest):")
    for month_key, month_data in photos_data:
        print(f"  • {month_data['display']}: {len(month_data['photos'])} photos")
    
    # Generate HTML
    print(f"\n🔨 Generating HTML gallery...")
    generate_html(photos_data, OUTPUT_HTML)
    
    print("\n" + "=" * 50)
    print("🎉 All done! Your beer gallery is ready to share!")
    print("\nNext steps:")
    print("1. Open 'beer-zoom-gallery.html' in your browser")
    print("2. Copy your screenshots to the same folder as the HTML")
    print("3. Edit themes directly in the HTML if desired")
    print("4. Share the folder with your friends!")

if __name__ == "__main__":
    main()
