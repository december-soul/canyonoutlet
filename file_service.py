import pickle

storageFileName = 'bikes.data'

def readFromFile():
    try:
        with open(storageFileName, 'rb') as filehandle:
            return pickle.load(filehandle)
    except:
        return []
        
def writeToFile(data):
    with open(storageFileName, 'wb') as filehandle:
        pickle.dump(data, filehandle)
