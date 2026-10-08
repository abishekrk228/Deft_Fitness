import cv2
import numpy as np

img = cv2.imread('public/membership/page_1.1.png')

# The banner is at the bottom. Let's search the last 200 rows and rightmost 800 cols.
roi = img[-200:, -800:]

# find white text.
gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

# Find contours of the white text
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create an image to draw bounding boxes
boxes_img = roi.copy()
for i, c in enumerate(contours):
    x, y, w, h = cv2.boundingRect(c)
    cv2.rectangle(boxes_img, (x, y), (x+w, y+h), (0, 255, 0), 1)

cv2.imwrite('C:/Users/abish/.gemini/antigravity/brain/94bfdeb0-7e3f-45db-bb26-f6c8f9617fbb/scratch/boxes.png', boxes_img)
