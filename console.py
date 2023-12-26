import os

def drawView(notifications):
    clearConsole()
    print("Scanning for CHoCH...")
    print("")
    printNotificationTable(notifications)
    print("")

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

def printNotificationTable(nList):
    print("---------------------------------------")
    print("CHoCH Detections      |   " + "Email/SMS")
    print("---------------------------------------")
    for x in nList:
        status = "Sent" if x.gotSent else "Not Sent"
        print(x.dateTime + "   |   " + status)
