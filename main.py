import os
import pyautogui
import time

currDir = os.getcwd()
testImg = currDir + "/mamsch.png"

while(True):
    try:
        Ones_list = list(pyautogui.locateAllOnScreen(testImg, confidence=0.87))
        if(len(Ones_list) != 0):
            x = str(len(Ones_list))
            print(x + " Ones found:")
            print(*Ones_list, sep = ", ")
    except:
        print("nothing")
        pass
    time.sleep(2)
