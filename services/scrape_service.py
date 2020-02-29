import requests
from bs4 import BeautifulSoup

def scrapeContent(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    bikes = soup.find_all('div', class_='productTile__contentWrapper')
    filteredContent = []
    for bike in bikes:
        name = bike.find('span', class_='productTile__productName').text.strip()
        regularPrice = bike.find('span', class_='productTile__productPriceOriginal').text.strip()[:-5]
        salePrice = bike.find('span', class_='productTile__productPriceSale').text.strip()[:-5]

        if None in (name, regularPrice, salePrice):
            continue
        
        filteredContent.append([name, regularPrice, salePrice])
    return filteredContent
