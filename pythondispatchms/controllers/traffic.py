# -*- coding: utf-8 -*-
"""Sample controller with all its actions protected."""
from tg import expose, flash,abort,app_globals
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tg import expose,request,redirect,render_template,predicates
from pythondispatchms.lib.base import BaseController
from pythondispatchms.lib.decorators import restErrorHandler
from pythondispatchms.lib.statistics import Statistics
from pythondispatchms.lib.jqgrid import jqgridDataGrabber
from pythondispatchms.model.tables import Traffic, Tickets,Pending,Images,helpComment,imeiTicket,EmailData,Events,OperatorLog,Dedicated,Roles
from pythondispatchms.model.auth import User
from pythondispatchms.model import DBSession
from pythondispatchms.lib.utililty import URLunicode
from pythondispatchms.lib.rest import Rest
from pythondispatchms.lib.messagequeue import Message
from math import cos

from tg import app_globals
from base64 import b64encode
import requests
import json
import datetime
from datetime import time
import enchant
from shutil import copyfileobj
import os
import socket
import urllib.parse
import arrow
from sqlalchemy import asc, desc, text, or_, and_
import pygal
import qrcode
import qrcode.image.svg
from io import BytesIO

__all__ = ['TrafficController']

class getTracker():
    def __init__(self):
        pass
    @classmethod
    def location(cls, **kw):
        heading = "0"
        speed = "0"
        latitude = "0"
        longitude = "0"
        if 'imei' in kw:
            pluto = Rest()
            imei=kw['imei']
            parameters = {}
            parameters['imei'] = imei
            imeiData = pluto.get(app_globals.domainpluto + "/services/imeiInfo", parameters)
            if 'error' in imeiData:
                if imeiData['error']=="notFound":
                    return dict(latitude=latitude,longitude=longitude,speed=speed,heading=heading)
                else:
                    if 'server' in imeiData:
                        if imeiData['server']==1:
                            r = requests.get("http://server1.gpscontrol.com.mx/webservice/api/location/getbyimei?imei=" + imei,
                                             auth=('lusa', '1234'))
                            json_object = r.json()
                            if len(json_object) > 0:
                                latitude = json_object[0]['latitude']
                                longitude = json_object[0]['longitude']
                                heading = json_object[0]['heading']
                                return dict(latitude=str(latitude), longitude=str(longitude), speed=speed, heading=str(heading))
                        elif imeiData['server']==2:
                            r = requests.get(
                                "http://server2.gpscontrol.com.mx/webservice/api/location/getbyimei?imei=" + imei,
                                auth=('lusa', '1234'))
                            json_object = r.json()
                            if len(json_object) > 0:
                                latitude = json_object[0]['latitude']
                                longitude = json_object[0]['longitude']
                                heading = json_object[0]['heading']
                                return dict(latitude=str(latitude), longitude=str(longitude), speed=speed,
                                            heading=str(heading))
                        elif imeiData['server']==3:
                            r = requests.get("http://plataforma3.gpscontrol.com.mx/ms03/location/" + imei,
                                             auth=('ms03', 'qazwsxedc'))
                            json_object = r.json()
                            if len(json_object) > 0:
                                latitude = json_object[0]['latitude']
                                longitude = json_object[0]['longitude']
                                speed = json_object[0]['speed']
                                heading = json_object[0]['azimut']

        return dict(latitude=str(latitude), longitude=str(longitude), speed=str(speed), heading=str(heading))


class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

class TrafficController(BaseController):

    #allow_only = predicates.not_anonymous()
    @expose()
    def check(self):
        return "UP"


    @expose('pythondispatchms.templates.traffic.traffic')
    def index(self, **kw):
        if not "user" in kw:
            abort(status_code=500, detail="Traffic error, parameter (user) not found")
        else:
            gaugeParameters = Statistics()
        currentGauge=gaugeParameters.byUser(kw["groups"])
        currentComments = []
        all = DBSession.query(helpComment).all()
        for item in all:
            currentComments.append(dict(id=item.id, hcomment=item.comment))
        currentGauge["group"]=kw["groups"]
        currentGauge["user"] = kw["user"]
        currentGauge["list"]=currentComments

        if 'application_id' in kw:
            r=requests.get('https://sun.dudewhereismy.com.mx/services/utc_zone?application_id='+kw["application_id"])
            parameters = {}
            parameters["application_id"] = kw["application_id"]
            newSession = requests.session()
            mkw = {'params': parameters,'verify': False, 'timeout': 10}
            response = newSession.get('https://sun.dudewhereismy.com.mx/services/utc_zone', **mkw)
            values = response.json()
            if "error" in values:
                if values['error']=='ok':
                    currentGauge["tz"] =values["utc_zone"]
                    #print("TZ:{}".format(currentGauge["tz"]))
                else:
                    currentGauge["tz"] = "America/Mexico_City"

        else:
            currentGauge["tz"] = "America/Mexico_City"
        #for k,v in kw.items():
        #    print("{} {}".format(k,v))
        #print("**************> GROUPS:{}".format(kw['groups']))
        return currentGauge

    @expose('json')
    def getGauges(self, **kw):
        gaugeParameters = Statistics()
        currentGauge = gaugeParameters.byUser(kw["group"])
        return currentGauge

    @expose('json')
    def loadTraffic(self, **kw):
        # for k,v in kw.items():
        #     print("{} {}".format(k,v))
        # group ManagerGPS,Monitoristas
        print(kw["group"])
        filter  = [('only', 'eq', 1),('attended_state', 'ne', 'C'),('attended_state', 'ne', 'R'),('user','in',kw["group"])]
        return jqgridDataGrabber(Traffic, 'id', filter, kw).loadGrid()

    @expose('json')
    def updateTraffic(self, **kw):
        filter = ['attended_state', 'bn', 'C']
        return jqgridDataGrabber(Traffic, 'id', filter, kw).updateGrid()

    @expose('json')
    def updateTrafficStatus(self, **kw):
        traffic_id = kw['traffic_id']
        state = kw['state']
        comment = kw['comment']
        if kw['false_alarm'] == "true":
            false_alarm = 1
        else:
            false_alarm = 0
        alert = DBSession.query(Traffic).filter_by(id=traffic_id).first()
        if alert is not None:
            alert.attended_state = state
            alert.comment = comment
            alert.false_alarm = false_alarm
            if state == "A":
                alert.attended_time = datetime.datetime.utcnow()
            if state == "P":
                OperatorLog.addLog(user_name=kw["user"], group_name=kw["group"], operation=app_globals.putPending,
                                   traffic_id=traffic_id)
                alert.pending_time = datetime.datetime.utcnow()
            if state == "C":
                OperatorLog.addLog(user_name=kw["user"], group_name=kw["group"], operation=app_globals.finalizedTraffic,
                                   traffic_id=traffic_id)
                alert.closed_time = datetime.datetime.utcnow()
            DBSession.flush()
        else:
            print("NOT FOUND!!!")
        if not "group" in kw:
            abort(status_code=500, detail="Traffic error, parameter (group) not found")
        else:
            gaugeParameters = Statistics()
            currentGauge=gaugeParameters.byUser(kw["group"])
        Message.post("trafficlistener_" + kw["group"], 'REPAINT' + "|")
        return currentGauge

    @expose('json')
    def getOperatorLog(self, **kw):
        localtz = kw['tz']
        operatorlog = []
        operlog = DBSession.query(OperatorLog).filter_by(traffic_id=kw['traffic_id']).order_by(asc(OperatorLog.time_stamp)).all()
        for operitem in operlog:
            oper_utc = arrow.get(operitem.time_stamp)
            oper_localtime = oper_utc.to(localtz)
            cabus=""
            if len(operitem.ticket)>1:
                cabus=":" +operitem.ticket
            operatorlog.append(str(oper_localtime) + ":" + operitem.user_name + ":" + operitem.group_name + ":" +
                               app_globals.trafficOperation[operitem.operation]+cabus)

        return dict(operatorlog=operatorlog)

    @expose('json')
    def getRecord(self, **kw):

        if "state" in kw:
            if kw["state"]=="open":
                OperatorLog.addLog(user_name=kw["user"],group_name=kw["group"],operation=app_globals.viewTrafficData,traffic_id=kw['record'])
        callerEventState = "Y"
        # group = DBSession.query(ListenerUsers).filter_by(user_name=kw["group"]).first()
        # if group is not None:
        #     if group.callerevent == 1:
        #         callerEventState = "Y"
        if 'tz' in kw:
            localtz=kw['tz']
        else:
            localtz="America/Mexico_City"
        comment = ""
        callercomment = ""
        false_alarm = ""

        record = kw['record']
        pendinghistory=""
        traffic = DBSession.query(Traffic).filter_by(id=record).first()
        if traffic is not None:
            operatorlog=[]
            operlog=DBSession.query(OperatorLog).filter_by(traffic_id=record).order_by(asc(OperatorLog.time_stamp)).all()
            for operitem in operlog:
                oper_utc=arrow.get(operitem.time_stamp)
                oper_localtime = oper_utc.to(localtz)
                operatorlog.append(str(oper_localtime)+":"+operitem.user_name+":"+operitem.group_name+":"+app_globals.trafficOperation[operitem.operation])

            pendingarray=[]
            pending= DBSession.query(Pending).filter_by(traffic_id=record).all()
            for items in pending:
                utc = arrow.get(items.pending_date)
                localtime = utc.to(localtz)
                pendingarray.append(localtime)
                pendingarray.append(items.data)
            pendinghistory = render_template({"pending": pendingarray,"operatorlog": operatorlog}, "mako", 'pythondispatchms.templates.traffic.pending')
            #print("Pending:{}".format(pendinghistory))
            comment = traffic.comment
            callercomment = traffic.callercomment
            if (traffic.false_alarm == 1):
                false_alarm = "true"
            else:
                false_alarm = "false"
        imei = traffic.imei
        latitude = traffic.latitude
        longitude = traffic.longitude
        cell_lat = 0
        cell_lon = 0
        icc=""
        if traffic.cellid>0:
            parameters = {}
            parameters["key"] = app_globals.opencellkey
            parameters['mcc'] = str(traffic.mcc)
            parameters['mnc'] = str(traffic.mnc)
            parameters['lac'] = str(traffic.lac)
            parameters['cellid'] = str(traffic.cellid)
            parameters["format"] = "json"
            newSession = requests.session()
            mkw = {'params': parameters,'verify': False, 'timeout': 10}
            response = newSession.get(app_globals.opencell, **mkw)
            values = response.json()
            if "lat" in values:
                cell_lat=values["lat"]
                cell_lon=values["lon"]
                print("latitude:{}".format(latitude))

        plates=''

        imeiInfo=Rest()
        imeiData=imeiInfo.get(app_globals.domainpluto+"/services/imeiInfo", {"imei":imei})
        if imeiData["error"]=="ok":
            #print("IMEI:"+imei)
            icc=imeiData["ccid"]
            list = []
            plates=imeiData["plates"]
            list.append(dict(left=_('IMEI') + ":", right=traffic.imei, id="im"))
            list.append(dict(left=_('Brand') + ":", right=imeiData["brand"], id="br"))
            list.append(dict(left=_('Model') + ":", right=imeiData["model"], id="mo"))
            list.append(dict(left=_('Year') + ":", right=imeiData["year"], id="ye"))
            list.append(dict(left=_('Color') + ":", right=imeiData["color"], id="co"))
            list.append(dict(left=_('Plates') + ":", right=imeiData["plates"], id="pl"))
            list.append(dict(left=_('Vin') + ":", right=imeiData["vin"], id="vi"))
            list.append(dict(left=_('CCID') + ": ", right=imeiData["ccid"], id="cc"))
            list.append(dict(left=_('Phone') + ": ", right=imeiData["phone"], id="ph"))
            list.append(dict(left=_('Eco') + ":", right=imeiData["eco"], id="ec"))
            vehicle = render_template({"list": list}, "mako", 'pythondispatchms.templates.traffic.eventdata')

            serverlink = ''
            if imeiData["server"] == 1:
                serverlink = 'http://server1.gpscontrol.com.mx/GPSControl/index.aspx?username=' + str(
                    imeiData["user"]) + '&password=' + str(imeiData["password"])
            if imeiData["server"] == 2:
                serverlink = 'http://server2.gpscontrol.com.mx/GPSControl/index.aspx?username=' + str(
                    imeiData["user"]) + '&password=' + str(imeiData["password"])
            if imeiData["server"] == 3:
                serverlink = 'http://plataforma3.gpscontrol.com.mx/loginV2.aspx?user=' + str(
                    imeiData["user"]) + '&password=' + str(imeiData["password"])
            platform = '<a href="' + serverlink + '" style="color: #0000EE" target = "_new">Plataform Access</a>'
            #print("platform:"+platform)
            utf8 = URLunicode()
            cc={"id":imeiData["client_id"],"enterprise":imeiData["application"],"rfc":imeiData["rfc"],"folio_sin_nube":imeiData["folio_sinube"],"address":utf8.decode(imeiData["address"]),"exp_date":imeiData["expires"],"created":imeiData["created"],"device":imeiData["device"],"state":imeiData["state"],"phone":imeiData["phone"]}
            list=[]
            list.append(dict(left=_('Client ID') + ":", right=cc["id"]))
            list.append(dict(left=_('Enterprise') + ":", right=cc["enterprise"]))
            list.append(dict(left=_('RFC') + ":", right=cc["rfc"]))
            list.append(dict(left=_('Folio sin nube') + ":", right=cc["folio_sin_nube"]))
            list.append(dict(left=_('Address') + ":", right=cc["address"]))
            list.append(dict(left=_('Expiration Date') + ":", right=cc["exp_date"]))
            list.append(dict(left=_('Created') + ":", right=cc["created"]))
            list.append(dict(left=_('Device') + ":", right=cc["device"]))
            list.append(dict(left=_('State') + ":", right=cc["state"]))
            list.append(dict(left=_('Phone') + ":", right=cc["phone"]))


            account = render_template({"list": list}, "mako", 'pythondispatchms.templates.traffic.account')

            spunit = ''
            if traffic.speedunit is not None:
                spunit = traffic.speedunit
            list = []

            list.append(dict(left=_('Time Stamp') + ":", right=str(traffic.time_stamp), id="ts"))
            list.append(dict(left=_('Event Id') + ":", right=traffic.event_id, id="ei"))
            list.append(dict(left=_('Description') + ":", right=utf8.decode(traffic.event_desc), id="de"))
            list.append(dict(left=_('Priority') + ":", right=traffic.priority, id="pr"))
            list.append(dict(left=_('Speed') + ":", right=str(traffic.speed) + " " + spunit, id="sp"))
            list.append(dict(left=_('Azimuth') + ":", right=traffic.azimuth, id="az"))
            list.append(dict(left=_('Vehicle') + ":", right=traffic.vehicle, id="ve"))
            list.append(dict(left=_('Event Time') + ":", right=str(traffic.event_time), id="et"))

            if traffic.dedicated_id!=0:
                ded = DBSession.query(Dedicated).filter_by(id=traffic.dedicated_id).first()
                if ded is not None:
                    for dev_ele in ded.devices:
                        print("imei:{}".format(dev_ele.imei))
                        if traffic.imei==dev_ele.imei:
                            print("bingo!!")
                            list.append(dict(left=_('Conductor') + ":", right=str(dev_ele.driver_name), id="et"))
                            list.append(dict(left=_('Password') + ":", right=str(dev_ele.password), id="et"))
                            list.append(dict(left=_('Tel1') + ":", right=str(dev_ele.phone1), id="et"))
                            list.append(dict(left=_('Tel2') + ":", right=str(dev_ele.phone2), id="et"))
                            list.append(dict(left=_('Tel3') + ":", right=str(dev_ele.phone3), id="et"))
                            list.append(dict(left=_('Obs') + ":", right=str(dev_ele.obs), id="et"))

            if callercomment != "":
                list.append(dict(left=_('Comment') + ":", right=callercomment, id="cc"))
            searchticket = DBSession.query(Tickets).filter_by(traffic_id=traffic.id).all()
            for item in searchticket:
                list.append(dict(left=_('Venus ticket') + ":", right="(" + str(item.ticket) + ") ----> " + str(
                    item.last_report) + " " + str(item.comment), id="cc"))
            searchpending = DBSession.query(Pending).filter_by(traffic_id=traffic.id).all()
            for item in searchpending:
                list.append(dict(left=_('Pending') + ":",
                                 right=str(item.pending_date.strftime('%Y/%m/%d %H:%M:%S')) + " (" +
                                     item.data + ")", id="cc"))

            searchticket = DBSession.query(Images).filter_by(traffic_id=traffic.id).all()
            imagelist = []
            for item in searchticket:
                image = item.data
                encoded_string = str(b64encode(image),'utf-8')
                imagelist.append(encoded_string)

            images = render_template({"list": imagelist}, "mako", 'pythondispatchms.templates.traffic.images')
            query = DBSession.query(EmailData).filter_by(imei=imei,time_stamp=traffic.event_time).first()
            if query is not None:
                images = query.data

            ts = str(traffic.time_stamp)
            et = str(traffic.event_time)
            event = render_template({"list": list}, "mako", 'pythondispatchms.templates.traffic.eventdata')

            list = []
            contactInfo = Rest()
            contactsList = imeiData["contacts"]

            for eachContact in contactsList:
                list.append(dict(name=eachContact["contact_name"], email=eachContact["contact_email"], phone1=eachContact["phone_one"],
                                 phone2=eachContact["phone_two"], phone3=eachContact["phone_tree"]))

            callerlist = render_template({"list": list}, "mako", 'pythondispatchms.templates.traffic.callerlist')
            list = []
            list.append(dict(event=""))
            history = DBSession.query(Traffic).filter_by(imei=traffic.imei).all()
            for e in history:
                utf8 = URLunicode()
                if e.event_desc is None:
                    ed = utf8.decode(str(e.event_desc))
                else:
                    ed = utf8.decode(e.event_desc)
                utc = arrow.get(e.time_stamp)
                localtime = utc.to(localtz)
                list.append(dict(
                    event="a las: " + str(localtime) + " Cliente " + e.user_name + " Evento " + str(e.event_id) + " " + ed + " Vehiculo " + e.vehicle))
            accounthistory = render_template({"list": list}, "mako", 'pythondispatchms.templates.traffic.history')

        else:
            images = ""
            query = DBSession.query(EmailData).filter_by(imei=imei,time_stamp=traffic.event_time).first()
            if query is not None:
                images = query.data

            list = []
            ts=""
            et=""
            list.append(dict(left="Data not found", right="IMEI " + traffic.imei + " not found"))
            account = render_template({"list": list}, "mako", 'pythondispatchms.templates.traffic.account')
            list = []
            utf8 = URLunicode()

            list.append(dict(left=_('Time Stamp') + ":", right=str(traffic.time_stamp), id=""))
            list.append(dict(left=_('Event Id') + ":", right=traffic.event_id, id=""))
            list.append(dict(left=_('Description') + ":", right=utf8.decode(traffic.event_desc), id=""))
            list.append(dict(left=_('Priority') + ":", right=traffic.priority, id=""))
            list.append(dict(left=_('Speed') + ":", right=traffic.speed, id=""))
            list.append(dict(left=_('Azimuth') + ":", right=traffic.azimuth, id=""))
            list.append(dict(left=_('Vehicle') + ":", right=traffic.vehicle, id=""))
            list.append(dict(left=_('Event Time') + ":", right=str(traffic.event_time), id=""))

            searchpending = DBSession.query(Pending).filter_by(traffic_id=traffic.id).all()
            for item in searchpending:
                utc = arrow.get(item.pending_date)
                localtime = utc.to(localtz)
                list.append(dict(left=_('Pending') + ":",
                                 right=str(localtime.strftime('%Y/%m/%d %H:%M:%S')) + " (" +
                                     item.data + ")", id="cc"))
            event = render_template({"list": list}, "mako", 'pythondispatchms.templates.traffic.eventdata')
            list = []
            list.append(dict(left=_('IMEI') + ":", right=traffic.imei, id=""))
            vehicle = render_template({"list": list}, "mako", 'pythondispatchms.templates.traffic.eventdata')
            list = []
            list.append(dict(name="", email="", phone1="", phone2="", phone3=""))
            callerlist = render_template({"list": list}, "mako", 'pythondispatchms.templates.traffic.callerlist')
            list = []
            list.append(dict(event=""))
            accounthistory = render_template({"list": list}, "mako", 'pythondispatchms.templates.traffic.history')
            list = []
            list.append(dict(event=""))
            platform = ""

        # Search newest instala
        link = 'http://dispatch.dwim.mx/traffic/noreport'
        urllink = "http://instala.dwim.mx/getuuidbyimei/" + imei
        #print("URL:{}".format(urllink))


        try:
            resp = requests.get(urllink)
        except MyError as e:
            pass
        else:
            ans = resp.text
            ans = ans.replace("[", "").replace("]", "")
            jsonanswer = json.loads(ans)
            if jsonanswer['Error'] == u'none':
                uuid = jsonanswer['uuid']
                link = "http://instala.dwim.mx/printinstallpdf/" + uuid
            else:
                # search oldest instala
                pass
                urllink = "http://ci.dwim.mx/getuuidbyimei/" + imei
                try:
                    resp = requests.get(urllink)
                except MyError as e:
                    pass
                else:
                    ans = resp.text
                    ans = ans.replace("[", "").replace("]", "")
                    jsonanswer = json.loads(ans)
                    if jsonanswer['Error'] == u'none':
                        uuid = jsonanswer['uuid']
                        link = "http://ci.dwim.mx/printinstallpdf/" + uuid
                    else:
                        link = "dontHave"



        return dict(account=account, event=event, callerlist=callerlist, accounthistory=accounthistory,
                    latitude=latitude, longitude=longitude, comment=comment, false_alarm=false_alarm,
                    attended_state=traffic.attended_state, link=link, vehicle=vehicle, platform=platform, ts=ts, et=et,
                    images=images, callerEventState=callerEventState,plates=plates,cell_lat=cell_lat,cell_lon=cell_lon,icc=icc,pendinghistory=pendinghistory)

    @expose('pythondispatchms.templates.traffic.noreport')
    def noreport(self, **kw):
        return dict(dummy="")

    @expose('json')
    def spellChecker(self, **kw):
        #print("Spell Checker")
        wordCount = 0
        text = kw['text']
        esp = enchant.Dict("es")
        error = "nok"
        words = text.split(" ")
        for word in words:
            if word != "":
                if esp.check(word):
                    wordCount = wordCount + 1
        if wordCount > 9:
            error = "ok"
        else:
            error = "Palabras reconocidas: " + str(wordCount)
        #print("Palabras:{}".format(str(wordCount)))
        return dict(error=error, words=wordCount)

    @expose('json')
    def addPending(self, **kw):
        traffic_id = int(kw['traffic_id'])
        #OperatorLog.addLog(user_name=kw["user"], group_name=kw["group"], operation=app_globals.putPending, traffic_id=traffic_id)
        newPending = Pending()
        newPending.traffic_id = traffic_id
        # newPending.pending_date = datetime.datetime.utcnow()
        newPending.data = kw['comment']
        DBSession.add(newPending)
        DBSession.flush()
        Message.post("trafficlistener_" + kw["group"], 'RELOAD' + "|")
        return dict(error='ok')

    @expose('json')
    def uploadImage(self,**kw):
        if "userfile" in kw:
            fileitem = kw["userfile"]
            if fileitem.file:
                fileName = fileitem.filename
                if fileName.find(".png") > 0 or fileName.find(".jpeg") > 0 or fileName.find(".jpg") > 0:
                    newImage = Images()
                    newImage.traffic_id = kw["traffic_id"]
                    newImage.data = fileitem.file.read()
                    DBSession.add(newImage)
                    DBSession.flush()
                    OperatorLog.addLog(user_name=kw["user"], group_name=kw["group"], operation=app_globals.addImage,traffic_id=kw['traffic_id'])
        return dict(dummy="")

    @expose('json')
    def uploadImage2(self, **kw):
        if 'traffic_id' in kw:
            traffic_id = int(kw['traffic_id'])
            file = request.POST['file']
            if file != '':
                # permanent_file = open(os.path.join('/var/www/python.dispatch', file.filename.lstrip(os.sep)), 'w')
                #print(app_globals.app_dir)
                permanent_file = open(os.path.join(app_globals.app_dir+'/', file.filename.lstrip(os.sep)), 'wb')
                copyfileobj(file.file, permanent_file)
                file.file.close()
                permanent_file.close()
                filename = request.params["file"].filename
                (this_file_name, this_file_extension) = os.path.splitext(filename)
                # format=imghdr.what(filename)
                # if format=='jpeg'or format=='bmp' or format=='png':
                if (this_file_extension == '.jpeg' or this_file_extension == '.bmp' or this_file_extension == '.png'):
                    # f = open('/var/www/python.dispatch/' + filename, 'rb').read()
                    f = open(app_globals.app_dir+'/' + filename, 'rb').read()
                    newImage = Images()
                    newImage.traffic_id = traffic_id
                    newImage.data = f
                    DBSession.add(newImage)
                    DBSession.flush()
        redirect("/index")

    @expose('json')
    def addTicket(self, **kw):
        traffic_id = int(kw['traffic_id'])
        comment = kw['comment']
        OperatorLog.addLog(user_name=kw["user"], group_name=kw["group"], operation=app_globals.createTicket,traffic_id=traffic_id)
        ticket = DBSession.query(Traffic).filter_by(id=traffic_id).first()
        if traffic_id != 0:
            kw['imei'] = ticket.imei
        if kw['imei'] is not None:
            imeiInfo = Rest()
            imeiData = imeiInfo.get(app_globals.domainpluto + "/services/imeiInfo", {"imei": kw['imei']})
            if imeiData["error"] == "ok":
                #print("IMEI:"+kw['imei'])
                client_id = imeiData["client_id"]
                if client_id is not None:
                    last_report = imeiData["last_report"]
                    url = "http://venus.gpscontrol.com.mx/dispatch/create_ticket?client_id=" + str(
                        client_id) + "&last_report=" + str(last_report) + "&folio=" + str(kw['traffic_id']) + "&imei=" + str(
                        kw['imei']) + "&comm=" + urllib.parse.quote_plus(comment)
                    print("URL:{}".format(url))
                    newTicket = Rest()
                    #print("URL:{}".format(url))
                    ticketData = newTicket.get(url, {})
                    #print("data:{}".format(ticketData))
                    ## Insert if error="ok"
                    #response = requests.get(url)
                    #print("Response:{}".format(ticketData))
                    iticket = ticketData['Ticket']
                    searchticket = DBSession.query(Tickets).filter_by(ticket=iticket).first()
                    if searchticket is None:
                        newTickets = Tickets()
                        if id != 0:
                            newTickets.traffic_id = id
                        newTickets.last_report = last_report
                        newTickets.ticket = iticket
                        newTickets.comment = kw['comment']
                        DBSession.add(newTickets)
                        DBSession.flush()
                        try:
                            newTickets = DBSession.query(imeiTicket).filter_by(imei=kw['imei']).one()
                            newTickets.imei = kw['imei']
                            newTickets.ticket = iticket
                        except:
                            newTickets = imeiTicket()
                            newTickets.imei = kw['imei']
                            newTickets.ticket = iticket
                            DBSession.add(newTickets)
                        DBSession.flush()
                    return ticketData
        else:
            return dict(Ticket=0)

    @expose('json')
    def send2C5(self, **kw):
        vehicle = "Prueba "+kw['vehicle']
        print("vehicle:{}".format(vehicle))
        imei = kw['imei']
        print("IMEI:{}".format(imei))
        plates= kw['plates']
        print("Plates:{}".format(plates))
        position=getTracker.location(imei=kw['imei'])
        latitude= position['latitude']
        print("Latitude:{}".format(latitude))
        longitude= position['longitude']
        print("Longitude:{}".format(longitude))
        speed= position['speed']
        heading = position['heading']
        print("Heading:{}".format(heading))
        print("latitude:{}".format(position['latitude']))
        separator=chr(9)
        ip="0"
        utcnow = datetime.datetime.utcnow()
        midnight_utc = datetime.datetime.combine(utcnow.date(), time(0))
        delta = utcnow - midnight_utc
        seconds=str(int(float(delta.seconds)))
        valid="1"
        status="1"
        prepayload="P"+separator+\
                   vehicle+separator+\
                   ip+separator+\
                   imei+separator+\
                   plates+separator+\
                   seconds+separator+\
                   latitude+separator+\
                   longitude+separator+\
                   speed+separator+\
                   heading+separator+\
                   valid+separator+\
                   status
        heading=format(len(prepayload), '02x')
        heading=heading.zfill(8).upper()
        payload=heading+prepayload
        #print("Payload:{}".format(payload))
        #print(payload.count(chr(9)))
        host = "138.68.54.137"
        #host = "201.144.252.139"
        port = 4105
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.send(payload.encode())
        data = b''
        s.settimeout(5.0)
        ticket = ""
        try:
            bytes = s.recv(1042)
        except Exception as e:
            ticket = "Error C5 Rechazo la alerta"
        else:
            print(bytes)
            raw_header = bytes.decode("utf-8")
            hex_header = "0x" + raw_header.lstrip("0")
            header_lenght = int(hex_header, 16)
            print("header length:{}".format(header_lenght))
            count = 0
            while True:
                try:
                    packet = s.recv(1)
                except:
                    break
                data += packet
                count += 1
                # print("count:{} data:{}".format(count,data))
                if count > header_lenght:
                    break
            sdata = data.decode("utf-8")
            position = sdata.rfind("\t")
            position += 1
            # print("position:{}".format(position))
            ticket = sdata[position:]
        s.close()
        print("Ticket:{}".format(ticket))
        OperatorLog.addLog(user_name=kw["user"], group_name=kw["group"], operation=app_globals.telefonicaLocation,
                           traffic_id=kw['traffic_id'],ticket=ticket)
        ticket=ticket[:14]
        return dict(Ticket=ticket)

    #
    @expose('json')
    def loadCallerEvent(self, **kw):
        rows = []
        recordcount = 0
        total = 1
        parameters = {}
        if 'filters' in kw:
            filters=eval(kw['filters'])
            for item in filters["rules"]:
                field=item["field"]
                data=item["data"]
                parameters[field] = data
        pluto=Rest()

        carsData = pluto.post(app_globals.domainpluto + "/services/findCars", parameters)

        if 'cars' in carsData:
            for item in carsData["cars"]:
                cell = []
                cell.append(item['id'])
                cell.append(item['status'])
                cell.append(item['imei'])
                cell.append(item['ccid'])
                cell.append(item['phone'])
                cell.append(item['last_report'])
                cell.append(item['device'])
                cell.append(item['eco'])
                cell.append(item['brand'])
                cell.append(item['model'])
                cell.append(item['year'])
                cell.append(item['color'])
                cell.append(item['plates'])
                cell.append(item['vin'])
                cell.append(item['user'])
                cell.append(item['password'])
                cell.append(item['client_id'])
                cell.append(item['server'])
                cell.append(item['internal_id'])
                recordcount=recordcount+1
                rows.append({"cell": cell})
             #rows = sorted(rows, key=lambda k: k['username'])
        expression=dict(records=recordcount,total=total,rows=rows)
        return expression


    @expose('json')
    def updateCallerEvent(self, **kw):
        return dict(rows=[])

    @expose('json')
    def getDynamicTemplate(self, **kw):
        list=[]
        #listener=kw['listener']
        currentevent = DBSession.query(Events).all()
        for element in currentevent:
            list.append({"FIELD1": element.event_id, "FIELD2": element.event_desc})

        eventtemplate = render_template({"list": list}, "mako", 'pythondispatchms.templates.traffic.eventstemplate')
        return dict(eventtemplate=eventtemplate)

    @expose('json')
    def addTraffic(self, **kw):
        event_id = int(kw['event_id'])
        imei = kw['imei']
        vehicle = kw['vehicle']
        comment = kw['comment']
        listener = 0
        position = getTracker.location(imei=imei)
        latitude = position['latitude']
        print("Latitude:{}".format(latitude))
        longitude = position['longitude']
        print("Longitude:{}".format(longitude))
        speed = position['speed']
        azimuth = position['heading']

        priority = int(kw['priority'])
        if kw['client_id'] == "None":
            client_id = -1
            user_name = "Inexistente=CLIENT_ID=none"
        else:
            parameters = {}
            parameters['imei'] = imei
            connection = requests.get(app_globals.domainpluto + "/services/imeiInfo", parameters)
            imeiData = connection.json()
            if imeiData["error"] == "ok":
                user_name=imeiData["application"]
            else:
                user_name="Inexistente=CLIENT_ID=none"

        currentEvent = DBSession.query(Events).filter_by(event_id=event_id).first()
        if currentEvent is not None:
            nd = currentEvent.event_desc
        else:
            nd = ""

        user = request.identity['repoze.who.userid']
        user = DBSession.query(User).filter_by(user_name=user).first()
        newTraffic = Traffic()
        newTraffic.priority = priority
        newTraffic.event_id = event_id
        newTraffic.user_name = user_name
        newTraffic.imei = imei
        newTraffic.vehicle = vehicle
        newTraffic.callercomment = comment
        newTraffic.event_desc = nd
        newTraffic.latitude = latitude
        newTraffic.longitude = longitude
        newTraffic.azimuth = int(float(azimuth))
        newTraffic.speed = int(float(speed))
        newTraffic.listener = listener
        newTraffic.attended_state = 'A'
        newTraffic.user_id = user.user_id
        newTraffic.user=kw["group"]
        DBSession.add(newTraffic)
        DBSession.flush()


        Message.post("trafficlistener_" + kw["group"], 'RELOAD' + "|")
        return dict(error="ok", id=str(newTraffic.id))

    @expose('json')
    def getPlataformPosition(self, **kw):
        OperatorLog.addLog(user_name=kw["user"], group_name=kw["group"], operation=app_globals.telefonicaLocation,
                           traffic_id=kw['traffic_id'])
        traffic_id=kw['traffic_id']
        error = "No puedo conectar con plataforma"
        position = DBSession.query(Traffic).filter_by(id=traffic_id).first()
        if position is not None:
            print("IMEI:{}".format(position.imei))
            pluto = Rest()
            parameters = {}
            parameters['imei'] = position.imei
            imei=position.imei
            imeiData = pluto.get(app_globals.domainpluto + "/services/imeiInfo", parameters)
            latitude='0'
            if 'server' in imeiData:
                if imeiData['server'] == 1:
                    r = requests.get("http://server1.gpscontrol.com.mx/webservice/api/location/getbyimei?imei=" + imei,
                                     auth=('lusa', '1234'))
                    json_object = r.json()
                    if len(json_object) > 0:
                        latitude = json_object[0]['latitude']
                        longitude = json_object[0]['longitude']
                        heading = json_object[0]['heading']
                        error='ok'

                elif imeiData['server'] == 2:
                    r = requests.get(
                        "http://server2.gpscontrol.com.mx/webservice/api/location/getbyimei?imei=" + imei,
                        auth=('lusa', '1234'))
                    json_object = r.json()
                    if len(json_object) > 0:
                        latitude = json_object[0]['latitude']
                        longitude = json_object[0]['longitude']
                        heading = json_object[0]['heading']
                        error = 'ok'
                elif imeiData['server'] == 3:
                    r = requests.get("http://plataforma3.gpscontrol.com.mx/ms03/location/" + imei,
                                     auth=('ms03', 'qazwsxedc'))
                    json_object = r.json()
                    if len(json_object) > 0:
                        latitude = json_object[0]['latitude']
                        longitude = json_object[0]['longitude']
                        speed = json_object[0]['speed']
                        heading = json_object[0]['azimut']
                        error = 'ok'

        return dict(error=error, latitude=latitude, longitude=longitude)

    @expose('json')
    def getTelefonicaPosition(self, **kw):
        OperatorLog.addLog(user_name=kw["user"], group_name=kw["group"], operation=app_globals.telefonicaLocation,
                           traffic_id=kw['traffic_id'])
        error="ICC Parameter not passed"
        if 'icc' in kw:
            error="ok"
            url = app_globals.telefonicaPosition + str(kw['icc']) + "/location"
            s = requests.session()
            params = {}
            kw = {'params': params, 'cert': app_globals.cert, 'verify': False, 'timeout': 10}
            response = s.get(url, **kw)
            values = response.json()
            timestamp=''
            if 'ClientException' in values:
                #print("Error:" + values['ClientException']['text'])
                latitude=0
                longitude=0
                error= values['ClientException']['text']
                #print("error:{}".format(error))
            else:
                # locationDetailData: {'automaticLocation': {'coordinates': {'longitude': -98.972992, 'latitude': 19.22096},'timestamp': '2018-07-19T11:54:32Z'}}
                # for k,v in values.items():
                #     print("{}:{}".format(k,v))
                error = "ok"
                latitude = values['locationDetailData']['automaticLocation']['coordinates']['latitude']
                longitude = values['locationDetailData']['automaticLocation']['coordinates']['longitude']
                timestamp =values['locationDetailData']['automaticLocation']['timestamp']
        #print("Error:{}".format(error))
        return dict(error=error,latitude=latitude,longitude=longitude,timestamp=timestamp)


    @expose('pythondispatchms.templates.traffic.finalizedtraffic')
    def finalizedtraffic(self, **kw):
        if 'application_id' in kw:
            r=requests.get('https://sun.dudewhereismy.com.mx/services/utc_zone?application_id='+kw["application_id"])
            parameters = {}
            parameters["application_id"] = kw["application_id"]
            newSession = requests.session()
            mkw = {'params': parameters,'verify': False, 'timeout': 10}
            response = newSession.get('https://sun.dudewhereismy.com.mx/services/utc_zone', **mkw)
            values = response.json()
            if "error" in values:
                mytz = "America/Mexico_City"
                if values['error'] == 'ok':
                    mytz = values["utc_zone"]
        return dict(group=kw["groups"], user=kw["user"],list=[],tz=mytz)
        #return dict(group="Monitoristas", user="monitorista1",list=[])


    @expose('json')
    def loadfinalizedTraffic(self, **kw):
        filter = [('only', 'eq', 1),('attended_state', 'eq', 'C'),('user','eq',kw["group"])]
        return jqgridDataGrabber(Traffic, 'id', filter, kw).loadGrid()

    @expose('pythondispatchms.templates.traffic.rejectedtraffic')
    def rejectedtraffic(self, **kw):
        if 'application_id' in kw:
            r=requests.get('https://sun.dudewhereismy.com.mx/services/utc_zone?application_id='+kw["application_id"])
            parameters = {}
            parameters["application_id"] = kw["application_id"]
            newSession = requests.session()
            mkw = {'params': parameters,'verify': False, 'timeout': 10}
            response = newSession.get('https://sun.dudewhereismy.com.mx/services/utc_zone', **mkw)
            values = response.json()
            mytz = "America/Mexico_City"
            if "error" in values:
                if values['error']=='ok':
                    mytz =values["utc_zone"]
        return dict(group=kw["groups"], user=kw["user"],list=[],tz=mytz)
        #return dict(group="Monitoristas", user="monitorista1",list=[])


    @expose('json')
    def loadrejectedTraffic(self, **kw):
        filter = [('only', 'eq', 1),('attended_state', 'eq', 'R'),('user','eq',kw["group"])]
        return jqgridDataGrabber(Traffic, 'id', filter, kw).loadGrid()


    @expose('pythondispatchms.templates.graphs.monitorStats')
    def monitor(self):
        #          1 --> Look Traffic Detail
        #          2 --> Put Pending
        #          3 --> Create Ticket
        #          4 --> Finalize Traffic
        #          5 --> C5 Alarm
        #          6 --> Add Image
        #          7 --> Telefonica Location
        imageArray=[]
        for operation in range(1,8):
            operation_name=app_globals.trafficOperation[operation]
            line_chart = pygal.HorizontalBar()
            line_chart.title = operation_name
            print("Operation:{}".format(operation_name))
            qry = DBSession.query(OperatorLog).filter(and_(OperatorLog.time_stamp <= '2018-08-30', OperatorLog.time_stamp >= '2018-08-01', OperatorLog.operation == operation)).order_by(asc(OperatorLog.time_stamp)).all()
            index= {}
            for item in qry:
                if item.user_name in index:
                    index[item.user_name]+=1
                else:
                    index[item.user_name]=1
            sort_dic = [(k, index[k]) for k in sorted(index, key=index.get, reverse=True)]

            for key,value in sort_dic:
                print("{}:{}".format(key,value))
                line_chart.add(key, value)
            imageArray.append(line_chart.render_data_uri())
        return dict(graph_data=imageArray)

    @expose('pythondispatchms.templates.graphs.monitor')
    def monitorGraph(self):
        return dict(dummy="")

    @expose('pythondispatchms.templates.graphs.qr')
    def qrGraph(self):
        return dict(dummy="")

    @expose('json')
    def getQRGraphs(self, **kw):
        qr = qrcode.QRCode(
            box_size=int(kw['size']),
            image_factory=qrcode.image.svg.SvgPathImage
        )
        qr.add_data(kw['msg'])
        img = qr.make_image()
        buf = BytesIO()
        img.save(buf)
        image_stream = buf.getvalue()
        return dict(graph_data=image_stream.decode("utf-8") )

    @expose('json')
    def getMonitorGraphs(self, **kw):
        imageArray=[]
        for operation in range(1,8):
            operation_name=app_globals.trafficOperation[operation]
            line_chart = pygal.HorizontalBar()
            line_chart.title = operation_name
            print("Operation:{}".format(operation_name))
            qry = DBSession.query(OperatorLog).filter(and_(OperatorLog.time_stamp <= kw['end'], OperatorLog.time_stamp >= kw['start'], OperatorLog.operation == operation)).order_by(asc(OperatorLog.time_stamp)).all()
            index= {}
            for item in qry:
                if item.user_name in index:
                    index[item.user_name]+=1
                else:
                    index[item.user_name]=1
            sort_dic = [(k, index[k]) for k in sorted(index, key=index.get, reverse=True)]

            for key,value in sort_dic:
                print("{}:{}".format(key,value))
                line_chart.add(key, value)
            imageArray.append(line_chart.render_data_uri())
        print(imageArray[0])
        return dict(graph_data=imageArray)


    @expose('json')
    def checkTraffic(self, **kw):
        #print("user:{}".format(kw['user']))
        # 0 - open
        # 1 - dedicated ok
        # 2 - dedicated nok
        status=2
        query = DBSession.query(Traffic).filter_by(id=kw['traffic_id']).first()
        if query is not None:
            if query.dedicated_id!=0:
                ded=DBSession.query(Dedicated).filter_by(id=query.dedicated_id).first()
                if ded is not None:
                    rol=ded.role
                    ded = DBSession.query(Roles).filter_by(name=rol).first()
                    if ded is not None:
                        for item in ded.users:
                            #print(item.user_name)
                            if item.user_name==kw['user']:
                                #print("bingo!")
                                status=1
            else:
                status=0

        return dict(status=status)