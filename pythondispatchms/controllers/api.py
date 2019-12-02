# -*- coding: utf-8 -*-
"""Sample controller with all its actions protected."""
from tg import expose, flash
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tg import predicates,app_globals
from pythondispatchms.lib.base import BaseController
from pythondispatchms.model import DBSession
from pythondispatchms.model.tables import Smartphones, Jobs, ReservedImages
from pythondispatchms.lib.messagequeue import Message
from pythondispatchms.lib.jqgrid import jqgridDataGrabber
import requests
import random
import json
import base64
from base64 import b64encode, b64decode
from datetime import datetime
from pyfcm import FCMNotification
from sqlalchemy import func,cast,Date

__all__ = ['ApiController']

import stomp
####

def a2m(x):
    return {
        'Jan': '01',
        'Feb': '02',
        'Mar': '03',
        'Apr': '04',
        'May': '05',
        'Jun': '06',
        'Jul': '07',
        'Aug': '08',
        'Sep': '09',
        'Oct': '10',
        'Nov': '11',
        'Dec': '12',

    }.get(x, '01')

def getJob(ggsdomain,ggs_user,ggs_password,app,job):
    print("Type app:{}".format(type(app)))
    url="http://"+ggsdomain+"/comGpsGate/api/v.1/applications/"+app+"/tokens"
    r=requests.post(url,json={"username":ggs_user,"password":ggs_password})
    j=r.json()
    token=j["token"]
    #print(token)
    url="http://"+ggsdomain+"/comGpsGate/api/v.1/applications/"+app+"/jobs/"+job
    print(url)
    # Read Job Data
    r = requests.get(url,headers={'Authorization': token})
    j=r.json()
    print("JOB data:{}".format(j))
    return j

def updateJob2Dispatched(ggsdomain,ggs_user,ggs_password,app,job,lat,lon):
    currentJob=getJob(ggsdomain,ggs_user,ggs_password,app,job)
    print(currentJob)
    session = requests.Session()
    url = "http://"+ggsdomain+"/comGpsGate/rpc/Directory"
    j = {
        "id": 1,
        "method": "Login",
        "params": {
            "appId": app,
            "bStaySignedIn": True,
            "strPassword": ggs_password,
            "strUserName": ggs_user
        }
    }
    session.post(url, json=j)
    #cookies = session.cookies.get_dict()
    #fransonId = cookies['FransonApplicationID']
    #print(fransonId)
    currentUTCTime = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')+".000Z"
    cmd={
        "id": 7,
        "method": "UpdateJob",
        "params": {
            "appId": app,
            "job": {
                "activatedTime": currentUTCTime,
                "applicationID": app,
                "assignedTime": currentJob["scheduledTime"],
                "assignedWorkerId": currentJob["workerId"],
                "comment": None,
                "commentItems": [],
                "completedTime": None,
                "createdTime": currentJob["scheduledTime"],
                "creatorId": 0,
                "customFields": "[{\"Key\":1,\"Value\":null}]",
                "description": currentJob["description"],
                "id": job,
                "jobDuration": None,
                "jobPoiId": None,
                "jobState": 1,
                "order": 0,
                "routeID": "",
                "scheduledTime": currentJob["scheduledTime"],
                "startLocation": {
                    "address": "Lat: "+str(lat)+" Long:"+str(lon),
                    "administrativeAreaName": None,
                    "categoryID": 0,
                    "cityName": None,
                    "countryName": None,
                    "description": None,
                    "id": "0",
                    "neighborhood": None,
                    "pointOfInterest": None,
                    "position": {
                        "altitude": 0,
                        "is3D": False,
                        "latitude": lat,
                        "longitude": lon
                    },
                    "postalCodeNumber": None,
                    "streetBox": None,
                    "streetName":  None,
                    "streetNumber": None,
                    "subAdministrativeAreaName": None
                },
                "updatedTime": currentUTCTime
            }
        }
    }
    print(json.dumps(cmd, indent=4, sort_keys=True))
    url = "http://"+ggsdomain+"/comGpsGate/rpc/DispatchFuture"
    cmd = session.post(url, json=cmd)
    print(cmd.json())
    return cmd


def updateJob2Active(ggsdomain,ggs_user,ggs_password,app,job,lat,lon):
    currentJob=getJob(ggsdomain,ggs_user,ggs_password,app,job)
    print(currentJob)
    session = requests.Session()
    url = "http://"+ggsdomain+"/comGpsGate/rpc/Directory"
    j = {
        "id": 1,
        "method": "Login",
        "params": {
            "appId": app,
            "bStaySignedIn": True,
            "strPassword": ggs_password,
            "strUserName": ggs_user
        }
    }
    session.post(url, json=j)
    currentUTCTime = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')+".000Z"
    cmd={
        "id": 7,
        "method": "UpdateJob",
        "params": {
            "appId": app,
            "job": {
                "activatedTime": None,
                "applicationID": app,
                "assignedTime": currentJob["scheduledTime"],
                "assignedWorkerId": currentJob["workerId"],
                "comment": None,
                "commentItems": [],
                "completedTime": None,
                "createdTime": currentJob["scheduledTime"],
                "creatorId": 0,
                "customFields": "[{\"Key\":1,\"Value\":null}]",
                "description": currentJob["description"],
                "id": job,
                "jobDuration": None,
                "jobPoiId": None,
                "jobState": 3,
                "order": 0,
                "routeID": "",
                "scheduledTime": currentJob["scheduledTime"],
                "startLocation": {
                    "address": "Lat: "+str(lat)+" Long:"+str(lon),
                    "administrativeAreaName": None,
                    "categoryID": 0,
                    "cityName": None,
                    "countryName": None,
                    "description": None,
                    "id": "0",
                    "neighborhood": None,
                    "pointOfInterest": None,
                    "position": {
                        "altitude": 0,
                        "is3D": False,
                        "latitude": lat,
                        "longitude": lon
                    },
                    "postalCodeNumber": None,
                    "streetBox": None,
                    "streetName":  None,
                    "streetNumber": None,
                    "subAdministrativeAreaName": None
                },
                "updatedTime": currentUTCTime
            }
        }
    }
    print(json.dumps(cmd, indent=4, sort_keys=True))
    url = "http://"+ggsdomain+"/comGpsGate/rpc/DispatchFuture"
    cmd = session.post(url, json=cmd)
    print(cmd.json())
    return cmd


def updateJob2Finished(ggsdomain,ggs_user,ggs_password,app,job,lat,lon,comment):
    currentJob=getJob(ggsdomain,ggs_user,ggs_password,app,job)
    print(currentJob)
    session = requests.Session()
    url = "http://"+ggsdomain+"/comGpsGate/rpc/Directory"
    j = {
        "id": 1,
        "method": "Login",
        "params": {
            "appId": app,
            "bStaySignedIn": True,
            "strPassword": ggs_password,
            "strUserName": ggs_user
        }
    }
    session.post(url, json=j)
    currentUTCTime = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')+".000Z"
    cmd={
        "id": 6,
        "method": "UpdateJob",
        "params": {
            "appId": app,
            "job": {
                "activatedTime": currentUTCTime,
                "applicationID": app,
                "assignedTime": currentJob["scheduledTime"],
                "assignedWorkerId": currentJob["workerId"],
                "comment": comment,
                "commentItems": [
                    {
                        "commentText": comment,
                        "created": currentUTCTime,
                        "userID": "-1",
                        "userName": "user"
                    }
                ],
                "completedTime": None,
                "createdTime": currentJob["scheduledTime"],
                "creatorId": 0,
                "customFields": "[{\"Key\":1,\"Value\":null}]",
                "description": currentJob["description"],
                "id": job,
                "jobDuration": None,
                "jobPoiId": None,
                "jobState": 5,
                "order": 0,
                "routeID": "",
                "scheduledTime": currentJob["scheduledTime"],
                "startLocation": {
                    "address": "Lat: "+str(lat)+" Long:"+str(lon),
                    "administrativeAreaName": None,
                    "categoryID": 0,
                    "cityName": None,
                    "countryName": None,
                    "description": None,
                    "id": "0",
                    "neighborhood": None,
                    "pointOfInterest": None,
                    "position": {
                        "altitude": 0,
                        "is3D": False,
                        "latitude": lat,
                        "longitude": lon
                    },
                    "postalCodeNumber": None,
                    "streetBox": None,
                    "streetName": None,
                    "streetNumber": None,
                    "subAdministrativeAreaName": None
                },
                "updatedTime": "2019-04-11T17:22:44.393Z"
            }
        }
    }
    print(json.dumps(cmd, indent=4, sort_keys=True))
    url = "http://"+ggsdomain+"/comGpsGate/rpc/DispatchFuture"
    cmd = session.post(url, json=cmd)
    print(cmd.json())
    return cmd

####
class MyListener(stomp.ConnectionListener):
    def on_message(self, headers, message):
        print('MyListener:\nreceived a message "{}"\n'.format(message))
        global read_messages
        read_messages.append({'id': headers['message-id'], 'subscription':headers['subscription']})


class MyStatsListener(stomp.StatsListener):
    def on_disconnected(self):
        super(MyStatsListener, self).on_disconnected()
        print('MyStatsListener:\n{}\n'.format(self))

class ApiController(BaseController):

    #allow_only = predicates.not_anonymous()

    @expose('pythondispatchms.templates.api.api')
    def index(self, **kw):
        currentUser=kw["user"]
        currentGroups= kw["groups"]
        for k,v in kw.items():
            print("{} {} ".format(k,v))
        return dict(groups=currentGroups,user=currentUser)

    @expose('json')
    def loadSmartphones(self, **kw):
        filter = [('account', 'eq', kw["user"])]
        return jqgridDataGrabber(Smartphones, 'id', filter, kw).loadGrid()

    @expose('json')
    def updateSmartphones(self, **kw):
        filter = [('account', 'eq', kw["user"])]
        return jqgridDataGrabber(Smartphones, 'id', filter, kw).updateGrid()

    @expose('json')
    def loadJobs(self, **kw):
        filter = [('gate_user', 'eq', kw["gate_user"])]
        return jqgridDataGrabber(Jobs, 'id', filter, kw).loadGrid()

    @expose('json')
    def updateJobs(self, **kw):
        filter = [('gate_user', 'eq', kw["gate_user"])]
        return jqgridDataGrabber(Jobs, 'id', filter, kw).updateGrid()

    @expose('json')
    def sendMsg(self, **kw):
        error = {"Error": "none"}
        print("")
        print(kw["title"])
        print(kw["subtitle"])

        query = DBSession.query(Smartphones).filter_by(imei=kw['imei']).first()
        if query is not None:
            data_message = {"command": "message", "title": kw["title"], "body": kw["subtitle"]}
            apikey = "AIzaSyCxiYxZsSqKGaJ4NM7vM4yP9d0BYlQcNmo"
            push_service = FCMNotification(api_key=apikey)
            resp = push_service.notify_single_device(registration_id=query.token, data_message=data_message)
            error = {"Error": str(resp)}
        else:
            error = {"Error": "Smartphone not found in table"}
        return error


    #https://dispatch.dudewhereismy.mx/api/redirector?account=jorge&imei=234&token=2344&platform=A&gate_user=Repartidor&gate_password=gpscontrol1
    @expose('json')
    def redirector(self, **kw):
        error = {"Error": "none","Password":"1234"}
        if not ('imei' in kw and 'account' in kw and 'token' in kw and 'platform' in kw
                and 'gate_user' in kw and 'gate_password' in kw):
            error = {"Error": "Parametros faltantes"}
        else:
            r=requests.get(app_globals.domainsun + "/app_log/login?user="+kw["account"])
            j=r.json()
            print(j)
            if j["error"]!="password Not Found":
                error = {"Error": "Cuenta de grupo inexistente"}
            else:
                look = DBSession.query(Smartphones).filter_by(gate_user=kw['gate_user']).first()
                if look is not None:
                    error = {"Error":"Usuario de plataforma ya registrado"}
                else:
                    query = DBSession.query(Smartphones).filter_by(account=kw['account'],imei=kw['imei']).first()
                    if query is not None:
                        if query.token!=kw["token"]:
                            error = {"Error": "Este telefono esta asignado a otro dispositivo"}
                    else:
                        root = "23456789AaBbCcDdEeFfGgHhJjKkLlMmNnPpQqRrSsTtUuVvWwXxYyZz"
                        pswd = ""
                        for x in range(0, 4):
                            pswd = pswd + root[random.randint(0, 55)]
                        url="http://testggs.dwim.mx/GPScontrol/Services/Auth.ashx/login?jsonp=&appId=2&strUsername="+kw["gate_user"]+"&strPassword="+kw["gate_password"]
                        r=requests.get(url)
                        j=r.json()
                        print(j)
                        #{'result': True, 'id': -1}
                        if j["result"]:
                            print("Paso!!!")
                            newitem = Smartphones()
                            newitem.imei = kw["imei"]
                            newitem.account = kw["account"]
                            newitem.token = kw["token"]
                            newitem.platform = kw["platform"]
                            newitem.gate_user = kw["gate_user"]
                            newitem.gate_password = kw["gate_password"]
                            newitem.gate_app = "2"
                            newitem.password = pswd
                            DBSession.add(newitem)
                            DBSession.flush()
                            error['Password']=pswd
                        else:
                            error = {"Error": "Usuario o Password Incorrecto"}
        print(error)
        Message.post("Smartphonesfrom", 'RELOAD' + "|")
        return error


    #https://dispatch.dudewhereismy.mx/api/location
    @expose('json')
    def location(self, **kw):
        error = {"Error": "none"}
        print("Updating location")
        if not ('imei' in kw and 'account' in kw and 'latitude' in kw and 'longitude' in kw and 'speed' in kw and 'battery' in kw and 'accuracy' in kw and 'azimuth' in kw and 'valid' in kw):
            error = {"Error": "Parametros faltantes"}
        else:
            query = DBSession.query(Smartphones).filter_by(account=kw['account'], imei=kw['imei']).first()
            if query is not None:
                query.lastupdate = datetime.utcnow()
                query.latitude = float(kw['latitude'])
                query.longitude = float(kw['longitude'])
                query.speed = kw['speed']
                query.accuracy = float(kw['accuracy'])
                query.battery = kw['battery']
                DBSession.flush()
            else:
                error = {"Error": "Parametros faltantes"}
        print(error)
        return error

    #https://dispatch.dudewhereismy.mx/api/release_license
    @expose('json')
    def release_license(self, **kw):
        error = {"Error": "none"}
        print("Release License")
        if not ('imei' in kw and 'account' in kw ):
            error = {"Error": "Parametros faltantes"}
        else:
            item = DBSession.query(Smartphones).filter_by(account=kw['account'], imei=kw['imei']).first()
            if item is not None:
                DBSession.delete(item)
                DBSession.flush()
                Message.post("Smartphonesfrom", 'RELOAD' + "|")
        print(error)
        return error


    #https://dispatch.dudewhereismy.mx/api/dispatch
    @expose('json')
    def dispatch(self, **kw):
        error = {"Error": "none"}
        jobID = kw['jobid']
        jobDate = kw['jobdate']
        jobDesc = kw['jobdesc']
        state = kw['state']
        name = kw['name']
        latitude = kw['latitude']
        longitude = kw['longitude']
        print("ID:{}".format(jobID))
        print("date:{}".format(jobDate))
        print("Description:{}".format(jobDesc))
        print("name:{}".format(name))
        print("state:{}".format(state))
        print("latitude:{}".format(latitude))
        print("longitude:{}".format(longitude))
        if state!="Assigned":
            dday = jobDate[8:10]
            ntime = jobDate[16:24]
            dyear = jobDate[11:15]
            dmonth = a2m(jobDate[4:7])
            newdate = dyear + "/" + dmonth + "/" + dday
            print("time:{}".format(jobDate[16:24]))
            sjobdate= newdate+" " +jobDate[16:24]
            print("S Date:{}".format(sjobdate))
            jobdate = datetime.strptime(sjobdate, '%Y/%m/%d %H:%M:%S')
            # store data in Job Table
            query = DBSession.query(Jobs).filter_by(gate_user=name,job_id=jobID).first()
            if query is None:
                newitem = Jobs()
                newitem.job_id = jobID
                newitem.job_date = jobdate
                newitem.job_description = jobDesc
                newitem.job_state = state
                newitem.latitude =  float(latitude)
                newitem.longitude =  float(longitude)
                newitem.last_update = datetime.now()
                newitem.gate_user = name
                DBSession.add(newitem)
                DBSession.flush()
            else:
                query.job_date = jobdate
                query.job_description = jobDesc
                query.job_state = state
                query.latitude = float(latitude)
                query.longitude = float(longitude)
                query.last_update = datetime.now()
                DBSession.flush()

            print("Date:{}".format(newdate))
            query = DBSession.query(Smartphones).filter_by(gate_user=name).first()
            if query is not None:
                # Send Message
                data_message = {"command": "message", "title": newdate, "body": jobDesc}
                # apikey=os.environ.get('FCM_KEY') or "AIzaSyAw5EFGDer7-PEuXXMzYNPwla9RP2SVqz4"
                apikey = "AIzaSyCxiYxZsSqKGaJ4NM7vM4yP9d0BYlQcNmo"
                push_service = FCMNotification(api_key=apikey)
                resp = push_service.notify_single_device(registration_id=query.token, data_message=data_message)
                # Update Data
                print("Send newjob")
                data_message = {"command": "newjob", "jobnumber": jobID, "jobdate": newdate, "jobtime": ntime,
                                "jobdesc": jobDesc, "joblat": latitude, "joblon": longitude, "jobstate": state}
                push_service = FCMNotification(api_key=apikey)
                resp = push_service.notify_single_device(registration_id=query.token, data_message=data_message)
            Message.post("Smartphonesfrom", 'RELOAD' + "|")
        return error
    
    #https://dispatch.dudewhereismy.mx/api/dispatch
    @expose('json')
    def updatedispatch(self, **kw):
        error = {"Error": "none"}
        ####
        ##
        ggs = "testggs.dwim.mx" ### GPS GATE SERVER DEFINITION
        ##
        ####

        imei = kw['imei']
        type = kw['type']
        jobNumber = kw['jobnumber']
        if 'jobcomment' in kw:
            jobComment = kw['jobcomment']
        else:
            jobComment = ""
        latitude = kw['latitude']
        longitude = kw['longitude']
        print("######### Update Dispatch ##########")
        print(imei)
        print(type)
        print("JOb:{}".format(jobNumber))
        print(jobComment)
        print(latitude)
        print(longitude)
        query = DBSession.query(Jobs).filter_by(job_id=jobNumber).first()
        if query is not None:
            query.comment=jobComment
            DBSession.flush()
        query = DBSession.query(Smartphones).filter_by(imei=imei).first()
        if query is not None:
            print(query.gate_user)
            print(query.gate_password)
            print(query.gate_app)
            if type == "D":
                updateJob2Dispatched(ggs, query.gate_user, query.gate_password, query.gate_app,
                                     jobNumber,
                                     float(latitude), float(longitude))
            if type == "A":
                updateJob2Active(ggs, query.gate_user, query.gate_password, query.gate_app,
                                 jobNumber,
                                 float(latitude), float(longitude))
            if type == "F":
                updateJob2Finished(ggs, query.gate_user, query.gate_password, query.gate_app,
                                   jobNumber,
                                   float(latitude), float(longitude), jobComment)

        return error

    @expose('json')
    def save_image_app(self, **kw):
        reserved = ReservedImages()
        reserved.code = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        reserved.extra = "APP"
        reserved.w = 450
        reserved.h = 450
        reserved.job_id = kw["jobid"]
        reserved.image = base64.decodebytes(bytes(kw["image"],'utf-8'))
        DBSession.add(reserved)
        DBSession.flush()
        return dict(error="ok")


    @expose('json')
    def load_i(self, **kw):
        filter = [('job_id', 'eq', kw['job_id'])]
        ids = []
        return jqgridDataGrabber(ReservedImages, 'id', filter, kw).loadGrid()

    @expose('json')
    def update_i(self, **kw):
        filter = [('job_id', 'eq', kw['job_id'])]
        return jqgridDataGrabber(ReservedImages, 'id', filter, kw).updateGrid()

    @expose('pythondispatchms.templates.api.display')
    def display(self, **kw):
        if 'job' in kw:
            all = DBSession.query(ReservedImages).filter_by(job_id=kw["job"]).all()
            st=""
            for item in all:
                st=st+str(item.id)+","
            if len(st)>0:
                st=st[: -1]
                print(st)
                query = DBSession.query(ReservedImages).filter_by(job_id=kw["job"]).first()
                if query is not None:
                    encoded_string = str(b64encode(query.image), 'utf-8')
                    return dict(jobimage=encoded_string,elements=st,currentjob=kw["job"])
        return dict(jobimage="",elements="",currentjob="")


    @expose('json')
    def getimage(self, **kw):
        print("getimage")
        if 'id' in kw and 'job' in kw:
            query = DBSession.query(ReservedImages).filter_by(job_id=kw["job"],id=kw['id']).first()
            if query is not None:
                print("found")
                encoded_string = str(b64encode(query.image), 'utf-8')
                return dict(image=encoded_string)
        return dict(image="")


    @expose('json')
    def getjobsbydate(self, **kw):
        error = {"Error": "none"}
        gate_user = kw['gateuser']
        jobDate = kw['date']
        if len(gate_user)>0 and len(jobDate)>0:
            cday = jobDate[6:8]
            cmonth = jobDate[4:6]
            cyear = jobDate[:4]
            newdate = cyear + "/" + cmonth + "/" + cday
            print("S Date:{}".format(newdate))
            print("Gate user:{}".format(gate_user))

            job_date = datetime.strptime(newdate, '%Y/%m/%d')
            print("job_date:{}".format(job_date))
            search = DBSession.query(Jobs).filter(func.date(Jobs.job_date)==job_date).all()
            jobsarray=[]
            for query in search:
                print("Found jobs")
                newdate=query.job_date.strftime('%Y-%m-%d')
                ntime = query.job_date.strftime('%H:%M:%S')
                joba = {"jobnumber": query.job_id, "jobdate": newdate, "jobtime": ntime,
                 "jobdesc": query.job_description, "joblat": str(query.latitude), "joblon": str(query.longitude),
                         "jobstate": query.job_state}
                jobsarray.append(joba)
            error = {"Error": "none","jobs":jobsarray}
        else:
            error = {"Error": "No records"}
        print(error)
        return error