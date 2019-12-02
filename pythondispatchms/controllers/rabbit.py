# -*- coding: utf-8 -*-
"""Sample controller with all its actions protected."""
from tg import expose, flash,request,predicates,app_globals
from tg.i18n import ugettext as _, lazy_ugettext as l_
from pythondispatchms.lib.base import BaseController
from pythondispatchms.lib.decorators import restErrorHandler

import requests

from tg import app_globals
__all__ = ['RabbitController']



class RabbitController(BaseController):
    allow_only = predicates.not_anonymous()

    @expose('json')
    def countsessions(self, **kw):
        if "user" in kw:
            # url=app_globals.host_prefix+app_globals.stompHost+":15672/api/connections"
            # response = requests.get(url, auth=(app_globals.stompUserName, app_globals.stompPassword), verify=False)
            # count=0
            # for item in response.json():
            #     user=item["user"]
            #     if (user==request.identity['repoze.who.userid']):
            #         count=count+1
            count=0
            return dict(count=count)
        else:
            return dict(error="Missing user parameter")

    @expose('json')
    def createuser(self,**kw):
        if "user" in kw:
            newUser=kw["user"]
            url=app_globals.host_prefix+app_globals.stompHost+":15672/api/users/"+newUser
            headers = {'Content-type': 'application/json'}
            data = '{"password":"gpscontrol1","tags":"none"}'
            r = requests.put(url, auth=(app_globals.stompUserName, app_globals.stompPassword),headers=headers,data=data, verify=False)
            url =app_globals.host_prefix+app_globals.stompHost+":15672/api/permissions/%2f/"+newUser
            data = '{"configure":".*","write":".*","read":".*"}'
            r = requests.put(url, auth=(app_globals.stompUserName, app_globals.stompPassword),headers=headers,data=data, verify=False)
            return dict(status="User created")
        else:
            return dict(error="no parameters")

    @expose('json')
    def deleteuser(self,**kw):
        if "user" in kw:
            newUser=kw["user"]
            url=app_globals.host_prefix+app_globals.stompHost+":15672/api/users/"+newUser
            headers = {'Content-type': 'application/json'}
            data = '{"password":"gpscontrol1","tags":"none"}'
            r = requests.delete(url, auth=(app_globals.stompUserName, app_globals.stompPassword),headers=headers,data=data, verify=False)
            return dict(status="User deleted")
        else:
            return dict(error="no parameters")



