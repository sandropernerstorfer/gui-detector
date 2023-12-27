from time import strftime, localtime, sleep
from pyautogui import locateAllOnScreen
from utils import *
from view import *

def main():
    
    imagePaths = getImagePaths()
    latestScanRight = 0
    detections = []
    
    while(True):        
        currScanRight = 0
        for img in imagePaths:
            try:
                found = list(locateAllOnScreen(img, confidence = 0.9))
                if len(found) == 0: continue
                for box in found:
                    if box[0] > currScanRight:
                        currScanRight = box[0]
            except:
                pass
        if currScanRight > latestScanRight:
            sendStatus = sendEmail()
            detections.append(
                DetectionEntry(strftime("%d-%m-%Y %H:%M:%S", localtime()), sendStatus)
            )

        drawView(detections)
        latestScanRight = currScanRight
        sleep(.7)


if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    clearConsole()
    exit()
  except Exception as issue:
      print("The following application issue occured: ")
      print(issue)
