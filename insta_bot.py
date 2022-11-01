from datetime import datetime
from tokenize import group
from instagrapi import Client
import time
import pytz
import os

timezone = pytz.timezone("Canada/Eastern")
USER_LOGIN = os.environ.get("USER_LOGIN")
USER_PASS = os.environ.get("USER_PASS")
USER_CHAT = os.environ.get("USER_CHAT")
USER_MESSAGE = os.environ.get("USER_MESSAGE")
TIME_HOUR = os.environ.get("TIME_HOUR")
TIME_MIN = os.environ.get("TIME_MIN")


def send_message():
	if(USER_LOGIN and USER_PASS):
		cl = Client()
		cl.login(USER_LOGIN, USER_PASS)
		dm = cl.direct_search(USER_CHAT)
		if(dm):
			groupchat = dm[0]
			cl.direct_send(USER_MESSAGE, [], [groupchat.id])

while True:
	dt_time = datetime.now(timezone)
	if dt_time.hour == TIME_HOUR and dt_time.minute == TIME_MIN:
		send_message()
		time.sleep(60)