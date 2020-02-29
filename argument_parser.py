import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="Set url", required=True)
parser.add_argument("-e", "--email", help="Set email", required=True)

args = parser.parse_args()

def parseArguments():
    if args.url:
        url = args.url

    if args.email:
        email = args.email
    
    fileName = email.split("@")[0] + ".data"

    return (email, fileName, url)
    
