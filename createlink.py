import imaplib
import email
import time
import smtplib
import base64
import requests
import json
#https://myaccount.google.com/lesssecureapps
import urllib.parse
from threading import Thread

from sqlalchemy import create_engine, text,asc
from pythondispatchms import model
from pythondispatchms.model import DBSession
from pythondispatchms.model.tables import EmailData,EmailService,Dedicated,Devices,Calendars,Roles, ListenerFields
import transaction
import os
import pytz
from datetime import datetime
engine = create_engine('mysql://gpscontrol:qazwsxedc@127.0.0.1/dispatch?charset=utf8')
model.init_model(engine)
#select * from listenerfields where listeners_id=80;
url="https://dispatch.dudewhereismy.com.mx/listener/logymex?"
listenerFields = DBSession.query(ListenerFields).filter_by(listeners_id=80).order_by(asc(ListenerFields.field)).all()
for item in listenerFields:
    a=item.field
    a=a.replace("&", "")
    b=item.value
    b = b.replace("&", "").replace("\n","")

    url=url+a+"="+b+"&"
    #print(item.field,item.value)
print(url)


# stomp -H localhost -P 61613 -U dwim -W gpscontrol1

#  Message.post("trafficlistener_" + eachActiveUser['user_name'], 'RELOAD' + "|"+str(sound))
# send /topic/trafficlistener_Monitoristas RELOAD|1
# send /topic/trafficlistener_Stalkers RELOAD|1
# send /topic/trafficlistener_dispatchAdmin RELOAD|2