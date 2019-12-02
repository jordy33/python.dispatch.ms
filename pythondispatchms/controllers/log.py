# -*- coding: utf-8 -*-
"""Sample controller with all its actions protected."""
from tg import expose, flash
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tg import predicates,app_globals
from pythondispatchms.lib.base import BaseController
from pythondispatchms.lib.decorators import restErrorHandler
from pythondispatchms.lib.graphs import GraphApi

import datetime
from random import randint
from pythondispatchms.model import DBSession, User,Notification
from pythondispatchms.model.tables import ListenerLog,ListenerLogFields,ListenerLogUsers
from pythondispatchms.lib.messagequeue import Message
from pythondispatchms.lib.jqgrid import jqgridDataGrabber
import requests
from pythondispatchms.lib.rest import Rest

__all__ = ['LogController']

import stomp

class MyListener(stomp.ConnectionListener):
    def on_message(self, headers, message):
        print('MyListener:\nreceived a message "{}"\n'.format(message))
        global read_messages
        read_messages.append({'id': headers['message-id'], 'subscription':headers['subscription']})


class MyStatsListener(stomp.StatsListener):
    def on_disconnected(self):
        super(MyStatsListener, self).on_disconnected()
        print('MyStatsListener:\n{}\n'.format(self))

class LogController(BaseController):

    #allow_only = predicates.not_anonymous()

    @expose('pythondispatchms.templates.log.log')
    def index(self, **kw):
        return dict(dummy="",user="dispatch")

    @expose('json')
    def loadLog(self, **kw):
        filter = []
        return jqgridDataGrabber(ListenerLog, 'id', filter, kw).loadGrid()

    @expose('json')
    def updateLog(self, **kw):
        filter = []
        return jqgridDataGrabber(ListenerLog, 'id', filter, kw).updateGrid()

    @expose('json')
    def loadLogFields(self, **kw):
        filter = [('listenerlog_id','eq',kw["id"])]
        return jqgridDataGrabber(ListenerLogFields, 'id', filter, kw).loadGrid()

    @expose('json')
    def updateLogFields(self, **kw):
        filter=[]
        return jqgridDataGrabber(ListenerLogFields, 'id', filter, kw).updateGrid()

    @expose('json')
    def loadLogUsers(self, **kw):
        filter = [('listenerlog_id', 'eq', kw["id"])]
        return jqgridDataGrabber(ListenerLogUsers, 'id', filter, kw).loadGrid()

    @expose('json')
    def updateLogUsers(self, **kw):
        filter = []
        return jqgridDataGrabber(ListenerLogUsers, 'id', filter, kw).updateGrid()

