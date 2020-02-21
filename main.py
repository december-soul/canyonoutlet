import requests
from bs4 import BeautifulSoup
import pickle

URL = 'https://www.canyon.com/en-hr/outlet/road-bikes/?cgid=outlet-road&prefn1=pc_outlet&prefn2=pc_rahmengroesse&prefv1=true&prefv2=L&srule=sort_price_ascending'
storedBikesFileName = 'bikes.data'

def readFromFile(name):
    with open(name, 'rb') as filehandle:
        return pickle.load(filehandle)

def writeToFile(name, data):
    with open(storedBikesFileName, 'wb') as filehandle:
        pickle.dump(data, filehandle)

def scrapeContent():
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    bikes = soup.find_all('div', class_='productTile__contentWrapper')
    # print("%-*s %-*s %s" % (40, "Model name", 20, "Regular price", "Sale price"))
    filteredContent = []
    for bike in bikes:
        name = bike.find('span', class_='productTile__productName').text.strip()
        regularPrice = bike.find('span', class_='productTile__productPriceOriginal').text.strip()
        salePrice = bike.find('span', class_='productTile__productPriceSale').text.strip()

        if None in (name, regularPrice, salePrice):
            continue
        
        filteredContent.append([name, regularPrice, salePrice])
        # print("%-*s %-*s %s" % (40, name, 20, regularPrice, salePrice))
    return filteredContent

content = scrapeContent()

storedBikes = readFromFile(storedBikesFileName)
print(storedBikes)

writeToFile(storedBikesFileName, content)


