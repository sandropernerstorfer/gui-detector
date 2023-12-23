import cv2
import pytesseract
import os
import pyautogui
import time

currDir = os.getcwd()


testImg = currDir + "/testing.png"


while(True):
    try:
        res = pyautogui.locateOnScreen(testImg)
        print(res)
    except:
        print("nothing")
        pass
    time.sleep(2)

exit()





pytesseract.pytesseract.tesseract_cmd = currDir + '/tesseract/tesseract.exe'

# Screenshot
im = pyautogui.screenshot(region=(0, 0, 300, 400))
im.save(currDir + "/screenImg/img.png")
 
# Read image from which text needs to be extracted
img = cv2.imread(currDir + "/screenImg/img.png")

# Convert the image to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
# Performing OTSU threshold
ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
 
# Specify structure shape and kernel size. 
# Kernel size increases or decreases the area 
# of the rectangle to be detected.
# A smaller value like (10, 10) will detect 
# each word instead of a sentence.
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
 
# Applying dilation on the threshold image
dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
 
# Finding contours
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, 
                                                 cv2.CHAIN_APPROX_NONE)
 
# Creating a copy of image
im2 = img.copy()
 
# A text file is created and flushed
file = open(currDir + "/recognized.txt", "w+")
file.write("")
file.close()
 
# Looping through the identified contours
# Then rectangular part is cropped and passed on
# to pytesseract for extracting text from it
# Extracted text is then written into the text file
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
     
    rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
     
    cropped = im2[y:y + h, x:x + w]
     
    file = open(currDir + "/recognized.txt", "a")
    text = pytesseract.image_to_string(cropped)

    file.write(text)
    file.write("\n")
    file.close
    
import smtplib
sender = 'from@fromdomain.com'
receivers = ['to@todomain.com']
message = """
From: TradingView
To: Kunde
Subject: CHoCH Benachrichtigung
This is a test e-mail message.
"""
try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message)
    print("Successfully sent email")
except Exception as x:
    print("Error: unable to send email")
    print(x)
