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
    """
    sms prend 3 str args
    exp : numéro de l'expéditeur (twilio)
    dest : numéro du destinateur, (twilio) si le compte vérifie tjr le num.
    msg  : contenu du message
    """
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