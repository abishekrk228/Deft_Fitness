import easyocr
import cv2
import numpy as np

def fix_image():
    print("Loading easyocr...")
    reader = easyocr.Reader(['en'])
    img = cv2.imread('public/membership/page_1.1.png')
    
    print("Reading text...")
    results = reader.readtext(img)
    
    box_30 = None
    box_00 = None
    
    for (bbox, text, prob) in results:
        print(f"Detected: {text} at {bbox}")
        if "10.30" in text:
            box_30 = bbox
        if "6.00" in text or "7.00" in text:
            # wait, I just need the '00' part, but easyocr might return the whole '6.00 PM'
            pass

fix_image()
