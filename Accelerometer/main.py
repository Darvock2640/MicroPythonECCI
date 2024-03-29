import time, socket, uping, network
from machine import ADC, Pin

print("\n\nProyecto Prueba IoT\n\n")

timeOutLimit = 45000
ssid = "iPhone de Alejho"
password = "11235813"
HOST = "172.20.10.2"  # the host ipv4 address 
PORT1 = "1234"
PORT2 = "1235"

accX = ADC(Pin(32), atten = ADC.ATTN_11DB)
accX.width(ADC.WIDTH_12BIT)

accY = ADC(Pin(33), atten = ADC.ATTN_11DB)
accY.width(ADC.WIDTH_12BIT)

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

    while True:
        valueX = accX.read_uv() - 1650000
        valueY = accY.read_uv() - 1650000
        print("X: {}, Y: {}".format(valueX,valueY))
        socket1.sendall(str(valueX).encode())
        socket2.sendall(str(valueY).encode())
        time.sleep_ms(250)




