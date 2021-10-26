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