from twilio.rest import Client
import os
import dotenv
import logging

logging.basicConfig(
    format='[%(asctime)s] %(message)s', 
    datefmt='%m/%d/%Y %I:%M:%S',
    level=logging.INFO,
    filename='contact.log'
    )

dotenv.load_dotenv(".env")

def send(exp, dest, msg):
    account_sid = os.environ['ACCOUNT_SID']
    auth_token = os.environ['AUTH_TOKEN']

    client = Client(account_sid, auth_token)

    try:
        client.messages \
            .create(
                from_=exp,
                to=dest,
                body=msg,
            )
    except Exception as err:
        print(err)
    else:
        print("\033[32mMessage envoyé.\033[00m")
        logging.info(f"Message envoyé à [{dest}]")