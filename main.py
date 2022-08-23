import time
import random
import cv2
import keyboard
import numpy as np

from PIL import ImageGrab

cooldown = True
fishing = cv2.imread('image.png', 0)
templateWidth, templateHeight = fishing.shape[::-1]

print("Fishing will be started in 5 seconds!")
time.sleep(5)
print("Started!")

while True:
    if (cooldown):
        print("Casting now!")
        keyboard.press_and_release('f')
        cooldown = False
        continue

    imagehook = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
    pixelhook = np.array(imagehook)

    imagescale = cv2.cvtColor(pixelhook, cv2.COLOR_BGR2GRAY)
    templateMatch = cv2.matchTemplate(
    imagescale, fishing, cv2.TM_CCOEFF_NORMED)
    matchxyz = np.where(templateMatch >= 0.8)

    for point in zip(*matchxyz[::-1]):
        if point != None:
            print("Catch!")
            keyboard.press_and_release('f')
            cooldown = True
            time.sleep(random.uniform(6, 7.5))
            break

    time.sleep(0.150)
