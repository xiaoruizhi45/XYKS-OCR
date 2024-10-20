import numpy as np
import pyautogui
import cv2
import PIL
import os
import pytesseract
from PIL import Image

region1 = (230,390,180,160)
region2 = (500,410,160,120)
region = region2

def change_color(image, target_color=(255, 255, 255), new_color=(224, 235, 254), tolerance=10):
    image_array = np.array(image)
    diff = np.abs(image_array - target_color)
    mask = np.all(diff <= tolerance, axis=-1)
    image_array[mask] = new_color
    new_image = Image.fromarray(image_array)
    return new_image

screenshot = pyautogui.screenshot(region=region)
screenshot = change_color(screenshot)
screenshot = np.array(screenshot)
screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGBA2BGR)
if not os.path.exists("./imgs"):
    os.makedirs("./imgs")
cv2.imwrite("./imgs/screen.jpg", screenshot)

def convert(screenshot):
    screenshot = change_color(screenshot)
    result = pytesseract.image_to_string(screenshot, config='--psm 6 -c tessedit_char_whitelist=0123456789')
    result = result.strip()
    if not result:
        return -1
    try:
        return int(result)
    except ValueError:
        return -1

# 示例用法：
# screenshot = pyautogui.screenshot(region=(x, y, width, height))  # 截图指定区域
screenshot = pyautogui.screenshot(region=region)
number = convert(screenshot)  # 转换截图中的数字
print(number)  # 输出数字或-1

wcenter = (450, 1000)
wspeed = 0.05
wsize = 100

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

while True:
    cm = input()
    if cm=="1":
        osmall()
    if cm=="2":
        obig()