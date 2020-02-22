import pickle

def readFromFile(name):
    try:
        with open('./CanyonScrape/' + name, 'rb') as filehandle:
            return pickle.load(filehandle)
    except:
        return []
        
def writeToFile(name, data):
    with open('./CanyonScrape/' + name, 'wb') as filehandle:
        pickle.dump(data, filehandle)
