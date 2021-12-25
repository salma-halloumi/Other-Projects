#!/usr/bin/env python
# scripts/examples/simple_tcp_client.py
import socket

from umodbus import conf
from umodbus.client import tcp

# Enable values to be signed (default is False).
conf.SIGNED_VALUES = True

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 502))

f = open("requeteRTU.txt", "r")
request=f.read()
paramsList=request.split()
slave_id=int(paramsList[0],16)
funcNumb=int(paramsList[1],16)
starting_address=int(paramsList[2],16)
quantity=int(paramsList[3],16)


# Returns a message or Application Data Unit (ADU) specific for doing
# Modbus TCP/IP.
print("Function",funcNumb)
if(funcNumb==1):
    message = tcp.read_coils(slave_id=slave_id, starting_address=starting_address, quantity=quantity)
elif (funcNumb==2):
    message = tcp.read_discrete_inputs(slave_id=slave_id, starting_address=starting_address, quantity=quantity)
elif (funcNumb==3):
    if(quantity>10-starting_address):
        print("cannot read registers: quantity+starting_address exceeds the limit")
        exit(0)
    else:
        message = tcp.read_holding_registers(slave_id=slave_id, starting_address=starting_address, quantity=quantity)
elif(funcNumb==4):
    message = tcp.read_input_registers(slave_id=slave_id, starting_address=starting_address, quantity=quantity)
elif (funcNumb==5):
    message = tcp.write_single_coil(slave_id=slave_id, starting_address=starting_address, value=1)
elif (funcNumb==6):
    message = tcp.write_single_register(slave_id=slave_id, starting_address=starting_address, value=1)
elif (funcNumb==15):
    message = tcp.write_multiple_coils(slave_id=slave_id, starting_address=starting_address, values=[1, 0, 1])
elif (funcNumb==16):
    message = tcp.write_multiple_registers(slave_id=slave_id, starting_address=starting_address, values=[1,50,10,20,0,200,2,11,30,40,400])
else:
    print("Unknown Function")
    exit(0)

# Response depends on Modbus function code. This particular returns the
# amount of coils written, in this case it is.
if message:
    response = tcp.send_message(message, sock)
    print("response:",response)
sock.close()