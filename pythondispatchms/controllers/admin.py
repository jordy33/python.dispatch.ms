# -*- coding: utf-8 -*-
"""Sample controller with all its actions protected."""
from tg import expose, render_template
from tg import predicates,app_globals

from pythondispatchms.lib.base import BaseController
from pythondispatchms.lib.jqgrid import jqgridDataGrabber
from pythondispatchms.model.tables import Listeners,ListenerFields,ListenerUsers,ListenerExpressions,UserTriggers,UserGlobalExp,UserFilters,EmailService,Events,Dedicated,Devices,Roles,RolUsers,Calendars,TempCalendars
from pythondispatchms.model import DBSession
from pythondispatchms.lib.messagequeue import Message
from pythondispatchms.lib.rest import Rest
from datetime import datetime
import arrow, pytz
from datetime import timedelta
import requests
__all__ = ['AdminController']

class AdminController(BaseController):

    #allow_only = predicates.not_anonymous()

    @expose('pythondispatchms.templates.admin.adminlistener')
    def adminListener(self,**kw):
        return dict(page='index',user=kw["user"])

    @expose('json')
    def loadListenerAdmin(self, **kw):
        filter = []
        return jqgridDataGrabber(Listeners, 'id', filter, kw).loadGrid()

    @expose('json')
    def updateListenerAdmin(self, **kw):
        filter = []
        return jqgridDataGrabber(Listeners, 'id', filter, kw).updateGrid()

    @expose('json')
    def updateListenerState(self, **kw):
        query = DBSession.query(Listeners).filter_by(id=kw["id"]).first()
        if query is not None:
            if query.state==1:
                query.state=0
            else:
                query.state=1
            DBSession.flush()
            Message.post("adminlistener", 'RELOAD' + "|" )

    @expose('json')
    def updateLogListenerState(self, **kw):
        query = DBSession.query(Listeners).filter_by(id=kw["id"]).first()
        if query is not None:
            if query.logstate==1:
                query.logstate=0
            else:
                query.logstate=1
            DBSession.flush()
            Message.post("adminlistener", 'RELOAD' + "|" )

    @expose('json')
    def updateListenerUserState(self,**kw):
        query = DBSession.query(ListenerUsers).filter_by(id=kw["id"]).first()
        if query is not None:
            if query.state==1:
                query.state=0
            else:
                query.state=1
            DBSession.flush()

    @expose('json')
    def loadListenerFieldsAdmin(self, **kw):
        filter = [('listeners_id', 'eq', kw["id"])]
        return jqgridDataGrabber(ListenerFields, 'id', filter, kw).loadGrid()

    @expose('json')
    def updateListenerFieldsAdmin(self, **kw):
        filter = []
        return jqgridDataGrabber(ListenerFields, 'id', filter, kw).updateGrid()

    @expose('json')
    def updateListenerFields(self, **kw):
        record = kw['record']
        assigment = kw['assigment']
        multiplier = kw['multiplier']
        unit = kw['unit']
        listener = DBSession.query(ListenerFields).filter_by(id=record).first()
        if listener is not None:
            listener.assign = int(assigment)
            listener.multiplier = float(multiplier)
            listener.unit = unit
            DBSession.flush()
        return dict(error='ok')

    @expose('json')
    def loadAssignFormTemplate(self, **kw):
        list = []
        search=DBSession.query(ListenerFields).filter_by(id=kw["row"]).first()
        if search is not None:
            pointer=search.listeners_id
            so=DBSession.query(ListenerFields).filter_by(listeners_id=pointer).all()
            lassigned=[]
            tosearch=""
            for k,v in app_globals.masterFields.items():
                if v==kw["assigned"]:
                    tosearch=k

            for item in so:
                if item.assign!=0 and item.assign!=tosearch:
                    lassigned.append(item.assign)
        menu =[]
        for element in range(0,18):
            if element in lassigned:
                pass
            else:
                selected=""
                if app_globals.masterFields[element]==kw["assigned"]:
                    selected="selected"
                menu.append(dict(id=str(element), name=app_globals.masterFields[element],selected=selected))
        assignformtemplate = render_template({"list": list,"field":kw["field"],"value":kw["value"],"multiplier":kw["multiplier"],"unit":kw["unit"],"menu":menu}, "mako", 'pythondispatchms.templates.admin.assignform')
        return dict(assignformtemplate=assignformtemplate)


    @expose('json')
    def getUsers(self,**kw):
        rows=[]
        imeiInfo=Rest()
        userData=imeiInfo.get(app_globals.sunUsers, {})
        for item in userData["users"]:
            rows.append({"username": item["username"], "email": item["email"]})
        rows = sorted(rows, key=lambda k: k['username'])
        return dict(rows=rows)

    @expose('json')
    def getGroups(self,**kw):
        rows=[]
        groups=requests.get(app_globals.sunGroups)
        groupsData=groups.json()
        for item in groupsData["groups"]:
            rows.append({"username": item["name"]})
        rows = sorted(rows, key=lambda k: k['username'])
        return dict(rows=rows)


    @expose('json')
    def getClients4Email(self,**kw):
        rows=[]
        imeiInfo=Rest()
        userData=imeiInfo.get(app_globals.sunApplications, {})
        for item in userData["applications"]:
            rows.append({"username": item["application_name"], "address": item["address"],"application_id": item["application_id"],"folio_sinube": item["folio_sinube"],"internal_id": item["internal_id"]})
        rows = sorted(rows, key=lambda k: k['username'])
        return dict(rows=rows)

    @expose('json')
    def loadListenerUsers(self, **kw):
        filter = [('userlisteners_id', 'eq', kw["id"])]
        return jqgridDataGrabber(ListenerUsers, 'id', filter, kw).loadGrid()

    @expose('json')
    def updateListenerUsers(self, **kw):
        filter = []
        return jqgridDataGrabber(ListenerUsers, 'id', filter, kw).updateGrid()

    @expose('json')
    def loadEvents(self, **kw):
        filter = [('listener_id', 'eq', kw["listener_id"])]
        return jqgridDataGrabber(Events, 'id', filter, kw).loadGrid()

    @expose('json')
    def updateEvents(self, **kw):
        if "event_id" in kw:
            if "listener_id" in kw:
                currentListener = DBSession.query(Events).filter_by(event_id=kw["event_id"],listener_id=kw["listener_id"]).first()
                if currentListener is not None:
                    Message.post("adminlistener", 'MSG' + "|" + "No puedo agregar evento ya existente")
                    return dict(dummy="")
        filter = []
        return jqgridDataGrabber(Events, 'id', filter, kw).updateGrid()

    @expose('json')
    def addUsersToListener(self,**kw):
        currentListener = DBSession.query(Listeners).filter_by(id=kw["id"]).first()
        if currentListener is not None:
            searchForUserinListener=DBSession.query(ListenerUsers).filter_by(userlisteners_id =kw["id"],user_name=kw["username"]).first()
            if searchForUserinListener is None:
                newUserListener=ListenerUsers()
                newUserListener.user_name=kw["username"]
                newUserListener.state=0
                currentListener.users.append(newUserListener)
                DBSession.add(newUserListener)
                DBSession.flush()

        return dict(dummy="")


    @expose('json')
    def loadGlobalExp(self, **kw):
        filter = [('explisteners_id', 'eq', kw["userlisteners_id"])]
        return jqgridDataGrabber(ListenerExpressions, 'id', filter, kw).loadGrid()

    @expose('json')
    def updateGlobalExp(self, **kw):
        filter = []
        if "oper" in kw:
            if kw["oper"]=="del":
                currentListener = DBSession.query(UserGlobalExp).filter_by(global_exp_id=kw["id"]).first()
                if currentListener is not None:
                    Message.post("adminlistener", 'MSG' + "|"+"Can not delete. Expression found un User-Triggers")
                    return dict(dummy="")
        return jqgridDataGrabber(ListenerExpressions, 'id', filter, kw).updateGrid()

    @expose('json')
    def loadExpressionsFormTemplate(self, **kw):
        list = []
        print("id:".format(kw["id"]))
        search = DBSession.query(ListenerFields).filter_by(listeners_id=kw["id"]).all()
        for item in search:
            if item.assign>0:
                list.append(app_globals.masterFields[item.assign])

        expressionformtemplate = render_template({"list": list}, "mako", 'pythondispatchms.templates.admin.expressionform')
        return dict(expressionformtemplate=expressionformtemplate)

    @expose('json')
    def addGlobalExp(self,**kw):
        field=str(kw["field"])
        operation=str(kw["operation"])
        value=str(kw["value"])
        print("value:{}".format(field+operation+value))
        if len(field)>0 and len(operation)>0 and len(value)>0:
            search = field + operation + value
            #exp_search = DBSession.query(ListenerExpressions).filter_by(expression=search).first()
            #if exp_search is None:
            currentListener = DBSession.query(Listeners).filter_by(id=kw["id"]).first()
            if currentListener is not None:
                newExpression=ListenerExpressions()
                newExpression.expression=search
                newExpression.expression_id=app_globals.inverseMasterFields[field]
                newExpression.expression_op=operation
                newExpression.expression_value=value
                currentListener.expressions.append(newExpression)
                DBSession.add(newExpression)
                DBSession.flush()
        return dict(dummy="")

    @expose('json')
    def addEmaillistener(self,**kw):
        email=str(kw["email"])
        password=str(kw["password"])
        smtp = str(kw["smtp"])
        port = str(kw["port"])
        client_id = str(kw["client_id"])
        client_name = str(kw["client_name"])
        imei = str(kw["imei"])
        internal_id = str(kw["internal_id"])
        event_id = str(kw["event_id"])
        event_desc = str(kw["event_desc"])
        # print("email:{}".format(email))
        # print("password:{}".format(password))
        # print("smtp:{}".format(smtp))
        # print("port:{}".format(port))
        if len(email)>0 and len(password)>0 and len(smtp)>0 and len(port)>0:
            exp_search = DBSession.query(EmailService).filter_by(email=email).first()
            if exp_search is None:
                sec_search = DBSession.query(EmailService).filter_by(event_desc=event_desc).first()
                if sec_search is None:
                    print("event desc not found")
                    parameters={}
                    parameters['imei'] = imei  # IMEI QUE TU ME QUIERAS DAR
                    parameters['status'] = 'DVR'  # DESCRIPCION DE DONDE ES TIENE HASTA 100 CARACTERES
                    parameters['application_id'] = client_id  # CLIENTE AL QUE PERTENECE, ESTE DATO TE LO MANDO CON SUN
                    parameters['server'] = 0  # SIEMPRE CERO PARA NO RELACIONARLO A NINGUNA PLATAFORMA
                    parameters['internal_id'] = internal_id  # INTERNAL ID AL QUE PERTENECE, ESTE DATO TE LO MANDO CON SUN
                    parameters['model'] = "Car"  # TABLA A LA QUE VAS A ACCEDER
                    parameters['expires'] = "2020-07-19 00:00:00"

                    ns = requests.session()

                    nkw = {'params': parameters, 'verify': False, 'timeout': 10}
                    response = ns.post(app_globals.domainpluto + "/rest", **nkw)
                    res = response.json()

                    ##pluto=Rest()
                    #res = pluto.delete(app_globals.domainpluto + "/rest", parameters)
                    ##res = pluto.post(app_globals.domainpluto + "/rest", parameters)
                    #connection=requests.post(app_globals.domainpluto + "/rest", parameters)
                    #res=connection.json()
                    #print("Result:{}".format(res))
                    if 'error' in res:
                        if res['error']=="ok":
                            # Result: {'error': 'ok'}
                            newExpression=EmailService()
                            newExpression.event_id = event_id
                            newExpression.event_desc = event_desc
                            newExpression.imei=imei
                            newExpression.password = password
                            newExpression.client_id=client_id
                            newExpression.client_name = client_name
                            newExpression.email=email
                            newExpression.smpt_server=smtp
                            newExpression.port = int(port)
                            DBSession.add(newExpression)
                            DBSession.flush()
                            Message.post("emaillistener",'MSG' + "|" + "Se agrego registro")
                    else:
                        Message.post("emaillistener", 'MSG' + "|" + "Pluton Rechazo la alta")
                else:
                    Message.post("emaillistener", 'MSG' + "|" + "Evento previamente definido")
            else:
                Message.post("emaillistener", 'MSG' + "|" + "Correo previamente definido")
        else:
            Message.post("emaillistener", 'MSG' + "|" + "Parametro faltante")
        return dict(dummy="")

    @expose('json')
    def loadTriggerByUser(self, **kw):
        filter = [('listener_users_id','eq',kw["user_id"])]
        return jqgridDataGrabber(UserTriggers, 'id', filter, kw).loadGrid()

    @expose('json')
    def updateTriggerByUser(self, **kw):
        filter=[]
        return jqgridDataGrabber(UserTriggers, 'id', filter, kw).updateGrid()

    @expose('json')
    def loadTriggerFormTemplate(self, **kw):
        list = []
        search = DBSession.query(ListenerExpressions).filter_by(explisteners_id =kw["id"]).all()
        count=0

        for item in search:
            count = count + 1
            value=item.expression
            #value=value.replace(" ","%20")
            list.append({"name":value,"ndx":count,"value":str(item.id)})


        triggerformtemplate = render_template({"list": list}, "mako",
                                                 'pythondispatchms.templates.admin.triggerform')
        return dict(triggerformtemplate=triggerformtemplate,count=str(count))

    @expose('json')
    def addUserTrigger(self,**kw):
        currentUser = DBSession.query(ListenerUsers).filter_by(id=kw["user_id"]).first()
        currentExpression=kw["expression"]
        if currentUser is not None:
            newTrigger = UserTriggers()
            newTrigger.expression = currentExpression.replace('%20',' ')
            newTrigger.priority = kw["priority"]
            newTrigger.sound = kw["sound"]
            currentUser.triggers.append(newTrigger)
            DBSession.add(newTrigger)
            DBSession.flush()
            currentTriggerId=newTrigger.id
            selectedFields = kw["selectedFields"]
            selectedFieldsList = selectedFields.split("|")
            for item in selectedFieldsList:
                print("item:{}".format(item))
                currentTrigger=DBSession.query(UserTriggers).filter_by(id=currentTriggerId).first()
                if currentTrigger is not None:
                    newuserglobalexp = UserGlobalExp()
                    newuserglobalexp.global_exp_id=item
                    currentTrigger.userglobalexp.append(newuserglobalexp)
                    DBSession.add(newuserglobalexp)
                    DBSession.flush()
        return dict(dummy="")

    @expose('json')
    def loadFilterByUser(self, **kw):
        filter = [('user_trigger_id','eq',kw["user_trigger_id"])]
        return jqgridDataGrabber(UserFilters, 'id', filter, kw).loadGrid()

    @expose('json')
    def updateFilterByUser(self, **kw):
        filter=[]
        return jqgridDataGrabber(UserFilters, 'id', filter, kw).updateGrid()

    @expose('json')
    def loadUserFilterTemplate(self, **kw):
        list = []
        expressionformtemplate = render_template({"list": list,"value":""}, "mako", 'pythondispatchms.templates.admin.userfilterform')
        return dict(expressionformtemplate=expressionformtemplate,value="")

    @expose('json')
    def addUserTriggerFilter(self,**kw):
        id=kw["id"]
        #filteroperation=kw["filteroperation"]
        fieldvalue=kw["fieldvalue"]
        #action=kw["action"]
        #resetoperation=kw["resetoperation"]
        resetvalue=kw["resetvalue"]
        numericAction=0
        #if action=="Keep":
        numericAction = 0
        store_exp="counter>"+fieldvalue
        exp_search = DBSession.query(UserFilters).filter_by(filter_id=1,user_trigger_id=id).first()
        if exp_search is None:
            currentUserTrigger = DBSession.query(UserTriggers).filter_by(id=kw["id"]).first()
            if currentUserTrigger is not None:
                newUserFilter = UserFilters()
                newUserFilter.filter_id=1
                newUserFilter.expression=store_exp
                newUserFilter.action=numericAction
                newUserFilter.reset_expression="counter>"+resetvalue
                currentUserTrigger.filters.append(newUserFilter)
                DBSession.add(newUserFilter)
                DBSession.flush()
        return dict(dummy="")


    @expose('pythondispatchms.templates.admin.emailservice')
    def emailListener(self,**kw):
        return dict(page='index',user=kw["user"])

    @expose('json')
    def loadEmailListener(self, **kw):
        filter = []
        return jqgridDataGrabber(EmailService, 'id', filter, kw).loadGrid()

    @expose('json')
    def updateEmailListener(self, **kw):
        filter = []
        return jqgridDataGrabber(EmailService, 'id', filter, kw).updateGrid()


    @expose('pythondispatchms.templates.admin.dedicated')
    def dedicated(self,**kw):
        return dict(page='index',user=kw["user"])


    @expose('json')
    def loadEmailListener(self, **kw):
        filter = []
        return jqgridDataGrabber(EmailService, 'id', filter, kw).loadGrid()

    @expose('json')
    def updateEmailListener(self, **kw):
        filter = []
        return jqgridDataGrabber(EmailService, 'id', filter, kw).updateGrid()


    @expose('json')
    def getClients4Dedicated(self,**kw):
        rows=[]
        imeiInfo=Rest()
        userData=imeiInfo.get(app_globals.sunapps+'?user=ivan', {})
        for item in userData["apps"]:
            rows.append({"username": item["application_name"], "address": item["address"],"application_id": item["application_id"],"folio_sinube": item["folio_sinube"],"internal_id": item["internal_id"]})
        rows = sorted(rows, key=lambda k: k['username'])
        return dict(rows=rows)


    @expose('json')
    def loadDedicatedMonitor(self, **kw):
        filter = []
        return jqgridDataGrabber(Dedicated, 'id', filter, kw).loadGrid()

    @expose('json')
    def updateDedicatedMonitor(self, **kw):
        filter = []
        return jqgridDataGrabber(Dedicated, 'id', filter, kw).updateGrid()

    @expose('json')
    def getDevices(self, **kw):
        rows = []
        pluto = Rest()
        parameters = {}
        parameters['application_id'] = kw['app_id']
        imeiData = pluto.get("https://pluto.dudewhereismy.com.mx/services/appID", parameters)
        for item in imeiData["cars"]:
            rows.append(
                {"imei": item["imei"], "eco": item["eco"], "brand": item["brand"],
                 "plates": item["plates"], "color": item["color"]})
        rows = sorted(rows, key=lambda k: k['eco'])
        return dict(rows=rows)

    @expose('pythondispatchms.templates.admin.roles')
    def roles(self,**kw):
        return dict(page='index',user=kw["user"])


    @expose('json')
    def loadRoles(self, **kw):
        filter = []
        return jqgridDataGrabber(Roles, 'id', filter, kw).loadGrid()

    @expose('json')
    def updateRoles(self, **kw):
        filter = []
        return jqgridDataGrabber(Roles, 'id', filter, kw).updateGrid()


    @expose('json')
    def loadWizard(self, **kw):
        list = []
        localtz = 'America/Mexico_City'
        oper_localtime = datetime.now(pytz.timezone(localtz))
        dedwizardtemplate = render_template({"list": list,"current_time":oper_localtime.strftime('%Y-%m-%dT%H:%M:%S'),'user':kw['user']}, "mako",kw['name'])
        return dict(dedwizardtemplate=dedwizardtemplate)

    @expose('json')
    def getGroups4Roles(self,**kw):
        rows=[]
        imeiInfo=Rest()
        groupData=imeiInfo.get('https://sun.dudewhereismy.mx/services/groupsTypes?id=2', {})
        for item in groupData["groups"]:
            rows.append({"groupname": item["group_name"]})
        rows = sorted(rows, key=lambda k: k['groupname'])
        return dict(rows=rows)

    @expose('json')
    def getUsersFromGroup(self, **kw):
        rows=[]
        imeiInfo=Rest()
        groupData=imeiInfo.get('https://sun.dudewhereismy.mx/services/groupsTypes?id=2', {})
        for item in groupData["groups"]:
            if item['group_name']==kw['group']:
                for element in item['users']:
                    rows.append({"user": element})
        rows = sorted(rows, key=lambda k: k['user'])
        return dict(rows=rows)


    @expose('json')
    def saveWizardRoles(self, **kw):
        rows = []
        print(kw['rolname'])
        print(kw['group-name'])
        print(kw['users'])
        userList=kw['users'].split(',')
        query = DBSession.query(Roles).filter_by(name=kw['rolname']).first()
        if query is None:
            nr=Roles()
            nr.name=kw['rolname']
            nr.group = kw['group-name']
            DBSession.add(nr)
            for item in userList:
                ru=RolUsers()
                ru.user_name=item
                nr.users.append(ru)
                DBSession.add(ru)
            DBSession.flush()
            Message.post("rolelistener", 'RELOAD' + "|")
            Message.post("rolelistener", 'MSG' + "|" + "Rol nuevo.")
        else:
            Message.post("rolelistener", 'MSG' + "|" + "Rol Existente.")
        return dict(rows=rows)


    @expose('json')
    def getUsersFromRole(self, **kw):
        rows=[]
        query=DBSession.query(Roles).filter_by(name=kw['rolname']).first()
        if query is not None:
            for item in query.users:
                rows.append({"user": item.user_name})
        rows = sorted(rows, key=lambda k: k['user'])
        return dict(rows=rows)


    @expose('json')
    def getRol(self, **kw):
        rows = []
        query = DBSession.query(Roles).all()
        for item in query:
            users_csv=''
            for element in item.users:
                users_csv=users_csv+element.user_name+','
            rows.append({"rol": item.name, "users":users_csv[:-1]})
        rows = sorted(rows, key=lambda k: k['rol'])
        return dict(rows=rows)

    @expose('json')
    def saveWizardDedicate(self, **kw):
        rows = []

        # print(kw['nameEvent'])
        # print(kw['startDate'])
        # print(kw['endDate'])
        # print(kw['interval'])
        # print(kw['app-id'])
        # print(kw['app-name'])
        # print(kw['imeis'])
        pluto = Rest()
        parameters = {}
        parameters['application_id'] = kw['app-id']
        imeiData = pluto.get("https://pluto.dudewhereismy.com.mx/services/appID", parameters)
        imeisList = kw['imeis'].split(',')
        query = DBSession.query(Dedicated).filter_by(name=kw['nameEvent']).first()
        if query is None:
            dd = Dedicated()
            dd.name = kw['nameEvent']
            dd.start =kw['startDate']
            dd.end = kw['endDate']
            dd.interval = kw['interval']
            dd.application_id = kw['app-id']
            dd.application_name = kw['app-name']
            dd.state = 0
            dd.role = kw['role']
            DBSession.add(dd)
            for item in imeisList:
                dv = Devices()
                dv.imei = item
                for element in imeiData["cars"]:
                    if element["imei"]==item:
                        dv.description=str(element["eco"])+"|"+str(element["brand"])+"|"+str(element["model"])+"|"+str(element["color"])+"|"+str(element["plates"])
                dd.devices.append(dv)
                DBSession.add(dv)
            sd=datetime.strptime(kw['startDate'], '%Y-%m-%dT%H:%M:%S')
            ed=datetime.strptime(kw['endDate'], '%Y-%m-%dT%H:%M:%S')
            query = DBSession.query(TempCalendars).filter_by(user_name=kw["user"]).all()
            for each in query:
                cal = Calendars()
                cal.day = each.day
                cal.h00 = each.h00
                cal.h01 = each.h01
                cal.h02 = each.h02
                cal.h03 = each.h03
                cal.h04 = each.h04
                cal.h05 = each.h05
                cal.h06 = each.h06
                cal.h07 = each.h07
                cal.h08 = each.h08
                cal.h09 = each.h09
                cal.h10 = each.h10
                cal.h11 = each.h11
                cal.h12 = each.h12
                cal.h13 = each.h13
                cal.h14 = each.h14
                cal.h15 = each.h15
                cal.h16 = each.h16
                cal.h17 = each.h17
                cal.h18 = each.h18
                cal.h19 = each.h19
                cal.h20 = each.h20
                cal.h21 = each.h21
                cal.h22 = each.h22
                cal.h23 = each.h23
                dd.calendars.append(cal)
                DBSession.add(cal)
            # for x in range(0, (ed - sd).days+1):
            #     nd=sd+timedelta(days=x)
            #     cal=Calendars()
            #     cal.day=nd
            #     dd.calendars.append(cal)
            #     DBSession.add(cal)
            DBSession.flush()
            Message.post("dedicatedlistener", 'RELOAD' + "|")
            Message.post("dedicatedlistener", 'MSG' + "|" + "Evento Monitoreo Dedicado nuevo.")
        else:
            Message.post("dedicatedlistener", 'MSG' + "|" + "Evento Monitoreo Dedicado Existente.")
        return dict(rows=rows)


    @expose('json')
    def getImeisFromDedicated(self, **kw):
        rows=[]
        query=DBSession.query(Dedicated).filter_by(name=kw['dedname']).first()
        if query is not None:
            for item in query.devices:
                rows.append({"imei": item.imei})
                print(item.imei)
        rows = sorted(rows, key=lambda k: k['imei'])
        return dict(rows=rows)

    @expose('json')
    def updateMonitorState(self, **kw):
        query = DBSession.query(Dedicated).filter_by(id=kw["id"]).first()
        if query is not None:
            if query.state==1:
                query.state=0
            else:
                query.state=1
            DBSession.flush()
            Message.post("dedicatedlistener", 'RELOAD' + "|" )

    @expose('json')
    def loadMonitorDevices(self, **kw):
        filter = [('dedicated_id', 'eq', kw["id"])]
        return jqgridDataGrabber(Devices, 'id', filter, kw).loadGrid()

    @expose('json')
    def updateMonitorDevices(self, **kw):
        filter = [('dedicated_id', 'eq', kw["id"])]
        return jqgridDataGrabber(Devices, 'id', filter, kw).updateGrid()

    @expose('json')
    def loadMonitorCalendars(self, **kw):
        filter = [('dedicated_id', 'eq', kw["id"])]
        return jqgridDataGrabber(Calendars, 'id', filter, kw).loadGrid()

    @expose('json')
    def updateMonitorCalendars(self, **kw):
        filter = [('dedicated_id', 'eq', kw["id"])]
        return jqgridDataGrabber(Calendars, 'id', filter, kw).updateGrid()

    @expose('json')
    def loadMonitorTempCalendars(self, **kw):
        filter = [('user_name', 'eq', kw["user_name"])]
        return jqgridDataGrabber(TempCalendars, 'id', filter, kw).loadGrid()

    @expose('json')
    def updateMonitorTempCalendars(self, **kw):
        filter = [('user_name', 'eq', kw["user_name"])]
        return jqgridDataGrabber(TempCalendars, 'id', filter, kw).updateGrid()

    @expose('json')
    def createTempCalendar(self, **kw):
        query = DBSession.query(TempCalendars).filter_by(user_name=kw["user"]).all()
        for item in query:
            DBSession.delete(item)
            DBSession.flush()
        sd = datetime.strptime(kw['startDate'], '%Y-%m-%dT%H:%M:%S')
        ed = datetime.strptime(kw['endDate'], '%Y-%m-%dT%H:%M:%S')
        for x in range(0, (ed - sd).days + 1):
            nd = sd + timedelta(days=x)
            newTmpCalendar=TempCalendars()
            newTmpCalendar.day=nd
            newTmpCalendar.user_name = kw['user']
            DBSession.add(newTmpCalendar)
            DBSession.flush()
        return dict(rows='')
