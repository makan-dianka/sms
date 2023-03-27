# Envoyer un simple sms

Ce petit programme vous permet d'envoyer un message à n'import quel numéro depuis votre terminal. Avec ce programme, vous pouvez envoyer un message à un seul numéro ou à plusieurs numéros en même temps


## Pre-requis

- Python version 3
- Un numéro Twilio
- Minimum connaissance en python

## Installation 

```git clone https://github.com/makan-dianka/sms.git```

```cd sms```

### Créer & activer l'environnement virtuelle

```python -m venv venv```

pour activer l'environnement virtuelle taper :

```. venv/bin/activate``` si vous êtes linux

```\venv\scripts\activate``` si vous êtes sur windows


## Installations de dependances


```pip install --upgrade pip```


```pip install -r requirements.txt```

## Fichier .env

créer un fichier ```.env``` et mettre les variables suivantes

```
ACCOUNT_SID="votre sid account de twilio"
AUTH_TOKEN="votre auth token de twilio"
NUMBER_1="votre numéro de twilio"
```


### message

créer un fichier ```message.txt``` et y mettre votre message

### csv file

créer un fichier ```target.csv``` et y mettre les numéros de destination de votre message. Le contenu de fichier csv doit être comme ci-après :

Ne remplace pas la première ligne "Country,Name,Number". Remplacer les autres lignes qui sont des numéros fictif
```
Country,Name,Number
France,toto,+33754274418
Italy,kiki,+393200412100
Mali,titi,+22379215461
.....
.....
.....
```


# ça y est, tout est prêt.

executer le fichier ```send_sms.py``` pour envoyer votre message

```python send_sms.py```




