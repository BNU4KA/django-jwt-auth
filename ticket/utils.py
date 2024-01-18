from django.core.mail import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()

class SendEmail:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['subject'],
            body=data['body'],
            from_email=os.environ.get('EMAIL_FROM'),
            to=[data['to_email']]
        )
        email.send()