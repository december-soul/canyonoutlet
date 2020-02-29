from services.scrape_service import scrapeContent
from services.file_service import FileService
from services.email_service import sendMail
from services.argument_parser import ArgumentParser

import numpy as np
import os

appPath = os.path.dirname(os.path.abspath(__file__))
fileService = FileService(appPath)

arguments = ArgumentParser()
if arguments.clearData:
    fileService.clearDataFolder()
    exit(0)

currentBikes = scrapeContent(arguments.url)
storedBikes = fileService.readFromFile(arguments.fileName)

if not np.array_equal(currentBikes, storedBikes):
    newBikes = [item for item in currentBikes if item not in storedBikes]

    # if len(newBikes):
    #     sendMail(email, newBikes)

    fileService.writeToFile(arguments.fileName, currentBikes)


