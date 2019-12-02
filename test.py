#!/usr/bin/python
import sys
import requests
list=sys.argv
#element=list[1]
#param=element.split(",")
param=[]
for i in range(0,11):
    param.append('868998030320317')
eid="1"

desc="Evento:"+eid
if eid=="1" or eid=="9":
    desc="S.O.S"
if eid=="3":
    desc="ParoDeMotor"
if eid=="4":
    desc="EncendidoDeMotor"
if eid=="5":
    desc="Ubicacion"
if eid=="6":
    desc="CuentaExpirada"
if eid=="7":
    desc="Itinerario"
if eid=="8":
    desc="Otro"
if eid=="23":
    desc="CorteDeBateria"
if eid=="28":
    desc="CorteDeAntena"

pluton=requests.get('https://pluto.dudewhereismy.com.mx/services/imeiInfo?imei='+param[1])
response=pluton.json()
if 'error' in response:
    if response['error']=='ok':
        if 'application_id' in response:
            app_id=response['application_id']
            if 'client_id' in response:
                client_id=response['client_id']
            else:
                client_id='No definido'
            if 'model' in response:
                model=response['model']
            else:
                model="nodef"
            if 'color' in response:
                color=response['color']
            else:
                color='nocolor'
            if 'plates' in response:
                plates=response['plates']
            else:
                plates='noplates'
            if app_id==200 or app_id==559 or app_id==959:
                #NEZA
                desc='Neza_'+desc
                neza = requests.get('https://dispatch.dudewhereismy.com.mx/listener/neza?imei='+str(param[1])+'&event_id='+str(param[2])+'&event_desc='+desc+'&latitude='+str(param[4])+'&longitude='+str(param[5])+'&speed='+str(param[6])+'&azimuth='+str(param[7])+'&gpsvalid='+str(param[8])+'&rdatetime='+str(param[9])+'&vehicle='+str(model)+'|'+str(color)+'|'+str(plates)+"&client_id="+str(client_id))
                neza = requests.get('http://c4neza.dwim.space/listener/one.html?imei='+str(param[1])+'&event_id='+str(param[2])+'&event_desc='+desc+'&latitude='+str(param[4])+'&longitude='+str(param[5])+'&speed='+str(param[6])+'&azimuth='+str(param[7])+'&gpsvalid='+str(param[8])+'&rdatetime='+str(param[9])+'&vehicle='+str(model)+'|'+str(color)+'|'+str(plates)+"&client_id="+str(client_id))
            else:
                # KANAN
                if not desc[:6]=="Evento":
                    internal_id=response['internal_id']
                    if internal_id==3:
                        desc='Kanan_'+desc
                        kanan = requests.get('https://dispatch.dudewhereismy.com.mx/listener/kanan?imei='+str(param[1])+'&event_id='+str(param[2])+'&event_desc='+desc+'&latitude='+str(param[4])+'&longitude='+str(param[5])+'&speed='+str(param[6])+'&azimuth='+str(param[7])+'&gpsvalid='+str(param[8])+'&rdatetime='+str(param[9])+'&vehicle='+str(model)+'|'+str(color)+'|'+str(plates)+"&client_id="+str(client_id))
                    else:
                        #print("gpscontrol")
                        desc='Plataforma3_'+desc
                        kanan = requests.get('https://dispatch.dudewhereismy.com.mx/listener/plataforma3?imei='+str(param[1])+'&event_id='+str(param[2])+'&event_desc='+desc+'&latitude='+str(param[4])+'&longitude='+str(param[5])+'&speed='+str(param[6])+'&azimuth='+str(param[7])+'&gpsvalid='+str(param[8])+'&rdatetime='+str(param[9])+'&vehicle='+str(model)+'|'+str(color)+'|'+str(plates)+"&client_id="+str(client_id))
    #else:
        #r = requests.get('https://dispatch.dudewhereismy.com.mx/listener/cp?account=' + param[0] + '&imei=' + param[1] + '&event_id=' + param[2] + '&event_desc=' + desc + '&latitude=' + param[4] + '&longitude=' + param[5] + '&speed=' + param[6] + '&azimuth=' + param[7] + '&gpsvalid=' + param[8] + '&rdatetime=' + param[9] + '&vehicle=' + param[10] + "&internal_id=2" + "&client_id=" + 'none')

