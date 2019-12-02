# -*- coding: utf-8 -*-
"""Sample controller with all its actions protected."""
from tg import expose, flash
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tg import predicates,app_globals
from pythondispatchms.lib.base import BaseController
from pythondispatchms.lib.decorators import restErrorHandler
from pythondispatchms.lib.graphs import GraphApi

from datetime import datetime
from random import randint
from pythondispatchms.model import DBSession, User,Notification
from pythondispatchms.lib.messagequeue import Message
import requests
from pythondispatchms.lib.rest import Rest,TelefonicaRest
from tg import request
import pygal
import arrow, pytz
from tg import expose, render_template
from base64 import b64encode
from pythondispatchms.lib.utililty import ExportCVS, ExportPDF
from pythondispatchms.model.tables import Assets
__all__ = ['TestController']

import stomp

def randomNumber():
    return randint(0, 5)

class MyListener(stomp.ConnectionListener):
    def on_message(self, headers, message):
        print('MyListener:\nreceived a message "{}"\n'.format(message))
        global read_messages
        read_messages.append({'id': headers['message-id'], 'subscription':headers['subscription']})


class MyStatsListener(stomp.StatsListener):
    def on_disconnected(self):
        super(MyStatsListener, self).on_disconnected()
        print('MyStatsListener:\n{}\n'.format(self))

class TestController(BaseController):

    #allow_only = predicates.not_anonymous()


    @expose()
    def check(self):
        return "UP"

    @expose('pythondispatchms.templates.test.websockets')
    def websockets(self, **kw):
        return dict(dummy="",id=kw["id"]+kw["user"],user=kw["user"])

    @expose('pythondispatchms.templates.graphs.graph')
    def graph(self):
         newGraph=GraphApi()
         return dict(graph_data=newGraph.simVolume())

    @expose('pythondispatchms.templates.graphs.graph')
    def graph2(self):
        newGraph = GraphApi()
        return dict(graph_data=newGraph.simVolume())

    @expose('pythondispatchms.templates.test.telefonica')
    def telefonica(self):
        print("TELEFONICA")
        icc = '8952020616170020641'
        icc  = '8952020216170366233'
        icc = '8952020616170017753'
        icc = '8934072100260832137'
        url = "https://m2m-api.telefonica.com:8010/services/REST/GlobalM2M/Inventory/v5/r12/sim/icc:" + str(
            icc) + "/location"
        print("url:"+url)
        s=requests.session()
        params={}
        kw = {'params': params, 'cert': app_globals.cert, 'verify': False, 'timeout': 10}
        response = s.get(url, **kw)
        print(response)
        values=response.json()
        if 'ClientException' in values:
            print("Error:"+values['ClientException']['text'])
        else:
            #locationDetailData: {'automaticLocation': {'coordinates': {'longitude': -98.972992, 'latitude': 19.22096},'timestamp': '2018-07-19T11:54:32Z'}}
            # for k,v in values.items():
            #     print("{}:{}".format(k,v))
            latitude=values['locationDetailData']['automaticLocation']['coordinates']['latitude']
            longitude = values['locationDetailData']['automaticLocation']['coordinates']['longitude']
            print(latitude)
            print(longitude)

        return dict(dummy=response)

    @expose('json')
    def users(self):
        params={}
        url = "https://m2m-api.telefonica.com:8010/services/REST/GlobalM2M/Users/v1/r12/user"
        r = requests.get(url, params=params, cert=app_globals.cert, verify=False)
        return str(r.json())

    @expose('json')
    @restErrorHandler()
    def stomp(self, **kw):
        if "channel" in kw and "msg"in kw:
            channel=kw["channel"]
            msg=kw["msg"]
            c = stomp.Connection([(app_globals.stompHost, 61613)])
            #c = stomp.Connection([("dudewhereismy.mx", 61613)])
            c.start()
            c.set_listener('my_listener', MyListener())
            c.set_listener('stats_listener', MyStatsListener())
            c.connect('dwim', 'gpscontrol1', wait=True)
            c.send(body="Msg: "+msg, destination='/topic/frame'+channel+'manager')
            c.disconnect()
            return dict(msg="sent")
        else:
            return dict(error="Missing channel or msg parameter")

    @expose('json')
    def notification(self, **kw):
        if "user" in kw:
            origin = ['System', 'Administrator', 'Guest', 'Bob', 'Louisa', 'Mark']
            action = ['Requests', 'Needs', 'Appreciate', 'Speaks', 'Share', 'Insist']
            category = ['Alert Manager', 'Stop Alarm', 'Extinguish Fire', 'Invite to dinner', 'Rest', 'Take Vacation']
            title = ['Attend Alarm', 'Kill System', 'Start Procedure', 'Find dodumentation', 'Press Button',
                     'End procedure']
            subtitle = ['For Neza', 'For Neto Stores', 'For Mexico News', 'For Alestra', 'For HSBC', 'For Bancomer']
            pushDate = str(datetime.utcnow())
            icon = ['glyphicon glyphicon-tags', 'glyphicon glyphicon-book', 'glyphicon glyphicon-bookmark',
                    'glyphicon glyphicon-eye-open', 'glyphicon glyphicon-warning-sign', 'glyphicon glyphicon-comment']

            message = origin[randomNumber()] + "," + action[randomNumber()] + "," + category[randomNumber()] + "," + title[
                randomNumber()] + "," + subtitle[randomNumber()] + "," + pushDate + "," + icon[randomNumber()]
            userSession = DBSession.query(User).filter_by(user_name=kw['user']).first()
            newItem = Notification()
            newItem.user_id = userSession.user_id
            newItem.attended_state = 'N'
            newItem.time_stamp = datetime.utcnow()
            newItem.message = message
            DBSession.add(newItem)
            DBSession.flush()
            counter = DBSession.query(Notification).filter_by(user_id=userSession.user_id,attended_state="N").count()
            if counter == 0:
                value = ""
            else:
                value = str(counter)
            message = 'NOT' + "|" + value
            Message.post(kw['user'],message)
            return dict(error='ok')
        else:
            return dict(error='user parameter missing')

    @expose('json')
    def message(self, **kw):
        if "user" in kw:
            if "msg" in kw:
                Message.post(kw['user'], 'MSG'+"|"+kw['msg'])
            else:
                return dict(error='msg parameter missing')
        else:
            return dict(error='user parameter missing')


    @expose('pythondispatchms.templates.test.json')
    def grid(self, **kw):
        return dict(dummy="")

    @expose('json')
    def data(self,**kw):
        print()
        rows=[]
        rows.append({"OrderID": "10248", "OrderDate": "1996-07-04", "CustomerID": "WILMK", "ShipName": "Vins et alcools Chevalier","Freight": "32.3800"})
        rows.append({"OrderID": "10249", "OrderDate": "1996-07-05", "CustomerID": "TRADH", "ShipName": "Toms Spezialit\u00e4ten","Freight": "11.6100"})
        rows.append({"OrderID": "10250", "OrderDate": "1996-07-08", "CustomerID": "HANAR", "ShipName": "Hanari Carnes","Freight": "65.8300"})
        rows.append({"OrderID": "10251", "OrderDate": "1996-07-08", "CustomerID": "VICTE", "ShipName": "Victuailles en stock","Freight": "41.3400"})
        rows.append({"OrderID": "10252", "OrderDate": "1996-07-09", "CustomerID": "SUPRD", "ShipName": "Supr\u00eames d\u00e9lices","Freight": "51.3000"})
        rows.append({"OrderID": "10253", "OrderDate": "1996-07-10", "CustomerID": "HANAR", "ShipName": "Hanari Carnes","Freight": "58.1700"})
        rows.append({"OrderID": "10254", "OrderDate": "1996-07-11", "CustomerID": "CHOPS", "ShipName": "Chop-suey Chinese","Freight": "22.9800"})
        rows.append({"OrderID": "10255", "OrderDate": "1996-07-12", "CustomerID": "RICSU", "ShipName": "Richter Supermarkt","Freight": "148.3300"})
        rows.append({"OrderID": "10256", "OrderDate": "1996-07-15", "CustomerID": "WELLI", "ShipName": "Wellington Importadora","Freight": "13.9700"})
        rows.append({"OrderID": "10257", "OrderDate": "1996-07-16", "CustomerID": "HILAA", "ShipName": "HILARI\u00d3N-Abastos","Freight": "81.9100"})
        rows.append({"OrderID": "10258", "OrderDate": "1996-07-17", "CustomerID": "ERNSH", "ShipName": "Ernst Handel","Freight": "140.5100"})
        rows.append({"OrderID": "10259", "OrderDate": "1996-07-18", "CustomerID": "CENTC", "ShipName": "Centro comercial Moctezuma","Freight": "3.2500"})
        rows.append({"OrderID": "10260", "OrderDate": "1996-07-19", "CustomerID": "OLDWO", "ShipName": "Ottilies K\u00e4seladen","Freight": "55.0900"})
        rows.append({"OrderID": "10261", "OrderDate": "1996-07-19", "CustomerID": "QUEDE", "ShipName": "Que Del\u00edcia","Freight": "3.0500"})
        rows.append({"OrderID": "10262", "OrderDate": "1996-07-22", "CustomerID": "RATTC", "ShipName": "Rattlesnake Canyon Grocery","Freight": "48.2900"})
        rows.append({"OrderID": "10263", "OrderDate": "1996-07-23", "CustomerID": "ERNSH", "ShipName": "Ernst Handel","Freight": "146.0600"})
        rows.append({"OrderID": "10264", "OrderDate": "1996-07-24", "CustomerID": "FOLKO", "ShipName": "Folk och f\u00e4 HB", "Freight": "3.6700"})
        rows.append({"OrderID": "10265", "OrderDate": "1996-07-25", "CustomerID": "BLONP", "ShipName": "Blondel p\u00e8re et fils","Freight": "55.2800"})
        rows.append({"OrderID": "10266", "OrderDate": "1996-07-26", "CustomerID": "WARTH", "ShipName": "Wartian Herkku","Freight": "25.7300"})
        rows.append({"OrderID": "10267", "OrderDate": "1996-07-29", "CustomerID": "FRANK", "ShipName": "Frankenversand","Freight": "208.5800"})
        rows.append({"OrderID": "10268", "OrderDate": "1996-07-30", "CustomerID": "GROSR", "ShipName": "GROSELLA-Restaurante","Freight": "66.2900"})
        rows.append({"OrderID": "10269", "OrderDate": "1996-07-31", "CustomerID": "WHITC", "ShipName": "White Clover Markets","Freight": "4.5600"})
        rows.append({"OrderID": "10270", "OrderDate": "1996-08-01", "CustomerID": "WARTH", "ShipName": "Wartian Herkku", "Freight": "136.5400"})
        rows.append({"OrderID": "10271", "OrderDate": "1996-08-01", "CustomerID": "SPLIR", "ShipName": "Split Rail Beer & Ale","Freight": "4.5400"})
        # for item in range(1,10):
        #     rows.append({"CategoryName":"Beverages","ProductName":"Steeleye Stout","Country":"UK","Price":"1008.0000","Quantity":"65"})
        #     rows.append({"CategoryName":"Beverages","ProductName":"Laughing Lumberjack Lager","Country":"USA","Price":"140.0000","Quantity":"10"})
        #     rows.append({"CategoryName":"Beverages","ProductName":"Lakkalik\Ri","Country":"USA", "Price":"2160.0000", "Quantity":"120" })
        return dict(rows=rows)

    @expose('pythondispatchms.templates.test.users')
    def users(self, **kw):
        return dict(dummy="")

    @expose('json')
    def getUsers(self,**kw):
        rows=[]
        imeiInfo=Rest()
        userData=imeiInfo.get(app_globals.sunUsers, {})
        for item in userData["users"]:
            rows.append({"username": item["username"], "email": item["email"]})
        rows = sorted(rows, key=lambda k: k['username'])
        return dict(rows=rows)


    @expose('pythondispatchms.templates.test.ecran')
    def ecran(self, **kw):
        return dict(dummy="")

    @expose('pythondispatchms.templates.test.new')
    def new(self, **kw):
        return dict(dummy="")


    @expose('pythondispatchms.templates.test.messages')
    def messages(self, **kw):
        return dict(user=request.identity["repoze.who.userid"])


    @expose('json')
    def receiveMessage(self, **kw):
        userName = request.identity['repoze.who.userid']
        Message.post("testlistener_" + userName, 'MSG_'+kw['color'] + "|" + "Test")
        return dict(dummy="")


    @expose('pythondispatchms.templates.test.test')
    def test(self):
        return dict(page='editor stuff')

    @expose('pythondispatchms.templates.test.datetime')
    def testdate(self, **kw):
        return dict(user=request.identity["repoze.who.userid"])


    @expose('pythondispatchms.templates.test.stepsExample')
    def stepsExample(self, **kw):
        return dict(user=request.identity["repoze.who.userid"])


    @expose('json')
    def loadWizard(self, **kw):
        list = []
        dedwizardtemplate = render_template(
            {"list": list, "parameter1": 'something'}, "mako", kw['name'])
        return dict(dedwizardtemplate=dedwizardtemplate)

    @expose()
    def asyncStep(self, **kw):
        localtz = 'America/Mexico_City'
        oper_localtime = datetime.now(pytz.timezone(localtz))
        dedwizardtemplate = render_template({"user": request.identity["repoze.who.userid"],"cal":kw['cal'],"current_time":oper_localtime.strftime('%Y-%m-%dT%H:%M:%S')}, "mako", 'pythondispatchms.templates.test.asyncStep')
        return dedwizardtemplate

    @expose('json')
    def saveWizard(self, **kw):
        rows = []
        print(kw['parameter1'])
        print(kw['parameter2'])
        return dict(rows=rows)


    @expose('pythondispatchms.templates.test.csv')
    def csv(self):
        list=[]
        allrecords = DBSession.query(User).all()
        for item in allrecords:
            list.append(str(item.user_id)+","+item.user_name+","+item.email_address+","+item.display_name+'\n')
        file_name=ExportCVS.create(list,"users","/test/csv")
        print("file_name:{}".format(file_name))
        return dict(file_name=file_name)

    @expose('pythondispatchms.templates.test.pdf')
    def pdf(self):
        list=[]
        file_name=ExportPDF.create({"parameter1": 'Jorge'},"pdftest","pythondispatchms.templates.test.pdfexample")
        print("fn:{}".format(file_name))
        return dict(file_name=file_name)


    @expose('pythondispatchms.templates.test.twg')
    def twg(self):
        return dict(dummy='')

    @expose('')
    def movie_submit(self,**kw):
        for k,v in kw.items():
            print("{}:{}".format(k,v))

        return dict(dummy='')


    @expose('pythondispatchms.templates.test.images')
    def images(self, **kw):
        list = []
        myimages = DBSession.query(Assets).all()
        for every_picture in myimages:
            list.append(every_picture.data)
            print("len:{}".format(len(every_picture.data)))
        return dict(list=list)
