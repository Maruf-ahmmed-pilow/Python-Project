from email.message import EmailMessage
from app2 import password
import ssl
import smtplib


email_sender = "pilowpp1997@gmail.com"
email_password = password

email_receiver = "bifiha8975@bodeem.com"

subject = "Dont forget me"

body = """
hey buddy ("_")
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())
    
