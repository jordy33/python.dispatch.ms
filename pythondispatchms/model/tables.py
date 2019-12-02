from pythondispatchms.model import DeclarativeBase, DBSession

from sqlalchemy import Column, Integer, Date, Text, Unicode, Boolean, Numeric,Float,LargeBinary
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.types import DateTime
from datetime import datetime
from sqlalchemy.orm import relation,backref,relationship
from sqlalchemy import ForeignKey

class Notification(DeclarativeBase):
    __tablename__ = 'notification'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,default=0)
    time_stamp = Column(DateTime, default=datetime.now)
    message = Column(Unicode(255), default=u'')
    attended_time = Column(DateTime, default=datetime.now)
    attended_state = Column(Unicode(1), default=u'N')

    def __repr__(self):
        return '<Notification: time_stamp=%s, message=%s, attended_state=%s>' % (
            repr(self.time_stamp),
            repr(self.message),
            repr(self.attended_state)
        )

    def __unicode__(self):
        return self.message

#create index user_attended_state_index on traffic(user,attended_state);
#SHOW INDEX FROM traffic;

class Jobs(DeclarativeBase):
    __tablename__ ='jobs'
    id = Column(Integer, primary_key=True)
    job_id = Column(Unicode(25), default="")
    job_date = Column(DateTime, default=datetime.utcnow())
    job_description = Column(Unicode(255), default="")
    job_state = Column(Unicode(30), default="")
    comment = Column(Unicode(254), default="")
    latitude = Column(Numeric(10,6),default=0)
    longitude = Column(Numeric(11,6),default=0)
    creation_date = Column(DateTime, default=datetime.utcnow())
    last_update = Column(DateTime, default=datetime.utcnow())
    gate_user = Column(Unicode(254), default="")


class Smartphones(DeclarativeBase):
    __tablename__ ='smartphones'
    id = Column(Integer, primary_key=True)
    imei = Column(Unicode(16), default=u"")
    creation_date = Column(DateTime,default=datetime.utcnow())
    lastupdate = Column(DateTime, default=datetime.utcnow())
    platform = Column(Unicode(1), default=u"")
    gate_user = Column(Unicode(254), default="")
    gate_password = Column(Unicode(254), default="")
    gate_app = Column(Unicode(254), default="")
    latitude = Column(Numeric(10,6),default=0)
    longitude = Column(Numeric(11,6),default=0)
    password = Column(Unicode(4), default=u"")
    speed = Column(Float, default=0)
    token = Column(Unicode(255), default=u"")
    account = Column(Unicode(64), index=True, default=u"")
    battery = Column(Integer,default=0)
    accuracy = Column(Numeric(10,6),default=0)
    lastpanic = Column(DateTime)
    paniclatitude = Column(Numeric(11,6),default=0)
    paniclongitude = Column(Numeric(11,6),default=0)
    panicspeed = Column(Float,default=0)
    panicbattery = Column(Integer,default=0)
    time4gps = Column(Unicode(2), default="40")
    intervaltime = Column(Unicode(2), default="10")
    distance4update = Column(Unicode(3), default="10")
    state = Column(Integer,default=0)
    last_sn = Column(DateTime)
    log = Column(Text(), default=u"")
    recurrent_credit = Column(Integer, default=0)
    last_status = Column(DateTime,default=datetime.utcnow())

class ReservedImages(DeclarativeBase):
    __tablename__ = 'reserved_images'
    id = Column(Integer,primary_key=True)
    image = Column(LargeBinary(length=(2 ** 32) - 1))
    code = Column(Unicode(50))
    extra = Column(Unicode(50))
    job_id = Column(Unicode(25), default="")
    w = Column(Integer)
    h = Column(Integer)


class Traffic(DeclarativeBase):
    __tablename__ ='traffic'
    id = Column(Integer, primary_key=True)
    attended_state = Column(Unicode(1),default=u'N')
    priority = Column(Integer,default=3)
    user_name = Column(Unicode(150), default=u'')
    event_id= Column(Integer,default=0)
    event_desc = Column(Unicode(255), default=u'')
    vehicle = Column(Unicode(255), default=u'')
    time_stamp = Column(DateTime, default=datetime.utcnow)
    attended_time = Column(DateTime, default=datetime.utcnow)
    pending_time = Column(DateTime, default=datetime.utcnow)
    closed_time = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer,default=0)
    imei = Column(Unicode(16), default=u'')
    latitude = Column(Numeric(10,6),default=0)
    longitude = Column(Numeric(11,6),default=0)
    speed = Column(Numeric(10,2),default=0)
    azimuth= Column(Numeric(10, 6))
    listener = Column(Integer, default=0)
    valid = Column(Unicode(1), default=u'')
    comment = Column(Text(), default=u'')
    callercomment = Column(Text(), default=u'')
    false_alarm = Column(Boolean,default=False)
    event_time = Column(DateTime, default=datetime.utcnow)
    speedunit = Column(Unicode(25), default=u'')
    only = Column(Integer, default=1)
    internal_id = Column(Unicode(10), default=u'')
    client_id = Column(Unicode(10), default=u'')
    user = Column(Unicode(16))
    voltage = Column(Integer, default=0)
    mcc = Column(Integer, default=0)
    mnc = Column(Integer, default=0)
    lac = Column(Integer, default=0)
    cellid = Column(Integer, default=0)
    dedicated_id = Column(Integer, default=0)

class logImei(DeclarativeBase): #NEVER DELETE FOR NOW
    __tablename__ = 'logImei'
    id = Column(Integer, primary_key=True)
    user_filters_id=Column(Integer, default=0) # 6am -> 12pm
    imei = Column(Unicode(16))
    group_name = Column(Unicode(16), default=u'', nullable=False)
    event_desc = Column(Unicode(255))
    morning = Column(Integer, default=0) # 6am -> 12pm
    afternoon = Column(Integer, default=0) # 12pm -> 6pm
    night = Column(Integer, default=0) # 6pm -> 12am
    early_morning = Column(Integer, default=0) # 12am -> 6am
    counter = Column(Integer, default=0)
    weekday = Column(Unicode(10))
    time_stamp= Column(DateTime, default=datetime.utcnow)
    hour = Column(Integer, default=0) # 12am -> 6am
    hour_counter = Column(Integer, default=0) # 12am -> 6am


class imeiTicket(DeclarativeBase):
    __tablename__ = 'imeiTicket'
    id = Column(Integer, primary_key=True)
    imei = Column(Unicode(16), default=u'')
    ticket = Column(Integer,default=0)

class imeiCommented(DeclarativeBase):
    __tablename__ = 'imeiCommented'
    id = Column(Integer, primary_key=True)
    imei = Column(Unicode(16), default=u'')
    commented = Column(Unicode(20), default=u'')

class Pending(DeclarativeBase):
    __tablename__ = 'pending'
    id = Column(Integer, primary_key=True)
    traffic_id = Column(Integer,default=0)
    pending_date = Column(DateTime, default=datetime.now)
    data = Column(Text())


class Events(DeclarativeBase):
    __tablename__='events'
    id = Column(Integer, primary_key=True)
    event_id = Column(Integer)
    event_desc = Column(Unicode(255))
    listener_id = Column(Unicode(255), default=u'')


class Tickets(DeclarativeBase):
    __tablename__ = 'tickets'
    id = Column(Integer, primary_key=True)
    traffic_id = Column(Integer,default=0)
    ticket = Column(Integer,default=0)
    last_report = Column(DateTime, default=datetime.utcnow)
    comment= Column(Unicode(255), default=u'')

class Images(DeclarativeBase):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True)
    traffic_id = Column(Integer,default=0)
    data = Column(LargeBinary(length=(2 ** 32) - 1))

class Relation(DeclarativeBase):
    __tablename__ = 'relations'
    id = Column(Integer, primary_key=True)
    imei = Column(Unicode(32), default=u'')
    contact_id = Column(Integer)

class helpComment(DeclarativeBase):
    __tablename__ = 'helpComment'
    id = Column(Integer, primary_key=True)
    comment = Column(Unicode(100))

class Listeners (DeclarativeBase):
    __tablename__ ='listeners'
    id = Column(Integer, primary_key=True)
    listener_id = Column(Unicode(255), default=u'')
    name = Column(Unicode(255), default=u'')
    time_stamp = Column(DateTime, default=datetime.utcnow)
    state = Column(Boolean, default=False)
    logstate = Column(Boolean, default=False)
    fields = relationship('ListenerFields', cascade="all,delete", backref='listeners')
    users  = relationship('ListenerUsers', cascade="all,delete", backref='listeners')
    expressions = relationship('ListenerExpressions', cascade="all,delete", backref='listeners')

class ListenerFields (DeclarativeBase):
    __tablename__ ='listenerfields'
    id = Column(Integer, primary_key=True)
    field = Column(Unicode(255),default=u'')
    value = Column(Unicode(255),default=u'')
    assign = Column(Integer,default=0)
    multiplier = Column(Float, default=1)
    unit = Column(Unicode(25), default=u'')
    listeners_id = Column(Integer, ForeignKey('listeners.id'))

class ListenerExpressions (DeclarativeBase):
    __tablename__ ='listenerexps'
    id = Column(Integer, primary_key=True)
    expression = Column(Unicode(255), nullable=False)
    expression_id = Column(Integer, default=0)
    expression_op = Column(Unicode(255), nullable=False,default=u'')
    expression_value = Column(Unicode(255), nullable=False,default=u'')
    explisteners_id = Column(Integer, ForeignKey('listeners.id'))

class ListenerUsers (DeclarativeBase):
    __tablename__ ='listenerusers'
    id = Column(Integer, primary_key=True)
    user_name = Column(Unicode(16), nullable=False,default=u'')
    state = Column(Boolean, default=False)
    finalize = Column(Boolean, default=True)
    userlisteners_id = Column(Integer, ForeignKey('listeners.id'))
    triggers = relationship('UserTriggers', cascade="all,delete", backref='listenerusers')

class UserTriggers(DeclarativeBase):
    __tablename__ = 'usertriggers'
    id = Column(Integer, primary_key=True)
    expression = Column(Unicode(255), nullable=False,default=u'')
    priority = Column(Integer,default=0)
    sound = Column(Integer, default=1)
    listener_users_id = Column(Integer, ForeignKey('listenerusers.id'))
    userglobalexp =relationship('UserGlobalExp',cascade="all,delete", backref='usertriggers')
    filters = relationship('UserFilters', cascade="all,delete", backref='usertriggers')

class UserGlobalExp(DeclarativeBase):
    __tablename__ = 'userglobalexp'
    id = Column(Integer, primary_key=True)
    global_exp_id = Column(Integer,default=0)
    usertriggers_id= Column(Integer, ForeignKey('usertriggers.id'))

class UserFilters(DeclarativeBase):
    __tablename__ = 'userfilters'
    id = Column(Integer, primary_key=True)
    filter_id = Column(Integer, default=0)
    expression = Column(Unicode(255), nullable=False, default=u'')
    action = Column(Boolean, default=False)
    reset_expression = Column(Unicode(255), nullable=False, default=u'')
    counter = Column(Float, default=0)
    user_trigger_id = Column(Integer, ForeignKey('usertriggers.id'))

class ListenerLog(DeclarativeBase):
    __tablename__ ='listenerlog'
    id = Column(Integer, primary_key=True)
    time_stamp = Column(DateTime, default=datetime.now)
    listener_id = Column(Unicode(255), default=u'')
    mapper_state = Column(Integer, default=0)
    imei = Column(Unicode(16), default=u'')
    fields = relationship('ListenerLogFields', cascade="all,delete", backref='listenerlog')
    users = relationship('ListenerLogUsers', cascade="all,delete", backref='listenerlog')

class ListenerLogFields(DeclarativeBase):
    __tablename__ ='listenerlogfields'
    id = Column(Integer, primary_key=True)
    field = Column(Unicode(255),default=u'')
    isfieldfound = Column(Boolean,default=False)
    assigned_to = Column(Integer, default=0)
    value = Column(Unicode(255),default=u'')
    expression = Column(Unicode(255), nullable=False, default=u'')
    expression_state = Column(Boolean,default=False)
    received = Column(Unicode(255),default=u'')
    listenerlog_id = Column(Integer, ForeignKey('listenerlog.id'))

class ListenerLogUsers(DeclarativeBase):
    __tablename__ ='listenerlogusers'
    id = Column(Integer, primary_key=True)
    user_name = Column(Unicode(16), nullable=False,default=u'')
    trigger_expr = Column(Unicode(255), nullable=False, default=u'')
    trigger_expr_state = Column(Boolean,default=False)
    filter_expr = Column(Unicode(255), nullable=False, default=u'')
    filter_expr_state = Column(Boolean,default=False)
    listenerlog_id = Column(Integer, ForeignKey('listenerlog.id'))

class EmailService(DeclarativeBase):
    __tablename__ = 'emailservice'
    id = Column(Integer, primary_key=True)
    event_id= Column(Integer,default=0)
    event_desc = Column(Unicode(255), default=u'')
    client_id = Column(Unicode(10), default=u'')
    client_name = Column(Unicode(150), default=u'')
    imei = Column(Unicode(16), default=u'')
    email = Column(Unicode(255), nullable=False, default=u'')
    password = Column(Unicode(255), nullable=False, default=u'')
    smpt_server = Column(Unicode(255), nullable=False, default=u'')
    port = Column(Integer, default=0)
    latitude = Column(Numeric(10,6),default=0)
    longitude = Column(Numeric(11,6),default=0)

class EmailData(DeclarativeBase):
    __tablename__ = 'emaildata'
    id = Column(Integer, primary_key=True)
    imei = Column(Unicode(16), default=u'')
    time_stamp = Column(DateTime, default=datetime.utcnow)
    email_id = Column(Unicode(255), default=u'')
    data = Column(LONGTEXT(), default=u'')


class OperatorLog(DeclarativeBase):
    __tablename__ ='operatorslog'
    id = Column(Integer, primary_key=True)
    time_stamp = Column(DateTime, default=datetime.utcnow)
    user_name = Column(Unicode(16),default=u'', nullable=False)
    group_name = Column(Unicode(256),default=u'', nullable=False)
    operation = Column(Integer, default=0)
    traffic_id = Column(Integer, default=0)
    ticket = Column(Unicode(255), default=u'')

    def __repr__(self):
        return '<Group: name=%s>' % repr(self.group_name)

    def __unicode__(self):
        return self.group_name


    #operation
    #          1 --> Look Traffic Detail
    #          2 --> Put Pending
    #          3 --> Create Ticket
    #          4 --> Finalize Traffic
    #          5 --> C5 Alarm
    #          6 --> Add Image
    #          7 --> Telefonica Location

    @classmethod
    def addLog(cls, **kw):
        newLog = cls(**kw)
        DBSession.add(newLog)
        DBSession.flush()

class Dedicated(DeclarativeBase):
    __tablename__ = 'dedicated'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(30),default=u'')
    start = Column(DateTime, default=datetime.now)
    end = Column(DateTime, default=datetime.now)
    interval = Column(Integer, default=0)
    application_id = Column(Integer, default=0)
    application_name = Column(Unicode(30), default=u'')
    role = Column(Unicode(30))
    state = Column(Boolean, default=True)

    devices = relationship('Devices',cascade="all,delete", backref='dedicated')
    calendars = relationship('Calendars', cascade="all,delete", backref='dedicated')

class Devices(DeclarativeBase):
    __tablename__ = 'devices'
    id = Column(Integer, primary_key=True)
    imei = Column(Unicode(30),default=u'', nullable=False)
    description = Column(Unicode(255),default=u'', nullable=False)
    driver_name = Column(Unicode(30), default=u'')
    password = Column(Unicode(255), default=u'')
    phone1 = Column(Unicode(30), default=u'')
    phone2 = Column(Unicode(30), default=u'')
    phone3 = Column(Unicode(30), default=u'')
    obs = Column(Text(), default=u'')
    dedicated_id = Column(Integer, ForeignKey('dedicated.id'))

class Calendars(DeclarativeBase):
    __tablename__ = 'calendars'
    id = Column(Integer, primary_key=True)
    day = Column(DateTime, default=datetime.now)
    h00 = Column(Unicode(2), default='Si')
    h01 = Column(Unicode(2), default='Si')
    h02 = Column(Unicode(2), default='Si')
    h03 = Column(Unicode(2), default='Si')
    h04 = Column(Unicode(2), default='Si')
    h05 = Column(Unicode(2), default='Si')
    h06 = Column(Unicode(2), default='Si')
    h07 = Column(Unicode(2), default='Si')
    h08 = Column(Unicode(2), default='Si')
    h09 = Column(Unicode(2), default='Si')
    h10 = Column(Unicode(2), default='Si')
    h11 = Column(Unicode(2), default='Si')
    h12 = Column(Unicode(2), default='Si')
    h13 = Column(Unicode(2), default='Si')
    h14 = Column(Unicode(2), default='Si')
    h15 = Column(Unicode(2), default='Si')
    h16 = Column(Unicode(2), default='Si')
    h17 = Column(Unicode(2), default='Si')
    h18 = Column(Unicode(2), default='Si')
    h19 = Column(Unicode(2), default='Si')
    h20 = Column(Unicode(2), default='Si')
    h21 = Column(Unicode(2), default='Si')
    h22 = Column(Unicode(2), default='Si')
    h23 = Column(Unicode(2), default='Si')
    dedicated_id = Column(Integer, ForeignKey('dedicated.id'))

class Roles(DeclarativeBase):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(30))
    group = Column(Unicode(30))
    users = relationship('RolUsers',cascade="all,delete", backref='roles')

class RolUsers(DeclarativeBase):
    __tablename__ = 'rolusers'
    id = Column(Integer, primary_key=True)
    user_name = Column(Unicode(16), default=u'', nullable=False)
    roles_id = Column(Integer, ForeignKey('roles.id'))


class TempCalendars(DeclarativeBase):
    __tablename__ = 'tmpcalendars'
    id = Column(Integer, primary_key=True)
    day = Column(DateTime, default=datetime.now)
    h00 = Column(Unicode(2), default='Si')
    h01 = Column(Unicode(2), default='Si')
    h02 = Column(Unicode(2), default='Si')
    h03 = Column(Unicode(2), default='Si')
    h04 = Column(Unicode(2), default='Si')
    h05 = Column(Unicode(2), default='Si')
    h06 = Column(Unicode(2), default='Si')
    h07 = Column(Unicode(2), default='Si')
    h08 = Column(Unicode(2), default='Si')
    h09 = Column(Unicode(2), default='Si')
    h10 = Column(Unicode(2), default='Si')
    h11 = Column(Unicode(2), default='Si')
    h12 = Column(Unicode(2), default='Si')
    h13 = Column(Unicode(2), default='Si')
    h14 = Column(Unicode(2), default='Si')
    h15 = Column(Unicode(2), default='Si')
    h16 = Column(Unicode(2), default='Si')
    h17 = Column(Unicode(2), default='Si')
    h18 = Column(Unicode(2), default='Si')
    h19 = Column(Unicode(2), default='Si')
    h20 = Column(Unicode(2), default='Si')
    h21 = Column(Unicode(2), default='Si')
    h22 = Column(Unicode(2), default='Si')
    h23 = Column(Unicode(2), default='Si')
    user_name = Column(Unicode(16), default=u'', nullable=False)


class Position(DeclarativeBase):
    __tablename__ = 'position'
    id = Column(Integer, primary_key=True)
    latitude = Column(Numeric(10,6),default=0)
    longitude = Column(Numeric(11,6),default=0)

class Pets(DeclarativeBase):
    __tablename__ = 'pets'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(16), default=u'', nullable=False)
    breed = Column(Unicode(16), default=u'', nullable=False)


class Assets(DeclarativeBase):
    __tablename__ = 'assets'
    id = Column(Integer, primary_key=True)
    assets_id = Column(Integer,default=0)
    data = Column(LONGTEXT(), default=u'')