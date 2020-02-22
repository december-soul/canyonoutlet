import pickle

def readFromFile(name):
    try:
        with open(name, 'rb') as filehandle:
            return pickle.load(filehandle)
    except:
        return []
        
def writeToFile(name, data):
    with open(name, 'wb') as filehandle:
        pickle.dump(data, filehandle)
