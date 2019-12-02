import argparse
import logging
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from AUTH import ACCOUNT_SID, AUTH_TOKEN, SENDER_NUMBER, RECEIVER_NUMBER


class Logger:
    def __init__(self, level=logging.DEBUG, filename="smsgate.log", mode="a", encoding="utf-8"):
        self.root_logger = logging.getLogger()
        self.root_logger.setLevel(level)
        handler = logging.FileHandler(filename, mode, encoding)
        handler.setFormatter(logging.Formatter("%(asctime)s:%(levelname)s:%(message)s"))
        self.root_logger.addHandler(handler)


class SmsSender(Logger):
    def __init__(self, account_sid=ACCOUNT_SID, auth_token=AUTH_TOKEN):
        super().__init__()
        self.client = Client(account_sid, auth_token)

    def send_sms(self, text, sender_number, receiver_number):
        self.root_logger.info(f"SMS MESSAGE: {text}")
        content = self.client.messages.create(
                                              body=text,
                                              from_=sender_number,
                                              to=receiver_number
                                             )
        print(content.date_updated, content.sid)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("message", help="message content")
    parser.add_argument("-s", "--sender", type=int, help="custom sender number", default=SENDER_NUMBER)
    parser.add_argument("-r", "--reciever", type=int, help="custom receiver number", default=RECEIVER_NUMBER)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()

    s = SmsSender()
    try:
        s.send_sms(args.message, args.sender, args.reciever)
        print(f"'{args.message}' - Message sent successfully from +{args.sender} to +{args.reciever}.")
    except TwilioRestException:
        print("Unable to send message. Invalid phone number.")
