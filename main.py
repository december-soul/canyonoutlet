from services.scrape_service import scrapeContent
from services.file_service import readFromFile, writeToFile
from services.email_service import sendMail
from services.argument_parser import parseArguments

import numpy as np
import os

(email, fileName, url) = parseArguments()

dataPath = os.path.dirname(os.path.abspath(__file__)) + '/data/'
filePath = dataPath + fileName

currentBikes = scrapeContent(url)
storedBikes = readFromFile(filePath)

if not np.array_equal(currentBikes, storedBikes):
    newBikes = [item for item in currentBikes if item not in storedBikes]

    if len(newBikes):
        sendMail(email, newBikes)

    writeToFile(filePath, currentBikes)


