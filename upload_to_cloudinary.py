"""
Auto-upload photos from local folder to Cloudinary
Run this script whenever you want to sync new photos
"""

import cloudinary
import cloudinary.uploader
from pathlib import Path
import os

# CONFIGURATION
LOCAL_PHOTOS_FOLDER = r"C:\Users\matto\Pictures\Screenshots\BeerZoom"

# Cloudinary will be configured from CLOUDINARY_URL environment variable
# Set it in your environment or in this script:
# os.environ['CLOUDINARY_URL'] = 'cloudinary://your_url_here'

def is_image(filename):
    """Check if file is an image"""
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']
    return any(filename.lower().endswith(ext) for ext in image_extensions)

def get_uploaded_images():
    """Get list of images already uploaded to Cloudinary"""
    try:
        result = cloudinary.api.resources(type="upload", max_results=500)
        return set(resource['public_id'] for resource in result.get('resources', []))
    except Exception as e:
        print(f"Error fetching Cloudinary images: {e}")
        return set()

def upload_new_photos():
    """Upload photos that aren't already on Cloudinary"""
    photos_folder = Path(LOCAL_PHOTOS_FOLDER)
    
    if not photos_folder.exists():
        print(f"❌ Error: Folder not found: {photos_folder}")
        return
    
    print(f"📁 Scanning: {photos_folder}")
    print(f"☁️  Checking Cloudinary for existing photos...")
    
    # Get existing photos on Cloudinary
    existing_photos = get_uploaded_images()
    print(f"   Found {len(existing_photos)} photos already uploaded")
    
    # Find new photos to upload
    new_photos = []
    for filepath in photos_folder.iterdir():
        if filepath.is_file() and is_image(filepath.name):
            # Use filename without extension as public_id
            public_id = filepath.stem
            if public_id not in existing_photos:
                new_photos.append(filepath)
    
    if not new_photos:
        print("✅ All photos are already uploaded!")
        return
    
    print(f"\n📤 Uploading {len(new_photos)} new photos...")
    
    # Upload new photos
    uploaded = 0
    failed = 0
    
    for filepath in new_photos:
        try:
            print(f"   Uploading: {filepath.name}...", end=" ")
            result = cloudinary.uploader.upload(
                str(filepath),
                public_id=filepath.stem,
                folder="beer_zoom"
            )
            print("✅")
            uploaded += 1
        except Exception as e:
            print(f"❌ Error: {e}")
            failed += 1
    
    print(f"\n{'='*50}")
    print(f"✅ Successfully uploaded: {uploaded}")
    if failed > 0:
        print(f"❌ Failed: {failed}")
    print(f"{'='*50}")
    print(f"\n🍺 Photos will appear in your gallery within 30 seconds!")

def main():
    print("="*50)
    print("🍺 Beer Zoom Gallery - Cloudinary Uploader")
    print("="*50)
    print()
    
    # Check if Cloudinary is configured
    if not os.environ.get('CLOUDINARY_URL'):
        print("❌ Error: CLOUDINARY_URL not set!")
        print("\nPlease set your Cloudinary URL:")
        print("  Windows: set CLOUDINARY_URL=cloudinary://...")
        print("  Mac/Linux: export CLOUDINARY_URL=cloudinary://...")
        print("\nOr add it to the script at line 12")
        return
    
    upload_new_photos()

if __name__ == "__main__":
    main()
