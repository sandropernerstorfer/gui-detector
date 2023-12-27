from os import getcwd, listdir

def getImagePaths():
    imgDir = getcwd() + "/img/"
    files = listdir(imgDir)
    paths = []
    for file in files[:]:
        if file.endswith(".png"):
            paths.append(imgDir + file)   
    if len(paths) > 0:
        return paths
    else:
        print("Missing .png image samples in \"img\" folder")
        # TODO handle case
        exit()

def sendEmail():
    # err    = return False
    # no err = return True
    return False
