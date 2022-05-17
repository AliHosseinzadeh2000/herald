import smtplib
import ssl
from email.message import EmailMessage
from kavenegar import KavenegarAPI
import os


class TextSender:

    def __init__(self, phone_number, email, text):
        print("initialized text sender")
        self.to_phone_number = phone_number
        self.to_email = email
        self.text = text
        self.from_email = os.environ.get('YOUR_EMAIL')


    def send(self):

        if not self.to_phone_number:
            api = KavenegarAPI(os.environ.get('API_KEY'))
            params = {
                "receptor": self.to_phone_number,
                "message": self.text
            }
            api.sms_send(params)
            print('successfully sent the sms.')

        if not self.to_phone_number:
            msg = EmailMessage()
            msg['Subject'] = 'Herald app'
            msg['From'] = self.from_email
            msg['To'] = self.to_email
            msg.set_content(self.text)

            context = ssl.create_default_context()

            smtp = smtplib.SMTP("smtp.gmail.com", port=587, timeout=2)
            smtp.starttls(context=context)
            smtp.login(msg["From"], os.environ.get('EMAIL_PASSWORD'))
            smtp.send_message(msg)
            print('successfully sent the email.')
