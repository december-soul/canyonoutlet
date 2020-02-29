import argparse
import re
class ArgumentParser:
    def __init__(self):
        self.__configureArguments()
        self.__readArguments()
    
    def __configureArguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-e", "--email",        help="Set email",                   required=True)
        parser.add_argument("-l", "--localization", help="Set website localization",    required=True)
        parser.add_argument("-t", "--type",         help="Set bike type",               required=True)
        parser.add_argument("-s", "--size",         help="Set bike size",               required=True)
        parser.add_argument("-m", "--model",        help="Set bike model",              required=True)

        self.__args = parser.parse_args()
    
    def __readArguments(self):
        self.email = self.__args.email
        emailRegex = r"[^@]+@[^@]+\.[^@]+"
        if not re.match(emailRegex, self.email):
            print("Error: Email address invalid")
            exit(1)
            
            self.fileName = self.email.split("@")[0] + ".data"

        self.url = self.__args.url
        self.localization = self.__args.localization
        self.type = self.__args.type
        self.size = self.__args.size
        self.model = self.__args.model