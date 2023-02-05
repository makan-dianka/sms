from twilio.rest import Client
import os
import dotenv

dotenv.load_dotenv(".env")
path = f"{os.getcwd()}/message.txt"

def sms(exp, dest, msg):
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
        message = client.messages \
            .create(
                from_=exp,
                to=dest,
                body=msg,
            )
    except Exception as err:
        print(err)
    else:
        print("\033[32mMessage envoyé.\033[00m")


print("\nCountry available are [\033[32mFrance\033[00m, \033[32mItaly\033[00m, \033[32mMali\033[00m]")
print("Country code \033[32m+33\033[00m for France, \033[32m+39\033[00m for Italy, \033[32m+223\033[00m for Mali")

FROM = os.environ["NUMBER_1"]
TO = input("\nPhone number (\033[32minclude country code\033[00m) :: ")
if TO.lower() in ["q", 'stop', 'ok', "non", "n"]:
    print("Program stopped. Bye.")
    exit()

with open(path, "r") as msg:
    message = msg.read()
    print(f"\nLe contenu \033[33m{path}\033[00m sera envoyé à \033[33m{TO}\033[00m")
    confirm = input("\nConfirm O/N : ")
    if confirm.lower() == "o":
        sms(FROM, TO, message)
    else:
        print("\n\033[31mEnvoie annulé.\033[00m\n")