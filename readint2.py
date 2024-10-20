from PIL import Image
import numpy as np
import pytesseract
import pyautogui
import time
import cv2
import os

region = (200,390,500,180)

def change_color(image, target_color=(255, 255, 255), new_color=(224, 235, 254), tolerance=10):
    image_array = np.array(image)
    diff = np.abs(image_array - target_color)
    mask = np.all(diff <= tolerance, axis=-1)
    image_array[mask] = new_color
    new_image = Image.fromarray(image_array)
    return new_image

def convertlst(screenshot):
    screenshot = change_color(screenshot)
    result = pytesseract.image_to_string(screenshot, config='--psm 6 -c tessedit_char_whitelist=0123456789?')
    result = result.strip()
    if not result:
        return -1
    try:
        result.find("?")
        return result.split("?")
    except ValueError:
        return [-1]

screenshot = pyautogui.screenshot(region=region)
screenshot = change_color(screenshot)
screenshot = np.array(screenshot)
screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGBA2BGR)
if not os.path.exists("./imgs"):
    os.makedirs("./imgs")
cv2.imwrite("./imgs/ri.jpg", screenshot)

print(convertlst(screenshot))
