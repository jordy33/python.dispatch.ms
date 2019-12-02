from tg import request
from pythondispatchms.model import DBSession
from sqlalchemy import or_
from pythondispatchms.model.auth import User
from pythondispatchms.model.tables import Notification, Traffic

class Statistics(object):

    def __init__(self):
        self._attended=0
        self._toattend=0
        self._closed=0
        self._score=0
        self._counter=0

    def byUser(self,user):
        user_list=user.split(",")
        alerts =DBSession.query(Traffic).filter(Traffic.user.in_(user_list)).all()
        for element in alerts:
            if (element.attended_state=="N" and element.only==1):
                self._counter = self._counter + 1
                self._toattend=self._toattend+1
            if ((element.attended_state=="A" and element.only==1) or (element.attended_state=="P" and element.only==1)):
                self._counter = self._counter + 1
                self._attended=self._attended+1
            if (element.attended_state=="C" and element.only==1):
                self._counter = self._counter + 1
                self._closed=self._closed+1
        if (self._counter>0):
            self._score=(self._closed*100/self._counter*100)/100
        return dict(user=user,attended_statistic=self._attended, toattend_statistic=self._toattend, closed_statistic=self._closed, score_statistic=self._score)