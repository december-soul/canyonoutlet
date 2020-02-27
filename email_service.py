import smtplib, ssl

def sendMail(emailAddress, password, message):
    port = 465
    smtpServer = "smtp.gmail.com"

    server = smtplib.SMTP_SSL(smtpServer, port)
    server.login(emailAddress, password)

    server.sendmail(emailAddress, emailAddress, message)
    server.quit()

def createMessage(bikes):
    message = '%-*s %-*s %s\n\n' % (43, 'Model', 9, 'Price', 'Discounted')
    for bike in bikes:
        message += '%-*s %-*s %s\n' % (40, bike[0], 14, bike[1], bike[2])
    return message
