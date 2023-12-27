from os import getcwd, listdir
from sys import stdout

def getImagePaths():
    while(True):
        imgDir = getcwd() + "/img/"
        files = listdir(imgDir)
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
    # err    = return False
    # no err = return True
    return False
