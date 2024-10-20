from PIL import Image
import numpy as np
import pytesseract
import pyautogui
import time
import cv2
import os

region1 = (230,390,180,160)
region2 = (500,410,160,120)
region = (200,390,500,180)
wcenter = (450, 1000)
wspeed = 0.05
wsize = 100

def change_color(image, target_color=(255, 255, 255), new_color=(224, 235, 254), tolerance=10):
    image_array = np.array(image)
    diff = np.abs(image_array - target_color)
    mask = np.all(diff <= tolerance, axis=-1)
    image_array[mask] = new_color
    new_image = Image.fromarray(image_array)
    return new_image

def convertint(screenshot):
    screenshot = change_color(screenshot)
    result = pytesseract.image_to_string(screenshot, config='--psm 6 -c tessedit_char_whitelist=0123456789')
    result = result.strip()
    if not result:
        return -1
    try:
        return int(result)
    except ValueError:
        return -1

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


def osmall():
    pyautogui.mouseUp()
    pyautogui.moveTo(wcenter[0]+wsize, wcenter[1]-wsize, 0)
    pyautogui.mouseDown()
    pyautogui.moveTo(wcenter[0]-wsize, wcenter[1], wspeed/2)
    pyautogui.moveTo(wcenter[0]+wsize, wcenter[1]+wsize, wspeed/2)
    pyautogui.mouseUp()

def obig():
    pyautogui.mouseUp()
    pyautogui.moveTo(wcenter[0] - wsize, wcenter[1] - wsize, 0)
    pyautogui.mouseDown()
    pyautogui.moveTo(wcenter[0] + wsize, wcenter[1], wspeed / 2)
    pyautogui.moveTo(wcenter[0] - wsize, wcenter[1] + wsize, wspeed / 2)
    pyautogui.mouseUp()


print("Detecting...")
while True:
    trigger1 = convertint(pyautogui.screenshot(region=region1))!=-1
    trigger2 = convertint(pyautogui.screenshot(region=region2))!=-1
    if trigger1 and trigger2:
        break   ## Wait until numbers appear

print("Started")

# input()

while True:
    img_num_1 = pyautogui.screenshot(region=region1)
    img_num_2 = pyautogui.screenshot(region=region2)
    num_1 = convertint(img_num_1)
    num_2 = convertint(img_num_2)
    print(num_1, num_2, sep=" ? ")
    if (num_1==-1 or num_2==-1):
        continue
    if (num_1 < num_2):
        print(num_1, "<", num_2)
        osmall()
    elif (num_1 > num_2):
        print(num_1, ">", num_2)
        obig()
    else:
        osmall()
        time.sleep(0.2)
        obig()
    print("\n")
    time.sleep(0.2)
