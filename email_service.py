import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromAddress = 'email4scrape@gmail.com'
password = 'throwawayaccount'

def sendMail(toAddress, content):
    port = 465
    smtpServer = "smtp.gmail.com"

    server = smtplib.SMTP_SSL(smtpServer, port)
    server.login(fromAddress, password)

    message = createEmail(toAddress, content).as_string()

    server.sendmail(fromAddress, toAddress, message)
    server.quit()

def createEmail(toAddress, content):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "New canyon outlet bikes available"
    msg['From'] = fromAddress
    msg['To'] = toAddress

    text = createTxtMessage(content)
    html = createHtmlMessage(content)

    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    msg.attach(part1)
    msg.attach(part2)
    return msg

def createTxtMessage(content):
    message = '%-*s %-*s %s\n\n' % (40, 'Model', 10, 'Price', 'Disc.')
    for element in content:
        message += '%-*s %-*s %s\n' % (40, element[0], 10, element[1], element[2])
    print(message)
    return message

def createHtmlMessage(content):
    html = """\
        <html>
        <head></head>
        <body>
            <table>
                <tr>
                    <td><b>Model</b></td>
                    <td><b>Price</b></td>
                    <td><b>Disc.</b></td>
                </tr>
        """

    for bike in content:
        html += '  <tr><td>'
        html += '    </td><td>'.join(bike)
        html += '  </td></tr>'

    html += """\
        </table>
        </body>
        </html>
        """
    
    return html