def programUpdate():

    checkForUpdates()
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
    print(decoded_line)
    if CurrentProgramVersion < int(decoded_line):
        print("Update Availible")
    else:
        print("Program is up to date")