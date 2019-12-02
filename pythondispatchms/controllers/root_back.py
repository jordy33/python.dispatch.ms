# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, flash, require, url, lurl
from tg import request, redirect, tmpl_context
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tg.exceptions import HTTPFound
from tg import predicates
from pythondispatchms.controllers.secure import SecureController
from pythondispatchms.model import DBSession
from pythondispatchms.lib.base import BaseController
from pythondispatchms.controllers.error import ErrorController
from pythondispatchms.controllers.notification import NotificationController
from pythondispatchms.controllers.services import ServicesController
from pythondispatchms.controllers.traffic import TrafficController
from pythondispatchms.controllers.rabbit import RabbitController
from pythondispatchms.controllers.test import TestController
from pythondispatchms.controllers.admin import AdminController
from pythondispatchms.controllers.log import LogController
from pythondispatchms.lib.messagequeue import Message
from pythondispatchms.model.tables import Listeners,ListenerFields,ListenerUsers,ListenerExpressions,UserTriggers,UserGlobalExp,UserFilters,Events,logImei,Tickets
from pythondispatchms.model.tables import ListenerLog,ListenerLogFields,ListenerLogUsers
from pythondispatchms.model.tables import Traffic
from pythondispatchms.lib.rest import Rest
from pythondispatchms.lib.utililty import URLunicode
import arrow, pytz
from tg import app_globals
from datetime import datetime
import requests
import markdown,os
import pygal
from pygal.style import Style
from pythondispatchms.lib.graphs import GraphApi
__all__ = ['RootController']


class RootController(BaseController):
    """
    The root controller for the python.dispatch.ms application.

    All the other controllers and WSGI applications should be mounted on this
    controller. For example::

        panel = ControlPanelController()
        another_app = AnotherWSGIApplication()

    Keep in mind that WSGI applications shouldn't be mounted directly: They
    must be wrapped around with :class:`tg.controllers.WSGIAppController`.

    """
    #allow_only = predicates.not_anonymous()

    secc  = SecureController()
    admin = AdminController()
    log   = LogController()
    notification = NotificationController()
    error = ErrorController()
    services= ServicesController()
    traffic = TrafficController()
    rabbit = RabbitController()
    test = TestController()

    def _before(self, *args, **kw):
        tmpl_context.project_name = "pythondispatchms"

    @expose('pythondispatchms.templates.index')
    def index(self):
        """Handle the front-page."""
        return dict(page='index')

    @expose('pythondispatchms.templates.index')
    @require(predicates.has_permission('manage', msg=l_('Only for managers')))
    def manage_permission_only(self, **kw):
        """Illustrate how a page for managers only works."""
        return dict(page='managers stuff')

    @expose('pythondispatchms.templates.index')
    @require(predicates.is_user('editor', msg=l_('Only for the editor')))
    def editor_user_only(self, **kw):
        """Illustrate how a page exclusive for the editor works."""
        return dict(page='editor stuff')

    @expose()
    def check(self):
        return "UP"

    @expose()
    def help(self):
        app_dir = os.getenv('dispatch_DIR')
        if app_dir is None:
            app_dir = os.getcwd()
        currentDirectory = app_dir
        #print(currentDirectory)
        with open(currentDirectory+ '/HELP.md','r') as markdown_file:
            content = markdown_file.read()
        return markdown.markdown(content)

    @expose('pythondispatchms.templates.main')
    def main(self):
        """Handle the front-page."""
        return dict(page='index')

    @expose()
    def listener(self, listenerID, **kw):
        currentListener = DBSession.query(Listeners).filter_by(listener_id=listenerID).first()
        if currentListener is None:
            newListener = Listeners()
            newListener.listener_id=listenerID
            newListener.name="Not Defined"
            DBSession.add(newListener)
            DBSession.flush()
            if newListener.id is not None:
                for key, value in kw.items():
                    newfielditem = ListenerFields()
                    newfielditem.field=key
                    newfielditem.value=value
                    newListener.fields.append(newfielditem)
                    DBSession.add(newfielditem)
                    DBSession.flush()
                #print("Admin LISTENER")
                Message.post("adminlistener", 'NEW' + "|")
        else:
            if currentListener.state == 0:
                # The listener is off --> write log and finish listener
                newListenerLog = ListenerLog()
                newListenerLog.time_stamp = datetime.utcnow()
                newListenerLog.listener_id = currentListener.listener_id
                newListenerLog.mapper_state=3;
                DBSession.add(newListenerLog)
                DBSession.flush()
            else:
                # Starting Log
                newListenerLog = ListenerLog()
                newListenerLog.time_stamp = datetime.utcnow()
                newListenerLog.listener_id = currentListener.listener_id
                newListenerLog.mapper_state=1;
                DBSession.add(newListenerLog)
                DBSession.flush()
                currentLog=newListenerLog.id
                allListenerUsers = DBSession.query(ListenerUsers).filter_by(userlisteners_id=currentListener.id).all()
                globalExpressionsRequiredbyListener=[]
                activeListenerUsers=[]
                for each_user in allListenerUsers:
                    # Getting Users to know which expressions must evaluate
                    # jorge
                    # diego
                    if each_user.state==1:
                        #print("USER-->{} userlistener_id{}".format(each_user.user_name,each_user.userlisteners_id))
                        # If the user is active ---> get all the triggers requested by the user
                        activeListenerUsers.append(dict(id=each_user.id,user_name=each_user.user_name))
                        currentUseId=each_user.id
                        allUserTriggers=DBSession.query(UserTriggers).filter_by(listener_users_id=currentUseId).all()
                        for eachUserTriger in allUserTriggers:
                            # id=1 / Expression = EVENT_DESC=SOS and CLIENT_ID-510
                            # id=2 Expression = EVENT_DESC=Paro de Motor and CLIENT_ID=510
                            currenUserId=eachUserTriger.id
                            allUserGlobalExpressions = DBSession.query(UserGlobalExp).filter_by(usertriggers_id=currenUserId).all()
                            for eachGlobalExpression in allUserGlobalExpressions:
                                found=False
                                for eitem in globalExpressionsRequiredbyListener:
                                    if eitem[0]==eachGlobalExpression.global_exp_id:
                                        found=True
                                if not found:
                                    globalExpressionsRequiredbyListener.append((eachGlobalExpression.global_exp_id,each_user.userlisteners_id));
                                    #print((eachGlobalExpression.global_exp_id,each_user.userlisteners_id))
                globalExpState={}
                for eachExpression in globalExpressionsRequiredbyListener:
                    # id=1 /Expression EVENT_DESC=SOS /expression_id=3 /expression_op = / expression_value = SOS
                    currentGlobalExpression = DBSession.query(ListenerExpressions).filter_by(id=eachExpression[0]).first()
                    currentListenerLog = DBSession.query(ListenerLog).filter_by(id=currentLog).first()
                    if currentGlobalExpression is not None:
                        # EVAL EXPRESSIONS
                        currentField=DBSession.query(ListenerFields).filter_by(assign=currentGlobalExpression.expression_id,listeners_id=eachExpression[1]).first()
                        if currentField is not None:
                            currentFieldName=currentField.field
                            operator = "==" if currentGlobalExpression.expression_op=="=" else currentGlobalExpression.expression_op
                            if currentFieldName in kw:
                                utf8 = URLunicode()
                                currentFieldvalue = utf8.decode(kw[currentFieldName])
                                #evalexpression='kw["'+currentFieldName+'"]'+operator+'"'+currentGlobalExpression.expression_value+'"'
                                evalexpression = '"'+currentFieldvalue +'"'+ operator + '"' + currentGlobalExpression.expression_value + '"'
                                isfieldfound='"'+currentFieldName+'" in kw'
                            else:
                                evalexpression=""
                                isfieldfound=False
                            #print("EVAL EXPRESSION:{}".format(evalexpression))
                            #print("Field Exists:{} ---> {}".format(isfieldfound,eval(isfieldfound)))
                            #print("Value:{}".format(currentFieldvalue))
                            try:
                                booleanEvalState=eval(evalexpression)
                            except Exception as e:
                                #print("ERROR:{}".format(e))
                                booleanEvalState=False
                            #print("id:{} Exp:{} {} --> {} ".format(eachExpression,currentGlobalExpression.expression,evalexpression,booleanEvalState))
                            globalExpState[eachExpression[0]]=booleanEvalState
                            newLogFields=ListenerLogFields()
                            newLogFields.field=currentFieldName
                            newLogFields.assigned_to=currentGlobalExpression.expression_id
                            newLogFields.value=currentGlobalExpression.expression_value
                            newLogFields.isfieldfound=eval(isfieldfound)
                            newLogFields.expression=currentGlobalExpression.expression
                            newLogFields.expression_state = booleanEvalState
                            newLogFields.received =  kw[currentFieldName]
                            currentListenerLog.fields.append(newLogFields)
                            DBSession.add(newLogFields)
                            DBSession.flush()
                currentListenerLog = DBSession.query(ListenerLog).filter_by(id=currentLog).first()
                #for k,v in globalExpState.items():
                    #print("KEY :{} VALUE:{}".format(k,v))
                ####
                ###   GET IMEI and pluto once
                ####
                currentIMEI = DBSession.query(ListenerFields).filter_by(listeners_id=currentListener.id,assign=1).first()
                if currentIMEI.field in kw:
                    imei=kw[currentIMEI.field]
                else:
                    imei=""
                #print("IMEI:{}".format(imei))
                pluto = Rest()
                parameters = {}
                parameters['imei'] = imei
                venusTicket = ""

                imeiData = pluto.get(app_globals.domainpluto + "/services/imeiInfo", parameters)
                for eachActiveUser in activeListenerUsers:
                    #print("{} {}".format(eachActiveUser['id'],eachActiveUser['user_name']))
                    toEvalUserTriggers = DBSession.query(UserTriggers).filter_by(listener_users_id=eachActiveUser['id']).all()
                    for eachEvalTriggers in toEvalUserTriggers:
                        priority=eachEvalTriggers.priority
                        globalExpToEval = DBSession.query(UserGlobalExp).filter_by(usertriggers_id=eachEvalTriggers.id).all()
                        sumOfexpressionsResult=True
                        for eachGlobalExpToEval in globalExpToEval:
                            #print("Expression:{} --> {}".format(eachGlobalExpToEval.global_exp_id,globalExpState[eachGlobalExpToEval.global_exp_id]))
                            k=eachGlobalExpToEval
                            if globalExpState[eachGlobalExpToEval.global_exp_id]==False:
                                sumOfexpressionsResult = False
                                break
                        #print("Global Expression:{} Traffic -->: {}".format(eachEvalTriggers.expression,sumOfexpressionsResult))
                        currentUserFiltersExpression=''
                        userTriggerExpressionState=False
                        currentUserFilters=DBSession.query(UserFilters).filter_by(user_trigger_id=eachEvalTriggers.id).first()
                        if currentUserFilters is not None:
                            eventCounter=currentUserFilters.counter+1
                            currentUserFiltersExpression=currentUserFilters.expression
                            userTriggerExpressionState=eval(currentUserFiltersExpression)
                            #print("Eval:{} --->{}".format(currentUserFiltersExpression,userTriggerExpressionState))
                            resetExpText=currentUserFilters.reset_expression
                            #print("Reset exp:{}".format(resetExpText))
                            resetExpText=resetExpText.replace("=","==")
                            resetExpression=eval(resetExpText)
                            if resetExpression:
                                eventCounter=0
                            if sumOfexpressionsResult:
                                currentUserFilters.counter=eventCounter
                                DBSession.flush()
                        else:
                            userTriggerExpressionState = True
                            currentUserFiltersExpression='Not Defined'
                        newLogUsers = ListenerLogUsers()
                        newLogUsers.user_name=eachActiveUser['user_name']
                        newLogUsers.trigger_expr=eachEvalTriggers.expression
                        newLogUsers.trigger_expr_state=sumOfexpressionsResult
                        newLogUsers.filter_expr=currentUserFiltersExpression
                        newLogUsers.filter_expr_state=userTriggerExpressionState
                        currentListenerLog.users.append(newLogUsers)
                        DBSession.add(newLogUsers)
                        DBSession.flush()
                        Message.post("logListener", 'NEW' + "|")
                        if sumOfexpressionsResult and userTriggerExpressionState:
                            #CREATE TRAFFIC FOR THE USER
                            currentListenerFields = DBSession.query(ListenerFields).filter_by(listeners_id=currentListener.id).all()
                            mapper={}
                            for eachListenerField in currentListenerFields:
                                if eachListenerField.assign!=0:
                                    mapper[eachListenerField.assign]=eachListenerField.field

                            newTraffic = Traffic()
                            if imeiData["error"] == "ok":
                                newTraffic.user_name=imeiData['application']
                            if 1 in mapper:
                                newTraffic.imei=kw[mapper[1]]
                            if 2 in mapper:
                                if kw[mapper[2]]=="":
                                    newTraffic.event_id = 0
                                else:
                                    newTraffic.event_id=kw[mapper[2]]
                            if 3 in mapper:
                                newTraffic.event_desc=kw[mapper[3]]
                            else:
                                eventsid=kw[mapper[2]]
                                events=DBSession.query(Events).filter_by(event_id=eventsid).first()
                                if events is not None:
                                    newTraffic.event_desc=events.event_desc
                                else:
                                    newTraffic.event_desc=""
                            if 4 in mapper:
                                newTraffic.latitude=kw[mapper[4]]
                            if 5 in mapper:
                                newTraffic.longitude=kw[mapper[5]]
                            if 6 in mapper:
                                if kw[mapper[6]]=="":
                                    speed=0
                                else:
                                    speed=int(float(kw[mapper[6]]))
                                newTraffic.speed=speed
                            if 7 in mapper:
                                newTraffic.azimuth=kw[mapper[7]]
                            if 8 in mapper:
                                newTraffic.valid=kw[mapper[8]]
                            if 9 in mapper:
                                newTraffic.event_time=kw[mapper[9]]
                            if 10 in mapper:
                                newTraffic.client_id=kw[mapper[10]]
                            if 11 in mapper:
                                vehicleData=kw[mapper[11]]
                                vehicleCheck=vehicleData.replace(" ","")
                                if len(vehicleData)>0:
                                    newTraffic.vehicle=vehicleData
                                else:
                                    if imeiData["error"] == "ok":
                                        if imeiData["brand"] is not None and imeiData["model"] is not None:
                                            newTraffic.vehicle = imeiData["brand"] + ' ' + imeiData["model"] + ' '
                            else:
                                if imeiData["error"] == "ok":
                                    if imeiData["brand"] is not None and imeiData["model"] is not None:
                                        newTraffic.vehicle=imeiData["brand"]+' '+imeiData["model"]+' '
                            if 12 in mapper:
                                newTraffic.voltage=kw[mapper[12]]
                            if 13 in mapper:
                                newTraffic.internal_id=kw[mapper[13]]
                            if 14 in mapper:
                                if kw[mapper[14]]=='':
                                    newTraffic.mcc=0
                                else:
                                    newTraffic.mcc=kw[mapper[14]]
                            if 15 in mapper:
                                if kw[mapper[15]] == '':
                                    newTraffic.mnc=0
                                else:
                                    newTraffic.mnc = kw[mapper[15]]
                            if 16 in mapper:
                                if kw[mapper[16]] == '':
                                    newTraffic.lac=0
                                else:
                                    newTraffic.lac = kw[mapper[16]]
                            if 17 in mapper:
                                if kw[mapper[17]] == '':
                                    newTraffic.cellid=0
                                else:
                                    newTraffic.cellid = kw[mapper[17]]
                            newTraffic.user=eachActiveUser['user_name']
                            newTraffic.priority=priority
                            localtz = 'America/Mexico_City'
                            if 9 in mapper:
                                cuda=kw[mapper[9]]
                                cuda=cuda[:19]
                                dateconversion = datetime.strptime(cuda, '%Y-%m-%dT%H:%M:%S')
                                oper_utc = arrow.get(dateconversion)
                                oper_localtime = oper_utc.to(localtz)
                            else:
                                oper_localtime = datetime.now(pytz.timezone(localtz))
                            nd = "Evento no definido"
                            if 3 in mapper:
                                nd = kw[mapper[3]]
                                nd=nd.lstrip().rstrip()
                                if len(nd)==0:
                                    nd="Evento no definido:"+newTraffic.event_desc
                            else:
                                eventsid = kw[mapper[2]]
                                events = DBSession.query(Events).filter_by(event_id=eventsid).first()
                                if events is not None:
                                    nd = events.event_desc
                            #print("-------->>> user:{}".format(eachActiveUser['user_name']))
                            logImeiRecord = DBSession.query(logImei).filter_by(imei=parameters['imei'],event_desc=nd,group_name=eachActiveUser['user_name']).first()
                            if mapper[2] in kw:
                                if kw[mapper[2]]=="99":
                                    logImeiRecord = None
                            if logImeiRecord is not None:
                                #print("FOUND!!!!->{}".format(eachActiveUser['user_name']))
                                newTraffic.attended_state = "R"
                                hour = oper_localtime.strftime("%H:%M")
                                if hour >= "06:00" and hour <= "12:00":
                                    logImeiRecord.morning += 1
                                else:
                                    if hour >= "12:00" and hour <= "18:00":
                                        logImeiRecord.afternoon += 1
                                    else:
                                        if hour >= "18:00" and hour <= "23:59":
                                            logImeiRecord.night += 1
                                        else:
                                            if hour >= "00:00" and hour <= "06:00":
                                                logImeiRecord.early_morning += 1
                                logImeiRecord.counter=logImeiRecord.counter+1
                                if logImeiRecord.counter>100:
                                    logImeiRecord.counter=0
                                    logImeiRecord.morning = 0
                                    logImeiRecord.afternoon = 0
                                    logImeiRecord.night = 0
                                    logImeiRecord.early_morning = 0
                                    logImeiRecord.group_name = eachActiveUser['user_name']
                                if logImeiRecord.counter==2:
                                    if 'client_id' in imeiData and 'last_report' in imeiData:
                                        venus=Rest()
                                        venusUrl = "http://venus.gpscontrol.com.mx/dispatch/create_ticket?client_id=" + str(imeiData['client_id']) + "&last_report=" + str(imeiData['last_report']) + "&folio=0" + "&imei=" + imei + "&comm=" + "Ignorar Rodo... Cierrala,.. Se detecto una inconcistencia en las alertas"
                                        res = requests.get(venusUrl)
                                        if res is not None:
                                            response=res.json()
                                            if 'Ticket' in response:
                                                venusTicket = response['Ticket']

                            else:
                                nd = "Evento no definido"
                                if 3 in mapper:
                                    nd = kw[mapper[3]]
                                    nd = nd.lstrip().rstrip()
                                    if len(nd) == 0:
                                        nd = "Evento no definido:" + newTraffic.event_desc
                                else:
                                    eventsid = kw[mapper[2]]
                                    events = DBSession.query(Events).filter_by(event_id=eventsid).first()
                                    if events is not None:
                                        nd = events.event_desc
                                newLogImei=logImei()
                                newLogImei.imei=parameters['imei']
                                newLogImei.event_desc=nd
                                newLogImei.counter=1
                                newLogImei.weekday = oper_localtime.strftime("%A")
                                newLogImei.group_name = eachActiveUser['user_name']
                                DBSession.add(newLogImei)
                            DBSession.add(newTraffic)
                            DBSession.flush()
                            if newTraffic.attended_state=="N":
                                Message.post("trafficlistener_" + eachActiveUser['user_name'], 'RELOAD' + "|")
                            elif newTraffic.attended_state=="R":
                                Message.post("rejectedlistener_" + eachActiveUser['user_name'], 'RELOAD' + "|")
                            if venusTicket!="":
                                searchticket = DBSession.query(Tickets).filter_by(ticket=venusTicket).first()
                                if searchticket is None:
                                    newTickets = Tickets()
                                    newTickets.traffic_id = newTraffic.id
                                    newTickets.ticket = venusTicket
                                    newTickets.comment = "Se detecto una inconcistencia en las alertas"
                                    DBSession.add(newTickets)
                                    DBSession.flush()

        return 'ok'



