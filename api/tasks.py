from celery import Celery
from api.services import TextSender


app = Celery('tasks', broker='redis://localhost:6379')

@app.task(bind=True, queue='send')
def send_text(self, phone_number, email, text):
    print('send email celery task -------')
    print('send sms celery task ########')

    try:
        text_sender = TextSender(phone_number=phone_number, email=email, text=text)
        text_sender.send()
    except Exception as exc:
        print(f'------------ exc: {exc}')
        raise self.retry(exc=exc)

    print('------- finished sending email')
    print('######## finished sending sms')
