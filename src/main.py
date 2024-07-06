"""This is the file that you have to execute"""
import os
import pywhatkit
from dotenv import load_dotenv

load_dotenv()

msg = os.getenv("msg")
mobileNo = os.getenv("mobileNo")
hour = os.getenv("hour")
minute = os.getenv("minute")
pywhatkit.sendwhatmsg(mobileNo, msg, int(hour), int(minute))
