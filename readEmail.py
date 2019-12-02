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

from sqlalchemy import create_engine, text
from pythondispatchms import model
from pythondispatchms.model import DBSession
from pythondispatchms.model.tables import EmailData,EmailService,Dedicated,Devices,Calendars,Roles
import transaction
import os
import pytz
from datetime import datetime
engine = create_engine('mysql://gpscontrol:qazwsxedc@127.0.0.1/dispatch?charset=utf8')
model.init_model(engine)

def read_email_from_gmail(FROM_EMAIL,FROM_PWD,SMTP_SERVER,SMTP_PORT,imei,url,event_id,event_desc,client_id,client_name,latitude,longitude):

    mail = imaplib.IMAP4_SSL(SMTP_SERVER,SMTP_PORT)
    mail.login(FROM_EMAIL, FROM_PWD)
    mail.select('inbox')

    #
    # ("EMAIL:{} password:{}".format(FROM_EMAIL,FROM_PWD))
    #mail.select(readonly=1)

    typ, data = mail.uid('SEARCH', None, '(UNSEEN)')

    for num in data[0].split():
        typ, data = mail.uid('fetch', num, '(RFC822)')
        for response in data:
            if isinstance(response, tuple):
                original = email.message_from_string(response[1].decode("utf-8") )
                # print(original.keys())
                ['Delivered-To', 'Received', 'X-Received', 'ARC-Seal', 'ARC-Message-Signature', 'ARC-Authentication-Results', 'Return-Path', 'Received', 'Received-SPF', 'Authentication-Results', 'DKIM-Signature', 'X-Google-DKIM-Signature', 'X-Gm-Message-State', 'X-Google-Smtp-Source', 'MIME-Version', 'X-Received', 'Date', 'List-Unsubscribe', 'X-Google-Id', 'X-Feedback-Id', 'X-No-Auto-Attachment', 'Message-ID', 'Subject', 'From', 'To', 'Content-Type']
                #print("original:{}",format(original))
                # print("From:{}".format(original['From']))
                # print("Subject:{}".format(original['Subject']))
                # print("Content:{}".format(original['Content-Type']))
                # print("ID:{}".format(original['Message-ID']))
                imageHtml = ''
                htmlBody ="<p>"
                if original.is_multipart():
                    #print("Multipart!")
                    for part in original.walk():
                        if part.get_content_maintype() == 'multipart':
                            continue
                        if part.get('Content-Disposition') is None:
                            continue
                        filename = part.get_filename()
                        #print("File Name:{}".format(filename))

                        if filename is not None and (filename.find('.jpeg')>0 or filename.find('.png')>0 or filename.find('.jpg')>0):
                            image=part.get_payload(decode=True)
                            bencodedString=base64.b64encode(image)
                            encodedString=bencodedString.decode("utf-8")
                            #print("IMAGE:{}".format(encodedString))
                            fp='<img src="data:image/png;base64, '
                            sp='" alt="Image" />'
                            imageHtml=imageHtml+fp+encodedString+sp
                    for part in original.get_payload():


                        if part.get_content_maintype() == 'text':
                            body = part.get_payload(decode=True)
                            #print("Body:{}".format(repr(body)))
                            #print("Type:{}".format(type (body)))
                            text = body.decode('utf-8','ignore')
                            #print("TEXT:{}".format(text))
                            #if text.find("[<email.message.Message object")<0:
                            for lines in text.split('\r\n'):
                                htmlBody=htmlBody+lines+'<br>'
                            htmlBody=htmlBody+"</p>"
                    utc = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
                    msg=htmlBody + imageHtml
                    query = DBSession.query(EmailData).filter_by(email_id=original['Message-ID']).first()
                    if query is None:
                        newitem = EmailData()
                        newitem.imei = imei
                        newitem.email_id = original['Message-ID']
                        newitem.time_stamp =utc
                        newitem.data = msg
                        DBSession.add(newitem)
                        DBSession.flush()
                        transaction.commit()
                    #url=url+event_desc
                    data = {'client_id': client_id, 'vehicle': client_name,
                            'event_id': event_id, 'event_desc': event_desc,
                            'rdatetime': utc, 'imei': imei,'latitude':str(latitude),'longitude':str(longitude)}
                    #print("URL:{}".format(url+event_desc))
                    #print("Event Desc:{}".format(event_desc))
                    resp = requests.get(url+event_desc, params=data)
                    #print(resp.text)
                else:
                    body = original.get_payload()
                    text = str(body)

                    for lines in text.split('\r\n'):
                        htmlBody = htmlBody + lines + '<br>'
                    htmlBody = htmlBody + "</p>"
                    query = DBSession.query(EmailData).filter_by(email_id=original['Message-ID']).first()
                    if query is None:
                        newitem = EmailData()
                        newitem.imei = imei
                        newitem.email_id = original['Message-ID']
                        newitem.data = htmlBody
                        DBSession.add(newitem)
                        DBSession.flush()
                        transaction.commit()
        mail.store(num, '+FLAGS', '\Seen')
        mail.uid("STORE", num, '+FLAGS', '\Seen')
    mail.close()
    mail.logout()

host_secure = os.getenv('dispatch_SECURE')
if host_secure is None:
    host_secure = "False"
if host_secure == "False":
    host_prefix = "http://"
else:
    host_prefix = "https://"

host_prefix = host_prefix
host = os.getenv('dispatch_HOST')

### Execute
def taskMonitor(i):
    dedicatedServices = DBSession.query(Dedicated).all()
    for item in dedicatedServices:
        if item.state==1:
            # active
            #print("interval:{}".format(item.interval))
            localtz = 'America/Mexico_City'
            cicles=int(60/item.interval)
            for element in item.calendars:
                rolesQuery = DBSession.query(Roles).filter_by(name=item.role).first()
                if rolesQuery is not None:
                    group = rolesQuery.group
                    params = {'group_name': group}
                    groupInfo = requests.get('https://sun.dudewhereismy.mx/services/groupInfo', params=params)
                    sunResponse = groupInfo.json()
                    if 'error' in sunResponse:
                        if sunResponse['error']=="ok":
                            internal_id = sunResponse["internal_id"]
                            params = {'internal_id': internal_id}
                            utcInfo = requests.get('https://sun.dudewhereismy.mx/services/utc_zone', params=params)
                            sunResponse = utcInfo.json()
                            if 'error' in sunResponse:
                                if sunResponse['error'] == "ok":
                                    localtz = sunResponse["utc_zone"]
                local=datetime.now(pytz.timezone(localtz))
                localDate = local.date()
                localHour = local.hour
                localMinute = local.minute
                server=element.day.date()
                if localDate==server:
                    # Today Dedicated Event
                    #print("Fire date:{}".format(server))
                    #print("Local hour At:{}".format(localHour))
                    triggerHour = getattr(element, 'h'+str(localHour))
                    if triggerHour==1:
                        # This is the current hour
                        serverMinute=0
                        for hourCycle in range(0,cicles):
                            #print("Server:{} Local:{}".format(serverMinute,localMinute))
                            if serverMinute==localMinute:
                                ### BINGO
                                #print("Role:{}".format(item.role))
                                query = DBSession.query(Roles).filter_by(name=item.role).first()
                                group = ''
                                if query is not None:
                                    group = query.group
                                #print("Group:{}".format(group))
                                for devices in item.devices:
                                    print(devices.imei)
                                    params = {'imei': devices.imei}
                                    pluto = requests.get('https://pluto.dudewhereismy.com.mx/services/imeiInfo',params=params)
                                    response = pluto.json()
                                    if 'error' in response:
                                        if response['error'] == "ok":
                                            latitude = '0'
                                            longitude = '0'
                                            azimuth = '0'
                                            speed = '0'
                                            if 'server' in response:
                                                if response['server'] == 1:
                                                    r = requests.get(
                                                        "http://server1.gpscontrol.com.mx/webservice/api/location/getbyimei?imei=" + devices.imei,
                                                        auth=('lusa', '1234'))
                                                    json_object = r.json()
                                                    if len(json_object) > 0:
                                                        latitude = json_object[0]['latitude']
                                                        longitude = json_object[0]['longitude']
                                                        azimuth = json_object[0]['heading']
                                                        error = 'ok'

                                                elif response['server'] == 2:
                                                    r = requests.get(
                                                        "http://server2.gpscontrol.com.mx/webservice/api/location/getbyimei?imei=" + devices.imei,
                                                        auth=('lusa', '1234'))
                                                    json_object = r.json()
                                                    if len(json_object) > 0:
                                                        latitude = json_object[0]['latitude']
                                                        longitude = json_object[0]['longitude']
                                                        azimuth = json_object[0]['heading']
                                                        error = 'ok'
                                                elif response['server'] == 3:
                                                    r = requests.get(
                                                        "http://plataforma3.gpscontrol.com.mx/ms03/location/" + devices.imei,
                                                        auth=('ms03', 'qazwsxedc'))
                                                    json_object = r.json()
                                                    if len(json_object) > 0:
                                                        latitude = json_object[0]['latitude']
                                                        longitude = json_object[0]['longitude']
                                                        speed = json_object[0]['speed']
                                                        azimuth = json_object[0]['azimut']
                                                        error = 'ok'
                                            #print("Response:{}".format(response["eco"]))
                                            traffic_url = host_prefix + host + "/addTraffic/"
                                            traffic_params = {'event_id': "99", 'event_desc': 'Monitoreo Dedicado',
                                                              'user_name': response['user'].upper(), 'user': group,
                                                              'vehicle': devices.description}
                                            traffic_params['imei'] = devices.imei
                                            traffic_params['latitude'] = latitude
                                            traffic_params['longitude'] = longitude
                                            traffic_params['azimuth'] = azimuth
                                            traffic_params['speed'] = speed
                                            traffic_params['priority'] = '1'
                                            traffic_params['valid'] = '1'
                                            traffic_params['dedicated_id'] = item.id
                                            traffic = requests.get(traffic_url, params=traffic_params)
                                            traffic_response = traffic.json()
                                            #print(traffic_response)

                            serverMinute=serverMinute+item.interval

def taskEmail(i):
    #print("thread {} start".format(i))
    emailServices=DBSession.query(EmailService).all()
    for everyitem in emailServices:
        # SMTP_SERVER = "imap.gmail.com"
        # SMTP_PORT = 993
        url = host_prefix + host + "/listener/"
        read_email_from_gmail(everyitem.email, everyitem.password, everyitem.smpt_server, everyitem.port,everyitem.imei,url,everyitem.event_id,everyitem.event_desc,everyitem.client_id,everyitem.client_name,everyitem.latitude,everyitem.longitude)
    #print("Thread {} woke up".format(i))



t = Thread(target=taskMonitor, args=(1,))
t.start()
e = Thread(target=taskEmail, args=(2,))
e.start()

# f = Thread(target=taskTraffic, args=(3,))
# f.start()