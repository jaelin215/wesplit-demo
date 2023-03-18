import cv2
import imutils
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from functions import orient_vertical, sharpen_edge, binarize, find_receipt_bounding_box, find_tilt_angle, adjust_tilt, crop, enhance_txt
import code2flow
import pytesseract

# Read raw image
raw_path = 'raw/faded2.JPG'
raw_img = cv2.imread(raw_path)

# View raw image
# raw_rgb = cv2.cvtColor(raw_img, cv2.COLOR_BGR2RGB)
# plt.imshow(raw_rgb)
# plt.show()


# Rotate
rotated = orient_vertical(raw_img)

# Detect edge
edged = sharpen_edge(rotated)
binary = binarize(edged, 100)
boxed, largest_cnt = find_receipt_bounding_box(binary, rotated)
boxed_rgb = cv2.cvtColor(boxed, cv2.COLOR_BGR2RGB)

# Adjust tilt
rect, angle = find_tilt_angle(largest_cnt)
tilted, delta = adjust_tilt(boxed, angle)
print(f"{round(delta,2)} degree adjusted towards right.")

# Crop
cropped = crop(tilted, largest_cnt)

# Enhance txt
enhanced = enhance_txt(cropped)
enhanced_rgb = cv2.cvtColor(enhanced, cv2.COLOR_BGR2RGB)
enhanced_path = 'preprocessed/enhanced.jpg'
plt.imsave(enhanced_path, enhanced_rgb)

# Run OCR
options_all = f"--psm 1 --oem 1"
txt = pytesseract.image_to_string(enhanced_path, config=options_all)

# Save output txt
txt_path = 'output/enhanced.txt'
with open(txt_path, 'w') as f:
    f.write(txt)
    f.close()

# Save flowchart
code2flow.code2flow(['path/to/filea', 'path/to/fileb'], 'path/to/outputfile')
