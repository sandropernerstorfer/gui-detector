import os
import pyautogui
import time

currDir = os.getcwd()
imgDir = currDir + "/img/"

# get ./img contents and sort out non-png files
images = os.listdir("img")
for img in images[:]:
    if not(img.endswith(".png")):
        images.remove(img)

# memory of latest detected occurence position
furthestRight = 0

while(True):
    newRight = 0
    
    for img in images:
        try:
            found = list(pyautogui.locateAllOnScreen(imgDir + img, confidence=0.9))
            if(len(found) == 0): continue
            for box in found:
                if(box[0] > newRight):
                    newRight = box[0]
        except:
            pass

    if(newRight > furthestRight):
        print("Send Notification!")
    furthestRight = newRight
    time.sleep(1)

# CLI schöner machen - clear all
# uhrzeit usw dazu wenn nachricht - und in liste speichern - immer oben anzeigen
# sonst während runtime eine art lade animation mit punkten usw
# btn zum beenden
