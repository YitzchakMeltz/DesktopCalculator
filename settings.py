import os
import json

def initializeCalculatorSettings():
    appDataPath = (str)(os.getenv('LOCALAPPDATA'))
    pathname = appDataPath + '\SassyOwl\SagyCalculator\Settings'

    if not os.path.isdir(pathname):
        os.makedirs(pathname)

        settings = {
            "HR-Display": True,
            "CopyToClipboard": True,
            "decimalsToCopy": 6
        }

        settingsPath = pathname + '\settings.json'
        with open(settingsPath, "w") as settingsFile:
            json.dump(settings, settingsFile)

def retrieveSettings():
    appDataPath = (str)(os.getenv('LOCALAPPDATA'))
    settingsPath = appDataPath + '\SassyOwl\SagyCalculator\Settings\settings.json'
    fstream = open(settingsPath,)
    settings = json.load(fstream)
    return settings