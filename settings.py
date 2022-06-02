import os
import json

def initializeCalculatorSettings():
    appDataPath = (str)(os.getenv('LOCALAPPDATA'))
    pathname = appDataPath + '\SassyOwl\SagyCalculator\Settings'

    if not os.path.isdir(pathname):
        os.makedirs(pathname)

        settings = {
            "Version": 20000,
            "HR-Display": "Auto",
            "CopyToClipboard": True,
            "decimalsToCopy": 6,
            "display_as_fraction": True
        }

        settingsPath = pathname + '\settings.json'
        with open(settingsPath, "w") as settingsFile:
            json.dump(settings, settingsFile)

    else:
        appDataPath = (str)(os.getenv('LOCALAPPDATA'))
        settingsPath = appDataPath + '\SassyOwl\SagyCalculator\Settings\settings.json'
        fstream = open(settingsPath,)
        settings = json.load(fstream)
        if not "Version" in settings.keys():
            settings["Version"] = 10700
            settings["HR-Display"] = "Auto"
        if settings["Version"] < 20000:
            settings["Version"] = 20000
            settings["display_as_fraction"] = True
        saveSettingsToFile(settings)

def retrieveSettings():
    appDataPath = (str)(os.getenv('LOCALAPPDATA'))
    settingsPath = appDataPath + '\SassyOwl\SagyCalculator\Settings\settings.json'
    fstream = open(settingsPath,)
    settings = json.load(fstream)
    return settings

def saveSettingsToFile(settings):
    appDataPath = (str)(os.getenv('LOCALAPPDATA'))
    settingsPath = appDataPath + '\SassyOwl\SagyCalculator\Settings\settings.json'
    with open(settingsPath, "w") as settingsFile:
        json.dump(settings, settingsFile)

def get_HR_Display_Value():
    appDataPath = (str)(os.getenv('LOCALAPPDATA'))
    settingsPath = appDataPath + '\SassyOwl\SagyCalculator\Settings\settings.json'
    fstream = open(settingsPath,)
    settings = json.load(fstream)
    return settings.get("HR-Display")