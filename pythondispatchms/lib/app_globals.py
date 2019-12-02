# -*- coding: utf-8 -*-

"""The application's Globals object"""

__all__ = ['Globals']
import os
import urllib3

class Globals(object):
    """Container for objects available throughout the life of the application.

    One instance of Globals is created during application initialization and
    is available during requests via the 'app_globals' variable.

    Insert this at ~./basrhrc

    export dispatch_HOST=dispatch.dudewhereismy.mx
    export dispatch_PORT=8093
    export dispatch_SECURE=True
    export dispatch_DIR=/root/python.dispatch.ms
    export STOMP_HOST=stomp.dudewhereismy.mx
    export STOMP_MASTER_USER=dwim
    export STOMP_MASTER_PASS=gpscontrol1
    export STOMP_SECURE=True

    """

    def __init__(self):
        """Do nothing, by default."""
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        # Server parameters

        self.host_secure = os.getenv('DISPATCH_SECURE')
        if self.host_secure is None:
            self.host_secure="False"

        if self.host_secure=="False":
            host_prefix="http://"
        else:
            host_prefix="https://"

        self.host_prefix=host_prefix

        host_port=os.getenv('DISPATCH_PORT')
        if host_port is None:
            host_port=""

        if len(host_port)>0:
            self.host_port=":"+host_port
        else:
            self.host_port=""

        self.host=os.getenv('DISPATCH_HOST')
        if self.host is None:
            self.host=host_prefix+"localhost:8093"
        else:
            self.host=host_prefix+self.host

        self.app_dir = os.getenv('DISPATCH_DIR')
        if self.app_dir is None:
            self.app_dir=os.getcwd()

        # STOMP parameters
        self.stomp_secure=os.getenv('STOMP_SECURE')
        if self.stomp_secure is None:
            self.stomp_secure="True"

        if self.stomp_secure=="False":
            stomp_prefix="ws://"
        else:
            stomp_prefix="wss://"

        stomp_port=os.getenv('STOMP_PORT')
        if stomp_port is None:
            stomp_port=""
        if len(stomp_port)>1:
            self.stomp_port=":"+stomp_port
        else:
            self.stomp_port=""

        self.stompHost = os.getenv('STOMP_HOST')
        if self.stompHost is None:
            self.stompHost = "stomp.dudewhereismy.mx"

        self.stompUserName = os.getenv('STOMP_MASTER_USER')
        if self.stompUserName is None:
            self.stompUserName = "dwim"

        self.stompPassword = os.getenv('STOMP_MASTER_PASS')
        if self.stompPassword  is None:
            self.stompPassword = "gpscontrol1"

        self.stompServer=stomp_prefix+self.stompHost+':15671'+'/ws'

        # Telefonica Test parameters
        cert_file_path = self.app_dir + "/telefonica.cer"
        key_file_path = self.app_dir + "/telefonica.key"
        self.cert = (cert_file_path, key_file_path)
        self.apiUser="customer-DUDE_WHERE_IS_MY156320dc8168LfDu"
        if os.getenv('SUN_SECURE')=="True":
            self.domainsun="https://"+os.getenv('SUN_HOST')
        else:
            self.domainsun = "http://" + os.getenv('SUN_HOST')

        if os.getenv('PLUTO_SECURE') == "True":
            self.domainpluto="https://"+os.getenv('PLUTO_HOST')
        else:
            self.domainpluto = "http://" + os.getenv('PLUTO_HOST')

        self.sunUsers = os.getenv('SUN_USERS')
        if self.sunUsers is None:
            self.sunUsers=self.domainsun+"/services/users"

        self.sunGroups = os.getenv('SUN_GROUPS')
        if self.sunGroups is None:
            self.sunGroups = self.domainsun+"/services/groups"

        self.sunApplications=self.domainsun+"/services/applications?internal_id=2"
        self.sunapps = self.domainsun + "/services/apps"

        self.telefonicaPosition="https://m2m-api.telefonica.com:8010/services/REST/GlobalM2M/Inventory/v5/r12/sim/icc:"
        self.opencell="http://opencellid.org/cell/get"
        self.opencellkey="2a87df53b26d3e"

        self.masterFields= {0: 'NONE', 1: U'IMEI', 2: U'EVENT_ID', 3: U'EVENT_DESC', 4: U'LATITUDE', 5: U'LONGITUDE',
               6: U'SPEED', 7: U'AZIMUTH', 8: U'VALID', 9: U'DATETIME', 10: U'CLIENT_ID', 11: U'VEHICLE',
               12: U'VOLTAGE', 13: U'INTERNAL_ID',14:U'MCC',15:U'MNC',16:U'LAC',17:U'CELLID'}

        self.inverseMasterFields = {'NONE':0, U'IMEI':1, U'EVENT_ID':2, U'EVENT_DESC':3, U'LATITUDE':4, U'LONGITUDE':5,
               U'SPEED':6, U'AZIMUTH':7, U'VALID':8, U'DATETIME':9, U'CLIENT_ID':10,  U'VEHICLE':11,
               U'VOLTAGE':12, U'INTERNAL_ID':13,U'MCC':14,U'MNC':15,U'LAC':16,U'CELLID':17}


        self.trafficOperation={1:'Ver detalle de Tráfico',2:'Poner en pendiente',3:'Crear Ticket',4:'Finalizar Tráfico',5:'Alarma C5',6:'Agregar Imagen',7:'Pedir ubicación Telefonica'}
        # operation
        #          1 --> View Traffic Data
        #          2 --> Put Pending
        #          3 --> Create Ticket
        #          4 --> Finalize Traffic
        #          5 --> C5 Alarm
        #          6 --> Add Image
        #          7 --> Telefonica Location

        self.viewTrafficData = 1
        self.putPending = 2
        self.createTicket = 3
        self.finalizedTraffic = 4
        self.c5Alarm = 5
        self.addImage = 6
        self.telefonicaLocation = 7