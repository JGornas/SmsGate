from twilio.rest import Client
from AUTH import ACCOUNT_SID, AUTH_TOKEN, SENDER_NUMBER, RECIVER_NUMBER
import logging


class Logger:
    def __init__(self):
        self.root_logger = logging.getLogger()
        self.root_logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler('smsgate.log', 'a', 'utf-8')
        handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(message)s'))
        self.root_logger.addHandler(handler)


class SmsSender(Logger):
    def __init__(self):
        super().__init__()
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_sms(self, text):
        self.root_logger.info(f"SMS MESSAGE: {text}")
        content = self.client.messages.create(
                                              body=text,
                                              from_=SENDER_NUMBER,
                                              to=RECIVER_NUMBER
                                             )
        print(content.sid)


if __name__ == "__main__":
    s = SmsSender()
    s.send_sms("Witaj podróżniku! Text example in unicode.")
