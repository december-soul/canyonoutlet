import pickle
import os
import shutil

def readFromFile(path):
    try:
        with open(path, 'rb') as filehandle:
            return pickle.load(filehandle)
    except:
        return []
        
def writeToFile(path, data):
    with open(path, 'wb') as filehandle:
        pickle.dump(data, filehandle)

def clearFolder(path):
    shutil.rmtree(path)
    os.mkdir(path)
    print("Data cleared...")
    exit(0)