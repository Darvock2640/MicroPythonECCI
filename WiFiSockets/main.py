import time, network, uping, socket

timeOutLimit = 45000
ssid = "yourSSID"
password = "yourPassword"
HOST = "127.0.0.1"  # the host ipv4 address 
PORT1 = "1234"
PORT2 = "1235"

socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

wlan = network.WLAN(network.STA_IF) # create station interface
wlan.active(True)

def Connect2WiFi():
    print("Connecting to WiFi ...")
    wlan.connect(ssid, password)
    start_time = time.ticks_ms()
    while not wlan.isconnected():
        if time.ticks_diff(time.ticks_ms(), start_time) > timeOutLimit:
            print("No se pudo establecer la conexión a WiFi, se superó el límite de tiempo")
            return
    print("Connected")
    uping.ping("google.com")

def main():
    Connect2WiFi()
    socket1.connect((HOST,PORT1))
    socket2.connect((HOST,PORT2))
    socket1.sendall(b'Hola mundo 1')
    socket2.sendall(b'Hola mundo 2')

