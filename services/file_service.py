import pickle
import os
import shutil
import errno

dataPath = '/data/'

def readFromFile(appPath, fileName):
    path = appPath + dataPath
    try:
        with open(path + fileName, 'rb') as filehandle:
            return pickle.load(filehandle)
    except:
        return []
        
def writeToFile(appPath, fileName, data):
    path = appPath + dataPath
    make_dir(path)
    with open(path + fileName, 'wb') as filehandle:
        pickle.dump(data, filehandle)

def clearDataFolder(appPath):
    path = appPath + dataPath
    shutil.rmtree(path)
    os.mkdir(path)
    print("Data cleared...")
    exit(0)

def make_dir(path):
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise