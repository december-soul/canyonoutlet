from services.scrape_service import scrapeContent
from services.file_service import FileService
from services.email_service import sendMail
from services.argument_parser import getArguments, shouldDeleteData

import numpy as np
import os

appPath = os.path.dirname(os.path.abspath(__file__))
fileService = FileService(appPath)

if shouldDeleteData():
    fileService.clearDataFolder()
    exit(0)

(email, fileName, url) = getArguments()

currentBikes = scrapeContent(url)
storedBikes = fileService.readFromFile(fileName)

if not np.array_equal(currentBikes, storedBikes):
    newBikes = [item for item in currentBikes if item not in storedBikes]

    # if len(newBikes):
    #     sendMail(email, newBikes)

    fileService.writeToFile(fileName, currentBikes)


