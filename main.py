import os, pyautogui, time

class DetectionEntry:
    def __init__(self, dateTime, gotSent):
        self.dateTime = dateTime
        self.gotSent = gotSent

def coloredText(color, text):
    if   color == "red"   : color = "91"
    elif color == "green" : color = "92"
    elif color == "cyan"  : color = "96"
    return "\033["+color+"m"+text+"\033[0m"

cwd = os.getcwd()
imgDir = cwd + "/img/"

images = os.listdir(imgDir)
for img in images[:]:
    if not(img.endswith(".png")):
        images.remove(img)
if(len(images) == 0):
    print("Missing .png image samples in \"img\" folder")
    # TODO handle case
    exit()

latestScanRight = 0
detections = []
loopCount = 1

while(True):    
    
    currScanRight = 0
    
    # detection
    for img in images:
        try:
            found = list(pyautogui.locateAllOnScreen(imgDir + img, confidence = 0.9))
            if(len(found) == 0): continue
            for box in found:
                if(box[0] > currScanRight):
                    currScanRight = box[0]
        except:
            pass
    
    # handle detection & notification
    if(currScanRight > latestScanRight):
        detection = DetectionEntry(time.strftime("%d-%m-%Y %H:%M:%S", time.localtime()), False)
        # TODO EMAIL/SMS after testing
        detections.append(detection)
    
    # draw console view
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n"+coloredText("cyan", "*") + " Scanning"+loopCount*' .'+"\n")
    print("CHoCH Detections      |   " + "Email")
    print("-------------------------------------")
    for el in detections:
        status = coloredText("green", "Sent") if el.gotSent else coloredText("red", "Failed")
        print(el.dateTime + "   |   " + status)
    loopCount = loopCount + 1 if loopCount < 3 else 1
    
    # update detection position and timeout
    latestScanRight = currScanRight
    time.sleep(1)
