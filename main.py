import requests
from bs4 import BeautifulSoup

import pickle

import smtplib, ssl
import certifi

import numpy as np

websiteUrl = 'https://www.canyon.com/en-hr/outlet/road-bikes/'
urlParameters = '?cgid=outlet-road&prefn1=pc_outlet&prefn2=pc_rahmengroesse&prefv1=true&prefv2=L&srule=sort_price_ascending'

storedBikesFileName = 'bikes.data'

emailAddress = 'markov@fotoin.com'
password = '12r0QO49p$Ex'

def readFromFile(name):
    try:
        with open(name, 'rb') as filehandle:
            return pickle.load(filehandle)
    except:
        return []
        

def writeToFile(name, data):
    with open(storedBikesFileName, 'wb') as filehandle:
        pickle.dump(data, filehandle)

def scrapeContent(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    bikes = soup.find_all('div', class_='productTile__contentWrapper')
    filteredContent = []
    for bike in bikes:
        name = bike.find('span', class_='productTile__productName').text.strip()
        regularPrice = bike.find('span', class_='productTile__productPriceOriginal').text.strip().replace('\u20ac', '')
        salePrice = bike.find('span', class_='productTile__productPriceSale').text.strip().replace('\u20ac', '')

        if None in (name, regularPrice, salePrice):
            continue
        
        filteredContent.append([name, regularPrice, salePrice])
    return filteredContent

def sendMail(emailAddress, password, message):
    port = 465
    smtpServer = "smtp.gmail.com"

    context = ssl.create_default_context(cafile=certifi.where())

    server = smtplib.SMTP_SSL(smtpServer, port, context=context)
    server.login(emailAddress, password)
    server.sendmail(emailAddress, emailAddress, message)
    server.quit()

def createMessage(bikes):
    message = '%-*s %-*s %s\n\n' % (43, 'Model', 9, 'Price', 'Discounted')
    for bike in bikes:
        message += '%-*s %-*s %s\n' % (40, bike[0], 14, bike[1], bike[2])
    return message

currentBikes = scrapeContent(websiteUrl + urlParameters)
storedBikes = readFromFile(storedBikesFileName)

if not np.array_equal(currentBikes, storedBikes):
    newBikes = [item for item in currentBikes if item not in storedBikes]

    message = createMessage(newBikes)
    sendMail(emailAddress, password, message)

    writeToFile(storedBikesFileName, currentBikes)


