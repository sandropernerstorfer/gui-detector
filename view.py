from os import system, name

class DetectionEntry:
    def __init__(self, dateTime, gotSent):
        self.dateTime = dateTime
        self.gotSent = gotSent

def coloredText(color, text):
    if   color == "red"   : color = "91"
    elif color == "green" : color = "92"
    elif color == "cyan"  : color = "96"
    else                  : color = "0"
    return "\033["+color+"m"+text+"\033[0m"

# generator for the dots in "Scanning..."
def dotGenerator():
    count = 1
    while True:
        yield count * " ."
        if count >= 3: count = 1
        else: count += 1
dots = dotGenerator()

def drawView(detections):
    system('cls' if name == 'nt' else 'clear')
    print("[" + coloredText("cyan", "P") + "]ause/Resume    [" + coloredText("cyan", "Q") + "]uit")
    print("\n" + coloredText("cyan", "~") + " Scanning" + next(dots) + "\n")
    print("CHoCH Detections      |   " + "Email")
    print("-------------------------------------")
    for el in detections:
        status = coloredText("green", "Sent") if el.gotSent else coloredText("red", "Failed")
        print(el.dateTime + "   |   " + status)
