import smtplib
from email.mime.text import MIMEText

def sendmsg(msg, email, password):
    # define content
    recipients = ["wesdeving@gmail.com"]
    sender = email
    subject = "**Craigslist Find!**"
    body = """\n
"""
    for each in msg:
        body += str(each['search']) + '\n'
        body += str(each['title']) + '\n'
        body += str(each['link']) + '\n\n'

    # make up message
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)

    # sending
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender, password)
    send_it = session.sendmail(sender, recipients, msg.as_string())
    session.quit()