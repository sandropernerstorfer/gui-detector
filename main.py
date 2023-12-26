import os
import pyautogui
import time

# !! for testing
activeMonitor = input("LG or TUX?\n")

cwd = os.getcwd()
imgDir = cwd + "/img/" + activeMonitor + "/"

# get .png's from ./img
images = os.listdir(imgDir)
for img in images[:]:
    if not(img.endswith(".png")):
        images.remove(img)
if(len(images) == 0):
    print("Missing .png image samples in \"img\" folder")
    exit()

# memory of latest detected occurence - furthest right position
latestScanRight = 0

while(True):
    
    currScanRight = 0
    
    for img in images:
        try:
            found = list(pyautogui.locateAllOnScreen(imgDir + img, confidence = 0.9))
            if(len(found) == 0): continue
            for box in found:
                if(box[0] > currScanRight):
                    currScanRight = box[0]
        except:
            pass

    if(currScanRight > latestScanRight):
        print("Email/SMS notification!")
    latestScanRight = currScanRight

    time.sleep(1.5)
