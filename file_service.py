import pickle
import os

path = os.path.dirname(os.path.abspath(__file__)) + '/data/'

def readFromFile(fileName):
    try:
        with open(path + fileName, 'rb') as filehandle:
            return pickle.load(filehandle)
    except:
        return []
        
def writeToFile(fileName, data):
    with open(path + fileName, 'wb') as filehandle:
        pickle.dump(data, filehandle)
