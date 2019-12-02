import datetime
import socket
from datetime import time
# 25 characteres
# 00000019I 80301234 TOL18060805483
# 18 caracteres
# 00000012
vehicle = "Prueba Renault Trafic 2015 Blanca"
print("vehicle:{}".format(vehicle))
imei = "864507035877413"
print("IMEI:{}".format(imei))
plates= "756916J"
print("Plates:{}".format(plates))
latitude= "19.900995"
print("Latitude:{}".format(latitude))
longitude= "-99.15909"
print("Longitude:{}".format(longitude))
speed= "0"
print("Speed:{}".format(speed))
heading = "14"
print("Heading:{}".format(heading))
separator=chr(9)
ip="0"
utcnow = datetime.datetime.utcnow()
midnight_utc = datetime.datetime.combine(utcnow.date(), time(0))
delta = utcnow - midnight_utc
seconds=str(int(float(delta.seconds)))
valid="1"
status="1"

prepayload="P"+separator+\
           vehicle+separator+\
           ip+separator+\
           imei+separator+\
           plates+separator+\
           seconds+separator+\
           latitude+separator+\
           longitude+separator+\
           speed+separator+\
           heading+separator+\
           valid+separator+\
           status
heading=format(len(prepayload), '02x')
heading=heading.zfill(8).upper()
payload=heading+prepayload
#print("Payload:{}".format(payload))
#print(payload.count(chr(9)))
#host = "138.68.54.137"
host = "201.144.252.139"
port = 4105
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send(payload.encode())
data = b''
s.settimeout(5.0)
ticket=""
try:
    bytes=s.recv(1042)
except Exception as e:
    ticket="Error C5 Rechazo la alerta"
else:
    print(bytes)
    raw_header = bytes.decode("utf-8")
    hex_header = "0x" + raw_header.lstrip("0")
    header_lenght = int(hex_header, 16)
    print("header length:{}".format(header_lenght))
    count=0
    while True:
        try:
            packet = s.recv(1)
        except:
            break
        data += packet
        count+=1
        #print("count:{} data:{}".format(count,data))
        if count>header_lenght:
            break
    sdata=data.decode("utf-8")
    position=sdata.rfind("\t")
    position+=1
    #print("position:{}".format(position))
    ticket = sdata[position:]
s.close()
print("Ticket:{}".format(ticket))