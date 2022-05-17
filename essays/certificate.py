import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText


import pandas as pd

def read_csv():
    df= pd.read_csv("appreciation.csv")
    number_of_people = df.shape[0]
    for i in range(0,number_of_people):
        email = df['Email'][i].strip()
        image = f'{i+1}_.jpg'
        name = df['Presenter'][i]
        preamble = f'Dear {name}, \nThank you for participating in IAHR-ASIA 2021.\nPlease find the certificate of participation attached to this mail. \n --- \n Regards, \n IAHR-Asia 2021 \n Turbine Testing Lab, \n Kathmandu University \n Nepal '
        with open("log.txt",'a+') as f:
            f.write(f'sending mail to {email} number {i}')
        print("sending mail --------")
        print(email)
        print(image)
        print('----------------')
        send_mail(email,image,preamble)

    
def send_mail(emailto, fileToSend, preamble):
    emailfrom = "iahr.asia.2021@ku.edu.np"
    # emailto = "ashish.thapa477@gmail.com"
    # fileToSend = "1_.jpg"
    usernames= "athapa54021319@gmail.com"
    passwords = "ePoweripi=1"
    username = "iahr.asia.2021@ku.edu.np"
    password= "ttl.ku.edu.np"

    msg = MIMEMultipart()
    msg["From"] = emailfrom
    msg["To"] = emailto
    msg["Subject"] = "IAHR-ASIA 2021"
    msg.attach(MIMEText(preamble,"plain"))

    ctype, encoding = mimetypes.guess_type(fileToSend)
    if ctype is None or encoding is not None:
        ctype = "application/octet-stream"

    maintype, subtype = ctype.split("/", 1)

    if maintype == "text":
        fp = open(fileToSend)
        # Note: we should handle calculating the charset
        attachment = MIMEText(fp.read(), _subtype=subtype)
        fp.close()
    elif maintype == "image":
        fp = open(fileToSend, "rb")
        attachment = MIMEImage(fp.read(), _subtype=subtype)
        fp.close()
    elif maintype == "audio":
        fp = open(fileToSend, "rb")
        attachment = MIMEAudio(fp.read(), _subtype=subtype)
        fp.close()
    else:
        fp = open(fileToSend, "rb")
        attachment = MIMEBase(maintype, subtype)
        attachment.set_payload(fp.read())
        fp.close()
        encoders.encode_base64(attachment)
    attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
    msg.attach(attachment)


    server = smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
    server.login(username,password)
    server.sendmail(emailfrom, emailto, msg.as_string())
    server.quit()

read_csv()