import argparse
import re
class ArgumentParser:
    def __init__(self):
        self.__configureArguments()
        self.__readArguments()
    
    def __configureArguments(self):
        __parser = argparse.ArgumentParser()

        __parser.add_argument("-u", "--url", help="Set url")
        __parser.add_argument("-e", "--email", help="Set email")
        __parser.add_argument("-d", "--delete", help="Delete data", action="store_true")

        self.__args = __parser.parse_args()
    
    def __readArguments(self):
        url = self.__args.url
        if url:
            self.url = url
        else:
            print("Error: Url argument is mandatory")
            exit(1)
        
        email = self.__args.email
        if email:
            emailRegex = r"[^@]+@[^@]+\.[^@]+"
            if not re.match(emailRegex, email):
                print("Error: Email address invalid")
                exit(1)
            self.email = email
        else:
            print("Error: Email argument is mandatory")
            exit(1)

        self.clearData = self.__args.delete

        self.fileName = self.email.split("@")[0] + ".data"
    
