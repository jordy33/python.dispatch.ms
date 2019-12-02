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
from pythondispatchms.model.tables import Devices
from pythondispatchms.lib.messagequeue import Message
from pythondispatchms.lib.jqgrid import jqgridDataGrabber
import requests
from pythondispatchms.lib.rest import Rest

__all__ = ['SmartPhonesController']

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

class SmartPhonesController(BaseController):

    #allow_only = predicates.not_anonymous()

    @expose('pythondispatchms.templates.devices.devices')
    def index(self, **kw):
        return dict(dummy="",user="dispatch")

    @expose('json')
    def loadDevices(self, **kw):
        filter = []
        return jqgridDataGrabber(Devices, 'id', filter, kw).loadGrid()

    @expose('json')
    def updateDevices(self, **kw):
        filter = []
        return jqgridDataGrabber(Devices, 'id', filter, kw).updateGrid()

    # @expose('json')
    # def loadDevicesFields(self, **kw):
    #     filter = [('listenerlog_id','eq',kw["id"])]
    #     return jqgridDataGrabber(ListenerLogFields, 'id', filter, kw).loadGrid()
    #
    # @expose('json')
    # def updateDevicesFields(self, **kw):
    #     filter=[]
    #     return jqgridDataGrabber(ListenerLogFields, 'id', filter, kw).updateGrid()
    #
    # @expose('json')
    # def loadDevicesUsers(self, **kw):
    #     filter = [('listenerlog_id', 'eq', kw["id"])]
    #     return jqgridDataGrabber(ListenerLogUsers, 'id', filter, kw).loadGrid()
    #
    # @expose('json')
    # def updateDeviceUsers(self, **kw):
    #     filter = []
    #     return jqgridDataGrabber(ListenerLogUsers, 'id', filter, kw).updateGrid()

