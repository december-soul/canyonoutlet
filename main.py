from services.scrape_service import scrapeContent
from services.file_service import readFromFile, writeToFile, clearDataFolder
from services.email_service import sendMail
from services.argument_parser import getArguments, shouldDeleteData

import numpy as np
import os

appPath = os.path.dirname(os.path.abspath(__file__))

if shouldDeleteData():
    clearDataFolder(appPath)

(email, fileName, url) = getArguments()

currentBikes = scrapeContent(url)
storedBikes = readFromFile(appPath, fileName)

if not np.array_equal(currentBikes, storedBikes):
    newBikes = [item for item in currentBikes if item not in storedBikes]

    if len(newBikes):
        sendMail(email, newBikes)

    writeToFile(appPath, fileName, currentBikes)


