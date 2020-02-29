import pickle
import os
import shutil
import errno
class FileService:
    def __init__(self, appPath):
        self.__appPath = appPath
        self.__dataFolderPath = appPath + '/data/'

    def readFromFile(self, fileName):
        try:
            with open(self.__dataFolderPath + fileName, 'rb') as filehandle:
                return pickle.load(filehandle)
        except:
            return []
            
    def writeToFile(self, fileName, data):
        self.__make_dir(self.__dataFolderPath)
        with open(self.__dataFolderPath + fileName, 'wb') as filehandle:
            pickle.dump(data, filehandle)

    def clearDataFolder(self):
        shutil.rmtree(self.__dataFolderPath)
        os.mkdir(self.__dataFolderPath)
        print("Data cleared...")

    def __make_dir(self, path):
        if not os.path.exists(path):
            try:
                os.makedirs(path)
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise