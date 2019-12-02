# coding=utf-8
"""Main Controller"""

from tg import expose, flash, require, url, lurl, request,response
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
from pythondispatchms.model.tables import Traffic, Position
from pythondispatchms.lib.rest import Rest
from pythondispatchms.lib.utililty import URLunicode
from pythondispatchms.controllers.lora import LoraController
import arrow, pytz
from tg import app_globals
from datetime import datetime
import requests
import markdown,os
from pythondispatchms.controllers.pets import PetsController
from pythondispatchms.controllers.images import ImagesController
from pythondispatchms.controllers.api import ApiController
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
    test = TestController()
    services= ServicesController()
    traffic = TrafficController()
    rabbit = RabbitController()
    lora = LoraController()
    pets = PetsController()
    images = ImagesController()
    api= ApiController()


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


    @expose('json')
    @expose('jsonp')
    def uplink(self, **kw):

        print(response.body)
        print(response.status)
        print(request.json_body)
        print("Entre")
        print(kw)
        print(repr(kw))
        for k,v in kw.items():
            print("{} {} ".format(k,v))
        return 'ok'


    @expose()
    def join(self, **kw):
        for k,v in kw.items():
            print("{} {} ".format(k,v))
        return 'ok'


    @expose()
    def status(self, **kw):
        for k,v in kw.items():
            print("{} {} ".format(k,v))
        return 'ok'

    @expose()
    def location(self, **kw):
        for k,v in kw.items():
            print("{} {} ".format(k,v))
        return 'ok'

    @expose()
    def ack(self, **kw):
        for k,v in kw.items():
            print("{} {} ".format(k,v))
        return 'ok'

    @expose()
    def error(self, **kw):
        for k,v in kw.items():
            print("{} {} ".format(k,v))
        return 'ok'


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
            if currentListener.state == 1:
                #print("listern on")
                if currentListener.logstate == 1:
                    # Enabled Logging
                    currentListenerFields = DBSession.query(ListenerFields).filter_by(listeners_id=currentListener.id).all()
                    mapper = {}
                    for eachListenerField in currentListenerFields:
                        if eachListenerField.assign != 0:
                            mapper[eachListenerField.assign] = eachListenerField.field
                    newListenerLog = ListenerLog()
                    newListenerLog.time_stamp = datetime.utcnow()
                    newListenerLog.listener_id = currentListener.listener_id
                    newListenerLog.mapper_state=1;
                    if 1 in mapper:
                        newListenerLog.imei = kw[mapper[1]]
                    DBSession.add(newListenerLog)
                    DBSession.flush()
                    currentLog=newListenerLog.id
                allListenerUsers = DBSession.query(ListenerUsers).filter_by(userlisteners_id=currentListener.id).all()
                globalExpressionsRequiredbyListener=[]
                activeListenerUsers=[]
                for each_user in allListenerUsers:
                    # Getting Users to know which expressions must evaluate
                    #print("Getting users")
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
                    if currentListener.logstate == 1:
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
                            # print("EVAL EXPRESSION:{}".format(evalexpression))
                            # print("Field Exists:{} ---> {}".format(isfieldfound,eval(isfieldfound)))
                            # print("Value:{}".format(currentFieldvalue))
                            try:
                                booleanEvalState=eval(evalexpression)
                            except Exception as e:
                                #print("ERROR:{}".format(e))
                                booleanEvalState=False
                            #print("id:{} Exp:{} {} --> {} ".format(eachExpression,currentGlobalExpression.expression,evalexpression,booleanEvalState))
                            globalExpState[eachExpression[0]]=booleanEvalState
                            #
                            #  Listener Log Fields
                            #
                            if currentListener.logstate == 1:
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
                if currentListener.logstate == 1:
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
                attended_state = "N"
                sound=1
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
                        encoded=eachEvalTriggers.expression.encode('utf8')
                        #print("Global Expression:{} Traffic -->: {}".format(encoded,sumOfexpressionsResult))
                        currentUserFiltersExpression=''
                        ####################
                        #                  #
                        # Checar el valor  #
                        # de abajo         #
                        ####################
                        userTriggerExpressionState=True
                        currentUserFilters=DBSession.query(UserFilters).filter_by(user_trigger_id=eachEvalTriggers.id).first()
                        if currentUserFilters is not None:
                            eventCounter=currentUserFilters.counter+1
                            currentUserFiltersExpression=currentUserFilters.expression
                            senTicketVenusExp=currentUserFilters.reset_expression
                            #### Checar

                            #print("UserFilters ID: {} For this group{} Eval:{} --->{}".format(currentUserFilters.id,eachActiveUser['user_name'],currentUserFiltersExpression,userTriggerExpressionState))
                            #print("Imei:{}".format(imei))
                            #print("send to discarded when: {}".format(currentUserFiltersExpression))
                            #print("Send Ticket to venus when:{}".format(senTicketVenusExp))


                        else:
                            userTriggerExpressionState = True
                            currentUserFiltersExpression='Not Defined'
                        #
                        # Listener Log Users
                        #
                        if currentListener.logstate == 1:
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
                            ################
                            # CHECK REPEAT only if there are filters to evaluete #
                            ################
                            if currentUserFilters is not None:
                                venusTicket=''
                                localtz = 'America/Mexico_City'
                                oper_localtime = datetime.now(pytz.timezone(localtz))
                                logImeiEvent=DBSession.query(logImei).filter_by(imei=imei,event_desc=eachEvalTriggers.expression[11:],group_name=eachActiveUser['user_name']).first()
                                if logImeiEvent is None:
                                    newLogImei = logImei()
                                    newLogImei.imei=imei
                                    newLogImei.event_desc=eachEvalTriggers.expression[11:]
                                    newLogImei.group_name=eachActiveUser['user_name']
                                    newLogImei.counter = 1
                                    newLogImei.hour = datetime.utcnow().hour
                                    newLogImei.hour_counter = 1
                                    newLogImei.weekday = oper_localtime.strftime("%A")
                                    newLogImei.user_filters_id=currentUserFilters.id
                                    hour = oper_localtime.strftime("%H:%M")
                                    if hour >= "06:00" and hour <= "12:00":
                                        newLogImei.morning=1
                                    else:
                                        if hour >= "12:00" and hour <= "18:00":
                                            newLogImei.afternoon = 1
                                        else:
                                            if hour >= "18:00" and hour <= "23:59":
                                                newLogImei.night = 1
                                            else:
                                                if hour >= "00:00" and hour <= "06:00":
                                                    newLogImei.early_morning = 1
                                    DBSession.add(newLogImei)
                                else:
                                    time_stamp=logImeiEvent.time_stamp
                                    time_diff=datetime.utcnow()-time_stamp
                                    days_difference=time_diff.days
                                    #print("Time difference since last time stamp in days:{}".format(time_diff.days))
                                    if logImeiEvent.hour==datetime.utcnow().hour:
                                        logImeiEvent.hour_counter +=1
                                        if logImeiEvent.hour_counter>15:
                                            #send to Venus
                                            venus = Rest()
                                            venusUrl = "http://venus.gpscontrol.com.mx/dispatch/create_ticket?client_id=" + str(imeiData['client_id']) + "&last_report=" + str(imeiData['last_report']) + "&folio=0" + "&imei=" + imei + "&comm=" + "Se detecto una inconcistencia en las alertas"
                                            res = requests.get(venusUrl)
                                            if res is not None:
                                                response=res.json()
                                                if 'Ticket' in response:
                                                    venusTicket = response['Ticket']
                                    else:
                                        logImeiEvent.hour=datetime.utcnow().hour
                                        logImeiEvent.hour_counter = 1
                                    if days_difference>0:
                                        logImeiEvent.morning=0
                                        logImeiEvent.afternoon=0
                                        logImeiEvent.night=0
                                        logImeiEvent.early_morning=0
                                        logImeiEvent.counter=1
                                        logImeiEvent.weekday=oper_localtime.strftime("%A")
                                        logImeiEvent.time_stamp=datetime.utcnow()
                                    else:
                                        logImeiEvent.counter=logImeiEvent.counter+1
                                        hour = oper_localtime.strftime("%H:%M")
                                        if hour >= "06:00" and hour <= "12:00":
                                            logImeiEvent.morning += 1
                                        else:
                                            if hour >= "12:00" and hour <= "18:00":
                                                logImeiEvent.afternoon += 1
                                            else:
                                                if hour >= "18:00" and hour <= "23:59":
                                                    logImeiEvent.night += 1
                                                else:
                                                    if hour >= "00:00" and hour <= "06:00":
                                                        logImeiEvent.early_morning += 1
                                        logImeiEvent.weekday = oper_localtime.strftime("%A")
                                        newLogExpression="logImeiEvent."+currentUserFiltersExpression
                                        evalnewLogExp=eval(newLogExpression)
                                        userTriggerExpressionState = True
                                        #print("EXPRESSION REJECTED:{} --->  {}".format(newLogExpression,evalnewLogExp))
                                        if evalnewLogExp:
                                            attended_state = "R"
                                            #if venusTicket=='':

                                            #else:
                                            #    attended_state = "N"
                                DBSession.flush()

                            # resetExpText=currentUserFilters.reset_expression
                            # #print("Reset exp:{}".format(resetExpText))
                            # resetExpText=resetExpText.replace("=","==")
                            # resetExpression=eval(resetExpText)
                            # if resetExpression:
                            #     eventCounter=0
                            # if sumOfexpressionsResult:
                            #     currentUserFilters.counter=eventCounter

                            ################
                            # END REPEAT   #
                            ################


                            #CREATE TRAFFIC FOR THE USER
                            currentListenerFields = DBSession.query(ListenerFields).filter_by(listeners_id=currentListener.id).all()
                            mapper={}
                            for eachListenerField in currentListenerFields:
                                if eachListenerField.assign!=0:
                                    mapper[eachListenerField.assign]=eachListenerField.field

                            newTraffic = Traffic()
                            sound = eachEvalTriggers.sound
                            #print("SOUND: {}".format(sound))
                            newTraffic.attended_state=attended_state
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
                                if kw[mapper[12]]=='':
                                    kw[mapper[12]]='0'
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

                            ############################
                            # logImeiRecord = DBSession.query(logImei).filter_by(imei=parameters['imei'],event_desc=nd,group_name=eachActiveUser['user_name']).first()
                            # if mapper[2] in kw:
                            #     if kw[mapper[2]]=="99":
                            #         logImeiRecord = None
                            # if logImeiRecord is not None:
                            #     #print("FOUND!!!!->{}".format(eachActiveUser['user_name']))
                            #     newTraffic.attended_state = "R"
                            #     hour = oper_localtime.strftime("%H:%M")
                            #     if hour >= "06:00" and hour <= "12:00":
                            #         logImeiRecord.morning += 1
                            #     else:
                            #         if hour >= "12:00" and hour <= "18:00":
                            #             logImeiRecord.afternoon += 1
                            #         else:
                            #             if hour >= "18:00" and hour <= "23:59":
                            #                 logImeiRecord.night += 1
                            #             else:
                            #                 if hour >= "00:00" and hour <= "06:00":
                            #                     logImeiRecord.early_morning += 1
                            #     logImeiRecord.counter=logImeiRecord.counter+1
                            #     if logImeiRecord.counter>100:
                            #         logImeiRecord.counter=0
                            #         logImeiRecord.morning = 0
                            #         logImeiRecord.afternoon = 0
                            #         logImeiRecord.night = 0
                            #         logImeiRecord.early_morning = 0
                            #         logImeiRecord.group_name = eachActiveUser['user_name']
                            #     if logImeiRecord.counter==2:
                            #         if 'client_id' in imeiData and 'last_report' in imeiData:
                            #             venus=Rest()
                            #             venusUrl = "http://venus.gpscontrol.com.mx/dispatch/create_ticket?client_id=" + str(imeiData['client_id']) + "&last_report=" + str(imeiData['last_report']) + "&folio=0" + "&imei=" + imei + "&comm=" + "Ignorar Rodo... Cierrala,.. Se detecto una inconcistencia en las alertas"
                            #             res = requests.get(venusUrl)
                            #             if res is not None:
                            #                 response=res.json()
                            #                 if 'Ticket' in response:
                            #                     venusTicket = response['Ticket']
                            #
                            # else:
                            #     nd = "Evento no definido"
                            #     if 3 in mapper:
                            #         nd = kw[mapper[3]]
                            #         nd = nd.lstrip().rstrip()
                            #         if len(nd) == 0:
                            #             nd = "Evento no definido:" + newTraffic.event_desc
                            #     else:
                            #         eventsid = kw[mapper[2]]
                            #         events = DBSession.query(Events).filter_by(event_id=eventsid).first()
                            #         if events is not None:
                            #             nd = events.event_desc
                            #     newLogImei=logImei()
                            #     newLogImei.imei=parameters['imei']
                            #     newLogImei.event_desc=nd
                            #     newLogImei.counter=1
                            #     newLogImei.weekday = oper_localtime.strftime("%A")
                            #     newLogImei.group_name = eachActiveUser['user_name']
                            #     DBSession.add(newLogImei)
                            #
                            ############################

                            DBSession.add(newTraffic)
                            DBSession.flush()
                            #print("Sound: {}".format(sound))
                            if newTraffic.attended_state=="N":
                                Message.post("trafficlistener_" + eachActiveUser['user_name'], 'RELOAD' + "|"+str(sound))
                            elif newTraffic.attended_state=="R":
                                Message.post("rejectedlistener_" + eachActiveUser['user_name'], 'RELOAD' + "|"+str(sound))
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



# mysql> select event_id,event_desc,user_name,event_time,user,latitude,longitude,imei,speed,azimuth,event_time,time_stamp,priority from traffic where id=42968;
# +----------+------------+--------------------------+---------------------+------------+-----------+------------+-----------------+-------+------------+---------------------+---------------------+----------+
# | event_id | event_desc | user_name                | event_time          | user       | latitude  | longitude  | imei            | speed | azimuth    | event_time          | time_stamp          | priority |
# +----------+------------+--------------------------+---------------------+------------+-----------+------------+-----------------+-------+------------+---------------------+---------------------+----------+
# |        1 | SOS        | 99 NCARGOS S DE RL DE CV | 2018-08-28 16:46:49 | ManagerGPS | 19.366170 | -99.186310 | 864507035846863 |  0.00 | 287.000000 | 2018-08-28 16:46:49 | 2018-08-28 16:46:52 |        1 |
# +----------+------------+--------------------------+---------------------+------------+-----------+------------+-----------------+-------+------------+---------------------+---------------------+----------+
# vehicle = 3B6WW	Yamaha	YBR 125	LBPKE097XF0489255	Roja	3B6WW


    @expose('json')
    def addTraffic(self,**kw):
        fields='event_id,event_desc,user_name,user,latitude,longitude,imei,speed,azimuth,priority,vehicle,valid,dedicated_id'
        error='Campos faltantes:'
        errorName=""
        for item in fields.split(","):
            if not item in kw:
                errorName=errorName+item+","
        if errorName=="":
            newTraffic=Traffic()
            for item in fields.split(","):
                setattr(newTraffic, item, kw[item])
            DBSession.add(newTraffic)
            DBSession.flush()
            Message.post("trafficlistener_" + kw['user'], 'RELOAD' + "|")
            return dict(error="ok")
        return dict(error=error+errorName[:-1])

    @expose('json')
    def storePosition(self,**kw):
        if 'latitude' in kw and 'longitude' in kw:
            query=DBSession.query(Position).filter_by(id=1).first()
            if query is None:
                new = Position()
                new.id = 1
                new.latitude=kw['latitude']
                new.longitude=kw['longitude']
                DBSession.add(new)
                print("added")
            else:
                query.latitude=kw['latitude']
                query.longitude=kw['longitude']
                print("moded")
            DBSession.flush()
            return dict(error="ok")
        else:
            return dict(error="nok")


    @expose('json')
    def getPosition(self,**kw):
        query=DBSession.query(Position).filter_by(id=1).first()
        return dict(latitude=query.latitude,longitude=query.longitude)


    @expose('json')
    def getBooks(self,**kw):
        books=[]
        books.append(dict(title="Sharks",edition="First"))
        books.append(dict(title="Python Programming", edition="First"))
        books.append(dict(title="Java Programming", edition="First"))
        return dict(books=books)



