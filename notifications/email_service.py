import os
import smtplib
from email.message import EmailMessage

class EmailService:

    def send(self, subject, body):
        email = os.getenv("EMAIL_ADDRESS")
        password = os.getenv("EMAIL_APP_PASSWORD")
        message = EmailMessage()
        message["subject"] = subject
        message["from"] = email
        message["to"] = email

        message.set_content(body)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(email, password)
            smtp.send_message(message)  

        print("Email sent successfully!")
