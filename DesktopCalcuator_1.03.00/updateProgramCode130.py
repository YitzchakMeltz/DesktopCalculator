def programUpdate():

    return

def checkForUpdates():

    CurrentProgramVersion = 10201

    print("Current Version: ",CurrentProgramVersion)

    import urllib.request
    url = "https://raw.githubusercontent.com/YitzchakMeltz/SassyOwl/main/Sagy%20Calculator/Desktop%20Program/SagyDesktopVersion.txt"
    file = urllib.request.urlopen(url)

    for line in file:
        decoded_line = line.decode("utf-8")
        
    decoded_line = decoded_line.replace(".","")

    if CurrentProgramVersion < int(decoded_line):
        print("Update Availible")
        return True
    else:
        print("Program is up to date")
        return False

    return False

def makeUpdateFolder():
    import os

    dir = os.path.dirname(__file__)
    pathname = os.path.join(dir, 'Updates')

    if not os.path.isdir(pathname):
        os.makedirs(pathname)

    else:
        dir = os.path.dirname(__file__)
        filename = os.path.join(dir, 'Updates','Sagy Calculator Setup.exe')
        if os.path.exists(filename):
            os.remove(filename)

def updateCalc():
    makeUpdateFolder()
    return