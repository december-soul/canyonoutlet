from services.scrape_service import scrapeContent
from services.file_service import readFromFile, writeToFile, clearFolder
from services.email_service import sendMail
from services.argument_parser import getArguments, shouldDeleteData

import numpy as np
import os

appPath = os.path.dirname(os.path.abspath(__file__))
dataPath = appPath + '/data/'

if shouldDeleteData():
    clearFolder(dataPath)

(email, fileName, url) = getArguments()
filePath = dataPath + fileName

currentBikes = scrapeContent(url)
storedBikes = readFromFile(filePath)

if not np.array_equal(currentBikes, storedBikes):
    newBikes = [item for item in currentBikes if item not in storedBikes]

    if len(newBikes):
        sendMail(email, newBikes)

    writeToFile(filePath, currentBikes)


