# Reddit Scrapping
This utilize the module of beautifulsoup to webscrap the html of reddit to grab the top post of the day, and text-messenging back a specific user daily using PythonAnywhere.

## Getting Started
This project utilized the twilio module so you must have atleast a trial account.

Firstly, you must replace the following variable:
```bash
ACCOUNT_SID = os.environ.get('TWILIO_SID') # Replace with your account ID
AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN') # Replace with your Auth token
```

```bash
messager.message(message=MoTD, number="your number") # Replace the string of Your number with a reciever phonenumber
```
By doing so you are able to run the program without any troubles.

Lastly, if you want to recieve daily messages you will need to create an account on python-anywhere.
https://www.pythonanywhere.com/

Once created you will be require to upload both messenger.py and main.py to the site.

![alt text](https://cdn.discordapp.com/attachments/237942075335639040/840648135911014410/unknown.png)

To setup a daily schedule task to recieve a text, go to the Task tab and fill in the time you want to recieve the message in UTC time and the following command.
```bash
export TWILIO_SID=YOUR TWILIO SID; export TWILIO_AUTH_TOKEN=YOUR TWILIO AUTH TOKEN;python3 main.py
```
