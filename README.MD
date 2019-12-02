# SmsGate

SmsGate - Python application for sms automatic distribution.
Uses Twilio provider. Login credentials for Twilio account are required.
Free subscription requires both sender and receiver numbers to be confirmed in settings page on their website.

## Installation

Use the package manager pip to install required libraries.

```bash
pip install -r requirements.txt
```

Fill the fields in send_sms.py file:
 account_sid, auth_token. Set a default sender - receiver 
numbers.

## Usage

```bash
python send_sms.py "message" [-s] [--sender] [-r] [--receiver]
```

## License

[MIT](https://choosealicense.com/licenses/mit/)

