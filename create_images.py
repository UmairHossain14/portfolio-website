#!/usr/bin/env python3
"""Create placeholder images for portfolio website"""
from PIL import Image, ImageDraw, ImageFont
import os

# Create images directory
os.makedirs('images', exist_ok=True)

def create_placeholder(filename, width, height, bg_color, text, text_color=(255, 255, 255)):
    """Create a placeholder image"""
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 48)
    except:
        font = ImageFont.load_default()
    
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    draw.text((x, y), text, fill=text_color, font=font)
    img.save(f'images/{filename}')
    print(f"✓ Created {filename}")

# Create images
create_placeholder('hero.jpg', 1920, 1080, (26, 26, 46), 'HERO BACKGROUND', (233, 69, 96))
create_placeholder('profile.jpg', 400, 400, (63, 81, 181), 'YOUR PHOTO', (255, 255, 255))
create_placeholder('project1.jpg', 600, 400, (33, 150, 243), 'Portfolio Website', (255, 255, 255))
create_placeholder('project2.jpg', 600, 400, (76, 175, 80), 'HTML/CSS Practice', (255, 255, 255))
create_placeholder('project3.jpg', 600, 400, (255, 152, 0), 'JavaScript Mini', (255, 255, 255))

print("\n✓ All placeholder images created successfully!")
