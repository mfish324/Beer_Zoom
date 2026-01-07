"""
Re-upload all photos to Cloudinary with original file dates preserved.
This will delete existing photos and re-upload them with date metadata.
"""

import cloudinary
import cloudinary.uploader
import cloudinary.api
from pathlib import Path
from datetime import datetime
import os

# CONFIGURATION
LOCAL_PHOTOS_FOLDER = r"C:\Users\matto\Pictures\Screenshots\BeerZoom"

# Set your Cloudinary URL here or via environment variable
# os.environ['CLOUDINARY_URL'] = 'cloudinary://...'

def is_image(filename):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']
    return any(filename.lower().endswith(ext) for ext in image_extensions)

def get_file_date(filepath):
    """Get the original file date"""
    try:
        timestamp = os.path.getctime(filepath)
    except:
        timestamp = os.path.getmtime(filepath)
    return datetime.fromtimestamp(timestamp)

def delete_existing_photos():
    """Delete all existing beer photos from Cloudinary"""
    print("🗑️  Deleting existing photos from Cloudinary...")
    try:
        result = cloudinary.api.resources(type="upload", max_results=500)
        to_delete = []
        for r in result.get('resources', []):
            pid = r['public_id']
            # Only delete Screenshot photos, not samples
            if pid.startswith('Screenshot') or pid.startswith('beer_zoom/'):
                to_delete.append(pid)

        if to_delete:
            # Delete in batches of 100
            for i in range(0, len(to_delete), 100):
                batch = to_delete[i:i+100]
                cloudinary.api.delete_resources(batch)
                print(f"   Deleted {len(batch)} photos...")

        print(f"   Total deleted: {len(to_delete)}")
        return len(to_delete)
    except Exception as e:
        print(f"Error deleting: {e}")
        return 0

def upload_all_photos():
    """Upload all photos with original dates"""
    photos_folder = Path(LOCAL_PHOTOS_FOLDER)

    if not photos_folder.exists():
        print(f"❌ Folder not found: {photos_folder}")
        return

    # Get all image files
    photos = [f for f in photos_folder.iterdir() if f.is_file() and is_image(f.name)]
    print(f"\n📤 Uploading {len(photos)} photos with original dates...")

    uploaded = 0
    failed = 0

    for filepath in sorted(photos):
        try:
            file_date = get_file_date(filepath)
            date_str = file_date.strftime("%Y-%m-%d %H:%M:%S")

            print(f"   {filepath.name} ({file_date.strftime('%b %d, %Y')})...", end=" ")

            cloudinary.uploader.upload(
                str(filepath),
                public_id=filepath.stem,
                folder="beer_zoom",
                context=f"original_date={date_str}",
                overwrite=True
            )
            print("✅")
            uploaded += 1
        except Exception as e:
            print(f"❌ {e}")
            failed += 1

    print(f"\n{'='*50}")
    print(f"✅ Uploaded: {uploaded}")
    if failed:
        print(f"❌ Failed: {failed}")
    print(f"{'='*50}")

def main():
    print("="*50)
    print("🍺 Beer Zoom - Re-upload with Original Dates")
    print("="*50)
    print()

    if not os.environ.get('CLOUDINARY_URL'):
        print("❌ CLOUDINARY_URL not set!")
        print("Set it with: set CLOUDINARY_URL=cloudinary://...")
        return

    print("⚠️  This will DELETE all existing photos and re-upload them.")
    confirm = input("Continue? (yes/no): ")

    if confirm.lower() != 'yes':
        print("Cancelled.")
        return

    delete_existing_photos()
    upload_all_photos()

    print("\n🍺 Done! Refresh your gallery to see photos with correct dates.")

if __name__ == "__main__":
    main()
