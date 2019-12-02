from pythondispatchms.lib.base import BaseController
from pythondispatchms.model import DBSession, User,Notification
from pythondispatchms.lib.jqgrid import jqgridDataGrabber
from tg import expose, request
import datetime

class NotificationController(BaseController):

    # MQTT
    @expose('json')
    def loadNotification(self, **kw):
        item = DBSession.query(User).filter_by(user_name=request.identity['repoze.who.userid']).first()
        return jqgridDataGrabber(Notification, 'user_id', [('user_id', 'eq', str(item.user_id) )], kw).loadGrid()

    @expose('json')
    def getBadge(self, **kw):
        user = DBSession.query(User).filter_by(user_name=request.identity['repoze.who.userid']).first()
        counter=DBSession.query(Notification).filter_by(user_id=user.user_id,attended_state='N').count()
        return dict(badge='' if counter == 0 else str(counter))

    @expose('json')
    def updateBadge(self, **kw):
        record = kw['record']
        user = DBSession.query(User).filter_by(user_name=request.identity['repoze.who.userid']).first()
        notification=DBSession.query(Notification).filter_by(id=record).first()
        if notification is not None:
            notification.attended_state="Y"
            notification.attended_time=datetime.datetime.utcnow()
            DBSession.flush()
        counter = DBSession.query(Notification).filter_by(user_id=user.user_id, attended_state='N').count()
        return dict(badge='' if counter == 0 else str(counter))