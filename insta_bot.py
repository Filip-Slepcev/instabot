from datetime import datetime
from tokenize import group
from instagrapi import Client
import time
import pytz
import os

timezone = pytz.timezone("Canada/Eastern")
USER_LOGIN = os.environ.get("USER_LOGIN")
USER_PASS = os.environ.get("USER_PASS")

def send_message():
	if(USER_LOGIN and USER_PASS):
		cl = Client()
		cl.login(USER_LOGIN, USER_PASS)
		dm = cl.direct_search("Gorck")
		if(dm):
			groupchat = dm[0]
			cl.direct_send("a", [], [groupchat.id])

while True:
	dt_time = datetime.now(timezone)
	if dt_time.hour == 0 and dt_time.minute == 14:
		send_message()
		time.sleep(60)