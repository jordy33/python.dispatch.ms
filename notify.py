#!/usr/bin/python
import sys
import requests
list=sys.argv
element=list[1]
param=element.split(",")
eid=str(param[2])
desc="No Definido"
if eid=="1" or eid=="9":
    desc="SOS"
if eid=="3":
    desc="Paro_de_motor"
if eid=="4":
    desc="Encendido_de_motor"
if eid=="5":
    desc="Ubicacion"
if eid=="6":
    desc="Cuenta_expirada"
if eid=="7":
    desc="Itinerario"
if eid=="8":
    desc="Otro"
if eid=="23":
    desc="Corte_de_bateria"
if eid=="28":
    desc="Corte_de_antena"

pluton=requests.get('https://pluto.dudewhereismy.com.mx/services/imeiInfo?imei='+param[1])
if 'error' in pluton:
    error=pluton['error']
    if pluton['error']=='ok':
        if 'application_id' in pluton:
            app_id=pluton['application_id']
            if app_id=='200' or app_id=='559' or app_id=='959':
                #NEZA
                neza = requests.get('http://c4neza.dwim.space/listener/one.html'+'?azimuth='+param[7]+"&client_id="+pluton['client_id']+'&event_desc='+desc+'&event_id='+param[2]+'&gpsvalid='+param[8]+'&imei='+param[1]+"&internal_id=2"+'&latitude='+param[4]+'&longitude='+param[5]+'&rdatetime='+param[9]+'&speed='+param[6]+'&vehicle=' + param[10])
            else:
                # KANAN
                r=requests.get('https://dispatch.dudewhereismy.com.mx/listener/basica?account='+param[0]+'&imei='+param[1]+'&event_id='+param[2]+'&event_desc='+desc+'&latitude='+param[4]+'&longitude='+param[5]+'&speed='+param[6]+'&azimuth='+param[7]+'&gpsvalid='+param[8]+'&rdatetime='+param[9]+'&vehicle='+param[10]+"&internal_id=2"+"&client_id="+pluton['client_id'])
    else:
        r = requests.get('https://dispatch.dudewhereismy.com.mx/listener/one?account=' + param[0] + '&imei=' + param[1] + '&event_id=' + param[2] + '&event_desc=' + desc + '&latitude=' + param[4] + '&longitude=' + param[5] + '&speed=' + param[                 6] + '&azimuth=' + param[7] + '&gpsvalid=' + param[8] + '&rdatetime=' + param[9] + '&vehicle=' + param[10] + "&internal_id=2" + "&client_id=" + client_id)
        #r = requests.get('https://dispatch.dudewhereismy.com.mx/listener/cp?account=' + param[0] + '&imei=' + param[1] + '&event_id='+param[2] + '&event_desc=' + desc + '&latitude=' + param[4] + '&longitude=' + param[5] + '&speed=' + param[6] + '&azimuth=' + param[7] + '&gpsvalid=' + param[8] + '&rdatetime=' + param[9] + '&vehicle=' + param[10] + "&internal_id=2" + "&client_id=" + pluton['client_id'])
