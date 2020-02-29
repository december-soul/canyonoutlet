import argparse
import re
class ArgumentParser:
    def __init__(self):
        self.__configureArguments()
        self.__readArguments()
    
    def __configureArguments(self):
        typeChoices = ["road", "mountain", "urban", "fitness", "pro"]
        sizeChoices = ["3XS", "2XS", "XS", "S", "M", "L", "XL", "2XL", "3XL"]
        genderChoices = ["Unisex", "WMNS"]

        parser = argparse.ArgumentParser()
        parser.add_argument("-e", "--email",        help="Set email",                           required=True, type=str)
        parser.add_argument("-l", "--localization", help="Set website localization",            default="de",  type=str)
        parser.add_argument("-t", "--type",         help="Set bike type",                       required=True, type=str, choices=typeChoices)
        parser.add_argument("-s", "--size",         help="Set bike size",                       required=True, type=str, choices=sizeChoices)
        parser.add_argument("-m", "--model",        help="Set bike models(comma separated)",    required=True, type=str)
        parser.add_argument("-g", "--gender",       help="Set gender (Unisex/WMNS)",            required=True, type=str, choices=genderChoices)

        self.__args = parser.parse_args()
    
    def __readArguments(self):
        self.email = self.__args.email
        emailRegex = r"[^@]+@[^@]+\.[^@]+"
        if not re.match(emailRegex, self.email):
            print("Error: Email address invalid")
            exit(1)

        self.fileName = self.email.split("@")[0] + ".data"

        self.localization = self.__args.localization
        self.type = self.__args.type
        self.size = self.__args.size
        self.model = self.__args.model.replace(",", "%7C")
        self.gender = self.__args.gender

        