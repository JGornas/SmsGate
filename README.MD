# SmsGate

SmsGate - Python application for sms automatic distribution.
Uses Twilio provider. Login credentials for Twilio account are required.


## Installation

Use the package manager pip to install required libraries.

```bash
pip install -r requirements.txt
```

Set up following environment variables:
ACCOUNT_SID and AUTH_TOKEN (from twilio profile page).
You can also set up default
SENDER_NUMBER and default RECEIVER_NUMBER.

## Usage

```bash
python send_sms.py "message" [-s] [--sender] [-r] [--receiver]
```

## License

[MIT](https://choosealicense.com/licenses/mit/)

