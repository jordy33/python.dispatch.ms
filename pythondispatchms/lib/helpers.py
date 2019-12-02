# -*- coding: utf-8 -*-
"""Template Helpers used in python.sun."""
import logging
from markupsafe import Markup
from datetime import datetime
from tg import request
from pythondispatchms.model import DBSession,User, Notification, Permission
from tg import app_globals

log = logging.getLogger(__name__)


def current_year():
    now = datetime.now()
    return now.strftime('%Y')

def today():
    now = datetime.now()
    return now.strftime('%d / %m / %y')

def icon(icon_name):
    return Markup('<i class="glyphicon glyphicon-%s"></i>' % icon_name)

def badge():
    if request.identity is None:
        counter = 0
    else:
        identity = request.identity['repoze.who.userid']
        user = DBSession.query(User).filter_by(user_name=identity).first()
        counter = DBSession.query(Notification).filter_by(user_id=user.user_id, attended_state="N").count()
    return '' if counter == 0 else str(counter)

def whoami():
    try:
        ret=request.identity["repoze.who.userid"]
    except:
        return ""
    else:
        return ret

def password():
        return 'gpscontrol1'

def perm(name):
    identity = request.identity['repoze.who.userid']
    user = DBSession.query(User).filter_by(user_name=identity).first()
    perm = Permission.exist(u''+name+'',user.groups)
    if perm == "si":
        return True
    else:
        return False

# def url():
#     return app_globals.host

def url():
    return app_globals.host
    #"https://dispatch.dudewhereismy.mx"

def stompServer():
    return app_globals.stompServer

def stompUser():
    return app_globals.stompUserName

def stompPassword():
    return app_globals.stompPassword

# Import commonly used helpers from WebHelpers2 and TG
from tg.util.html import script_json_encode

try:
    from webhelpers2 import date, html, number, misc, text
except SyntaxError:
    log.error("WebHelpers2 helpers not available with this Python Version")