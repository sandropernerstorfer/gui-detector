import os
import pyautogui
import time
import console

class NotificationEntry:
    def __init__(self, dateTime, gotSent):
        self.dateTime = dateTime
        self.gotSent = gotSent

# !! for testing
activeMonitor = input("LG or TUX?\n")

cwd = os.getcwd()
imgDir = cwd + "/img/" + activeMonitor + "/"
notifications = []

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
    
    # notification handling 
    if(currScanRight > latestScanRight):
        entry = NotificationEntry(time.strftime("%d-%m-%Y %H:%M:%S", time.localtime()), False)
        #
        # TODO EMAIL/SMS
        #
        notifications.append(entry)
    console.drawView(notifications)
    
    # update detection position and timeout
    latestScanRight = currScanRight
    time.sleep(1.5)
