from datetime import datetime, timedelta
import time
import pyautogui
import os
import email.message
import ssl
import smtplib

#
# view utils
# 
class DetectionEntry:
    def __init__(self, timestamp, gotSent):
        self.timestamp = timestamp
        self.gotSent = gotSent

def coloredText(color, text):
    if   color == "red"    : color = "91"
    elif color == "green"  : color = "92"
    elif color == "yellow" : color = "93"
    elif color == "cyan"   : color = "96"
    else                   : color = "0"
    return "\033["+color+"m"+text+"\033[0m"

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

def dotGenerator():
    count = 1
    while True:
        yield count * " ."
        if count >= 3: count = 1
        else: count += 1
dots = dotGenerator()

def drawView(detections):
    clearConsole()
    print("\n" + coloredText("cyan", "~") + " Scanning" + next(dots) + "\n")
    print("Detections            |   " + "Email")
    print("-------------------------------------")
    for el in detections:
        status = coloredText(el.gotSent[0], el.gotSent[1])
        print(el.timestamp + "   |   " + status)
        
#
# program
#
def main():
    
    # testmode
    testMode = False
    for file in os.listdir(os.getcwd())[:]:
        if file.startswith("testing"):
            testMode = True
            clearConsole()
            print("INFO:")
            print(coloredText("cyan", "*") + " app is in testing-mode")
            print(coloredText("cyan", "*") + " email sending will be simulated")
            time.sleep(6)
            break
    
    # get images
    imagePaths = []
    while(True):
        clearConsole()
        imgDir = os.getcwd() + "/img/"
        try:
            files = os.listdir(imgDir)
        except:
            input("Create \"img\" folder next to your .exe then press enter.")
            continue
        for file in files[:]:
            if file.endswith(".png"):
                imagePaths.append(imgDir + file)
        if len(imagePaths) > 0:
            break
        else:
            input("Missing .png image samples in \"img\" folder. Add images and press enter.")
    
    # scanner vars
    latestScanRight = 0
    detections = []
    lastEmailSent = datetime.now()
    
    # email vars
    sender   = "placeholder"
    password = "placeholder"
    receiver = "placeholder"
    subject  = "CHoCH-Detection"
    body     = "TradingView CHoCH Detection."
    em = email.message.EmailMessage()
    em['From'] = sender
    em['To'] = receiver
    em['subject'] = subject
    em.set_content(body)
    
    # scanner & email
    while(True):
                
        currScanRight = 0
        
        for img in imagePaths:
            try:
                found = list(pyautogui.locateAllOnScreen(img, confidence = 0.9))
                if len(found) == 0: continue
                for box in found:
                    if box[0] > currScanRight:
                        currScanRight = box[0]
            except:
                pass
            
        if currScanRight > latestScanRight:
            
            sendStatus = []
            now = datetime.now()
            diff = now - lastEmailSent
            
            if diff.seconds < 20:
                sendStatus = ["yellow", "Hold"]
            else:
                try:
                    if not testMode:
                        context = ssl.create_default_context()
                        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                            smtp.login(sender, password)
                            smtp.sendmail(sender, receiver, em.as_string())

                    lastEmailSent = now
                    sendStatus = ["green", "Sent"]
                except:
                    sendStatus = ["red", "Failed"]
            
            detections.append(DetectionEntry(time.strftime("%d-%m-%Y %H:%M:%S", time.localtime()), sendStatus))

        drawView(detections)
        latestScanRight = currScanRight
        time.sleep(.8)

#
# start main
#
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        clearConsole()
        exit()
    except Exception as issue:
        print("The following application issue occured: ")
        print(issue)
