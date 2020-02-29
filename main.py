from scrape_service import scrapeContent
from file_service import readFromFile, writeToFile
from email_service import sendMail
from argument_parser import parseArguments

import numpy as np

(email, fileName, url) = parseArguments()

currentBikes = scrapeContent(url)
storedBikes = readFromFile(fileName)

if not np.array_equal(currentBikes, storedBikes):
    newBikes = [item for item in currentBikes if item not in storedBikes]

    if len(newBikes):
        sendMail(email, newBikes)

    writeToFile(fileName, currentBikes)


