import smtplib
import ssl

def sendemail(message):
    host = "smtp.gmail.com"
    port = 465
    username = "riyagaming65@gmail.com"
    password = "pspu lgtw yqjq yiit"

    context = ssl.create_default_context()

    receiver ="riyagaming65@gmail.com"
    message = """\
    Subject: Thank For Connecting
    Sucessfully Sent
    
    """

    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)

