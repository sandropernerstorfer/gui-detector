from os import getcwd, listdir
from sys import stdout

def getImagePaths():
    while(True):
        imgDir = getcwd() + "/img/"
        try:
            files = listdir(imgDir)
        except:
            stdout.write('\x1b[1A') 
            stdout.write('\x1b[2K')
            input("Create \"img\" folder next to your .exe then press enter.")
            continue
            
        paths = []
        for file in files[:]:
            if file.endswith(".png"):
                paths.append(imgDir + file)
        if len(paths) > 0:
            break
        else:
            stdout.write('\x1b[1A') 
            stdout.write('\x1b[2K')
            input("Missing .png image samples in \"img\" folder. Add images and press enter.")
    return paths

def sendEmail():
    # err   = return False
    # noerr = return True
    # email spam guard - zb "Held Back" status wenn in zu kurzem zeitabstand
    # mit aws lambda testen

    return False
