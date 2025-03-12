import cv2

import numpy as np

print("Running AI UI Validator")

# Define full paths for images

baseline_path = r"C:\Users\SHRTOMAR\OneDrive - Capgemini\Desktop\Python\AI_UI_Validator\saucedemo_baseline.png"

changed_path = r"C:\Users\SHRTOMAR\OneDrive - Capgemini\Desktop\Python\AI_UI_Validator\saucedemo_changed.png"

# Load the baseline and changed screenshots

baseline_img = cv2.imread(baseline_path)

changed_img = cv2.imread(changed_path)

# Check if images loaded correctly

if baseline_img is None or changed_img is None:

    print(f"Error: One or both images not found.\nBaseline Path: {baseline_path}\nChanged Path: {changed_path}")

    exit()

# Convert images to grayscale

baseline_gray = cv2.cvtColor(baseline_img, cv2.COLOR_BGR2GRAY)

changed_gray = cv2.cvtColor(changed_img, cv2.COLOR_BGR2GRAY)

# Compute absolute difference between images

diff = cv2.absdiff(baseline_gray, changed_gray)

# Apply threshold to highlight differences

_, thresh = cv2.threshold(diff, 50, 255, cv2.THRESH_BINARY)

# Save the difference image

diff_path = r"C:\Users\SHRTOMAR\OneDrive - Capgemini\Desktop\Python\AI_UI_Validator\ui_diff.png"

cv2.imwrite(diff_path, thresh)

print(f"UI differences saved in: {diff_path}")

# Display the difference image

cv2.imshow("Differences", thresh)

cv2.waitKey(0)

cv2.destroyAllWindows() 