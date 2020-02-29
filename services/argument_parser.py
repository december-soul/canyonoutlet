import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="Set url")
parser.add_argument("-e", "--email", help="Set email")
parser.add_argument("-d", "--delete", help="Delete data", action="store_true")

args = parser.parse_args()

def getArguments():
    if args.url:
        url = args.url
    else:
        print("Error: Url argument is mandatory")
        exit(1)
    
    if args.url:
        email = args.email
    else:
        print("Error: Email argument is mandatory")
        exit(1)

    fileName = email.split("@")[0] + ".data"

    return (email, fileName, url)

def shouldDeleteData():
    return args.delete
    
