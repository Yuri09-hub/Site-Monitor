import smtplib
import os
from email.message import Message
from pydantic import EmailStr
from dotenv import load_dotenv

load_dotenv()
def message(email:EmailStr,value):

    if value in [500,502,503,504]:
        content = f"<p>The status of website has changed to 'DOWN' </p>"
    else:
        content = f"<p>The status of website has changed to 'UP' </p>"


    msg = Message()
    msg['subject'] = 'Price alert'
    msg['from'] = str(os.getenv("EMAIL"))
    msg['to'] = email
    msg.add_header("content-type", "text/html")
    msg.set_payload(content)

    s = smtplib.SMTP("smtp.gmail.com",587)
    s.starttls()
    s.login(str(os.getenv("EMAIL")),str(os.getenv("PASSWORD")))
    s.sendmail(msg['from'],msg['to'],msg.as_string())