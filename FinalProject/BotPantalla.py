import time, network, dht, uping, utelegram, sh1106, ssd1306
from machine import Pin, PWM, ADC, I2C

renglon1 = {"x": 0, "y": 0}
renglon2 = {"x":0, "y": 8}
renglon3 = {"x":0, "y": 16}
renglon4 = {"x":0, "y": 24}
renglon5 = {"x":0, "y": 32}
renglon6 = {"x":0, "y": 40}
renglon7 = {"x":0, "y": 48}
renglon8 = {"x":0, "y": 56}
highLine = 8
widthLine = 127
timeoutLimit = 60000

ssid = "Aquí va el nombre de la red"
password = "Aquí va la contraseña"
telegramToken = "Aquí va el token del bot de telegram" 

print("\n\n -------------------------- Inicio del programa --------------------------\n\n")

def get_message(message):
    value = message['message']['text']
    print(value)
    display.fill_rect(renglon3["x"], renglon3["y"], widthLine, highLine, 0)
    display.show()
    display.text(value,renglon3["x"], renglon3["y"], 1)
    display.show()
    bot.send(message['message']['chat']['id'], "Aquí ponen lo que quieren enviar a telegram") 

def Principal():
    print("The bot is listening")
    bot.listen()

i2c = I2C(0, scl=Pin(18), sda=Pin(19), freq=400000)
display = sh1106.SH1106_I2C(128, 64, i2c, None, 0x3c)
#display = ssd1306.SSD1306_I2C(128, 64, i2c)
display.fill(0)
display.show()
display.text("MicroPython ECCI", renglon1["x"], renglon1["y"], 1)
display.show()

wlan = network.WLAN(network.STA_IF) # create station interface
wlan.active(True)

print("Connecting to WiFi ...")
wlan.connect(ssid, password)
start_time = time.ticks_ms()
while not wlan.isconnected():
    if time.ticks_diff(time.ticks_ms(), start_time) > timeoutLimit:
        print("No se pudo establecer la conexción a WiFi, se superó el límite de tiempo")
        break
print("Connected")
uping.ping("google.com")

if wlan.isconnected():
    print("Creating telegram bot")
    bot = utelegram.ubot(telegramToken)
    bot.set_default_handler(get_message)
    print("The Telegram bot was created")

print("\n\n -------------------------- Termino el programa --------------------------\n\n")