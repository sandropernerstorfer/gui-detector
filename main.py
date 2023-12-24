import os
import pyautogui
import time

currDir = os.getcwd()
imgDir = currDir + "/img/"

while(True):
    try:
        Ones_list = list(pyautogui.locateAllOnScreen(imgDir + "/x.png", confidence=0.9))
        if(len(Ones_list) != 0):
            x = str(len(Ones_list))
            print(x + " Ones found:")
            print(*Ones_list, sep = ", ")
    except:
        print("nothing")
        pass
    time.sleep(2)
