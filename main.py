from scrape_service import scrapeContent
from file_service import readFromFile, writeToFile
from email_service import sendMail, createMessage

import numpy as np

websiteUrl = 'https://www.canyon.com/en-hr/outlet/road-bikes/'
urlParameters = """?cgid=outlet-road
                    &prefn1=pc_geschlecht
                    &prefn2=pc_outlet
                    &prefn3=pc_rahmengroesse
                    &prefn4=pg_materialgroup
                    &prefv1=Unisex
                    &prefv2=true
                    &prefv3=XL%7CL
                    &prefv4=Complete%20bikes
                    &srule=sort_price_ascending
                """

emailAddress = 'markov@fotoin.com'
password = '12r0QO49p$Ex'

storedBikesFileName = 'bikes.data'

currentBikes = scrapeContent(websiteUrl + urlParameters)
storedBikes = readFromFile(storedBikesFileName)

if not np.array_equal(currentBikes, storedBikes):
    newBikes = [item for item in currentBikes if item not in storedBikes]

    message = createMessage(newBikes)
    sendMail(emailAddress, password, message)
    print(message)

    writeToFile(storedBikesFileName, currentBikes)


