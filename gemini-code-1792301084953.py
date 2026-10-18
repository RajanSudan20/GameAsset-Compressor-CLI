import os
from PIL import Image

def optimize_texture(image_path, max_size=2048):
    # Step 1: Image Open Karo
    img = Image.open(image_path)
    width, height = img.size
    
    # Step 2: Check Karo Ki Resize Ki Zaroorat Hai Ya Nahi
    if width > max_size or height > max_size:
        img.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
        print(f"Resized: {image_path} -> {max_size}px")
        
    # Step 3: Optimized Format Mein Save Karo
    output_path = os.path.splitext(image_path)[0] + "_opt.webp"
    img.save(output_path, "WEBP", quality=85)
    print(f"Saved: {output_path}")

# Step 4: Folder Mein Har File Par Tool Chalao
def process_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                full_path = os.path.join(root, file)
                optimize_texture(full_path)

# Run The Tool
process_folder("./game_assets")