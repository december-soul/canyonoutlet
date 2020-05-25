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
        parser.add_argument("-e", "--email",        help="Set email",           required=True,      type=str)
        parser.add_argument("-l", "--locale",       help="Set website locale",  default="hr",       type=str)
        parser.add_argument("-t", "--type",         help="Set bike type",       default="road",     type=str, choices=typeChoices)
        parser.add_argument("-s", "--size",         help="Set bike size",       required=True,      type=str, choices=sizeChoices)
        parser.add_argument("-m", "--model",        help="Set bike model(s)",   required=True,      type=str)
        parser.add_argument("-g", "--gender",       help="Set gender",          default="Unisex",   type=str, choices=genderChoices)
        parser.add_argument("-r", "--group",        help="Set group (Ultegra, 105, Dura Ace, ..)",  default="Ultegra", type=str)
        parser.add_argument("-p", "--price",        help="Set max price",       default=max,        type=int)

        self.__args = parser.parse_args()
    
    def __readArguments(self):
        self.email = self.__args.email
        emailRegex = r"[^@]+@[^@]+\.[^@]+"
        if not re.match(emailRegex, self.email):
            print("Error: Email address invalid")
            exit(1)

        self.fileName = self.email.split("@")[0] + ".data"

        self.locale = self.__args.locale
        self.type = self.__args.type
        self.size = self.__args.size
        self.model = self.__args.model.replace(",", "%7C")
        self.gender = self.__args.gender
        self.group = self.__args.group.replace(",", "%7C")
        self.max_price = self.__args.price

