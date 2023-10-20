#!/home/pydev/virtualenv/sms/bin/python

import os
import sms
import csv

message_path = f"{os.getcwd()}/message.txt"

def message():
    with open(message_path, 'r') as msg:
        return msg.read()

def send_to_all():
    """envoyer un message à tous les numéro dans le fichier target.csv"""

    # liste des numbers
    target_path = f"{os.getcwd()}/target.csv"

    with open(target_path, newline='') as csv_file:
        targets = csv.DictReader(csv_file, delimiter=',')
        print(f"\nLe contenu \033[33m{message_path}\033[00m sera envoyé à tous les numéro dans \033[33m{target_path}\033[00m")
        confirm = input("\nConfim \033[32mO\033[00m/\033[31mN\033[00m : ")
        if confirm.lower() in ('o', 'oui'):
            for target in targets:
                sms.send(target.get('Number'), message())
        else:
            print("\n\033[31mEnvoie annulé.\033[00m\n")


def sender():

    print("\nCountry available are [\033[32mFrance\033[00m, \033[32mItaly\033[00m, \033[32mMali\033[00m]")
    print("Country code \033[32m+33\033[00m for France, \033[32m+39\033[00m for Italy, \033[32m+223\033[00m for Mali")

    TO = input("\nPhone number (\033[32minclude country code\033[00m) :: ")
    if TO.lower() in ["q", 'stop', 'ok', "non", "n"]:
        print("Program stopped. Bye.")
        exit()

    print(f"\nLe contenu \033[33m{message_path}\033[00m sera envoyé à \033[33m{TO}\033[00m")

    confirm = input("\nConfim \033[32mO\033[00m/\033[31mN\033[00m : ")

    if confirm.lower() in ('o', 'oui'):
        sms.send(TO, message())
    else:
        print("\n\033[31mEnvoie annulé.\033[00m\n")


if __name__ == "__main__":
    print("\nQuelle fonction souhaitez-vous executer ?")
    print("\nCommands : \n [*] 1) Envoyer sms à un seul numéro\n [*] 2) Envoyer sms à tous les numéro")
    choice = input("\nCommand *> ")
    if choice == '1':
        sender()
    elif choice == '2':
        send_to_all()
    else:
        print("\nCommand incorrect. Réessayer\n")
