from maix import uart, pinmap

import json

file_path = 'config.json'
with open(file_path, 'r', encoding='utf-8') as file:
    config = json.load(file)

pinmap.set_pin_function("A18", "UART1_RX")
pinmap.set_pin_function("A19", "UART1_TX")

main_toglle=False

device = "/dev/ttyS1"

serial1 = uart.UART(device, 115200)

port0=config['port0_init_value']
port1=config['port1_init_value']

msg=f"#001P{str(config['port1_init_value']).zfill(4)}T0000!"
serial1.write_str(msg)
msg=f"#000P{str(config['port0_init_value']).zfill(4)}T0000!"
serial1.write_str(msg)

def port_init():
    global port0, port1
    port0=config['port0_init_value']
    port1=config['port1_init_value']
    msg=f"#001P{str(config['port1_init_value']).zfill(4)}T0000!"
    serial1.write_str(msg)
    msg=f"#000P{str(config['port0_init_value']).zfill(4)}T0000!"
    serial1.write_str(msg)
def port1_change(value,speed=100):
    global port1, serial1,port1_toggle,main_toglle
    if main_toglle==False:
        return
    if value==0:
        return
    speedVal=10000-100*speed
    if speedVal==10000:
        speedVal-=1
    port1+=int(value)

    if port1>config["port1_search_max"]:
        port1_toggle=-1
    if port1<config["port1_search_min"]:
        port1_toggle=1
    if port1>int(config['port1_max_value']):
        port1=int(config['port1_max_value'])
    if port1<int(config['port1_min_value']): 
        port1=int(config['port1_min_value'])
    # print(str(speedVal).zfill(4))
    msg=f"#001P{str(port1).zfill(4)}T{str(speedVal).zfill(4)}!"
    # print(msg)
    serial1.write_str(msg)


def port0_change(value,speed=100):
    global port0, serial1,port0_toggle,main_toglle

    if main_toglle==False:
        return
    if value==0:
        return
    speedVal=10000-100*speed
    if speedVal==10000:
        speedVal-=1
    port0+=int(value)

    if port0<config["port0_search_min"]:
        port0_toggle=1
    if port0>config["port0_search_max"]:
        port0_toggle=-1

    if port0>int(config['port0_max_value']):
        port0=int(config['port0_max_value'])
    if port0<int(config['port0_min_value']): 
        port0=int(config['port0_min_value'])
    # print(str(speedVal).zfill(4))
    # print(port0_toggle)
    msg=f"#000P{str(port0).zfill(4)}T{str(speedVal).zfill(4)}!"
    # print(msg)
    serial1.write_str(msg)
port0_toggle=1
port1_toggle=1
def search_mode():
    global port1_toggle,port0_toggle,port1
    port0_change(config['port0_search_speed']*port0_toggle)
    # port1=config['pot1_search_val']
    port1_change(config['pot1_search_val']-port1)
    # port1_change(config['port1_search_speed']*port1_toggle)

def open_sg_uart():
    global main_toglle, port0_toggle, port1_toggle
    if main_toglle==False:
        main_toglle=True
        port0_toggle=-1

def close_sg_uart():
    global main_toglle, port0_toggle, port1_toggle
    if main_toglle==True:
        main_toglle=False
    
def search_val_init(port0,port1):
    # print("get in ")
    global port1_toggle,port0_toggle
    port0_toggle=port0
    port1_toggle=port1
# def port0_change(value,speed=100):
#     global serial1
#     speedVal=10*speed
#     if value>0:
#         msg=f"#000P{str(1500-speedVal).zfill(4)}T0000!"
#         print(str(1500-speedVal).zfill(4))
#     elif value<0:
#         msg=f"#000P{str(1500+speedVal).zfill(4)}T0000!"
#         print(str(1500+speedVal).zfill(4))
#     elif value==0:
#         msg=f"#000P1500T0000!"
#     serial1.write_str(msg)







