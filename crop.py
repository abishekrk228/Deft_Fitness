from PIL import Image

img = Image.open('public/membership/page_1.1.png')
w, h = img.size

# crop bottom right
crop = img.crop((w - 800, h - 200, w, h))
crop.save('C:/Users/abish/.gemini/antigravity/brain/94bfdeb0-7e3f-45db-bb26-f6c8f9617fbb/scratch/crop.png')
