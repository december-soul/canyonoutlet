from scrape_service import scrapeContent
from file_service import readFromFile, writeToFile
from email_service import sendMail

import numpy as np

url = 'https://www.canyon.com/en-hr/outlet/road-bikes/?cgid=outlet-road&prefn1=pc_familie&prefn2=pc_geschlecht&prefn3=pc_outlet&prefn4=pc_rahmengroesse&prefn5=pg_materialgroup&prefv1=Speedmax%7CUltimate%7CAeroad&prefv2=Unisex&prefv3=true&prefv4=L&prefv5=Complete%20bikes&srule=sort_price_ascending'
emailAddress = 'vuka66@gmail.com'

currentBikes = scrapeContent(url)
storedBikes = readFromFile()

if not np.array_equal(currentBikes, storedBikes):
    newBikes = [item for item in currentBikes if item not in storedBikes]

    if len(newBikes):
        sendMail(emailAddress, newBikes)

    writeToFile(currentBikes)


