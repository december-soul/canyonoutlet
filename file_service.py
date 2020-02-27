import pickle
import os

path = os.path.dirname(os.path.abspath(__file__))
fileName = 'storage.data'
fileFullPath = path + '/' + fileName

def readFromFile():
    try:
        with open(fileFullPath, 'rb') as filehandle:
            return pickle.load(filehandle)
    except:
        return []
        
def writeToFile(data):
    with open(fileFullPath, 'wb') as filehandle:
        pickle.dump(data, filehandle)
