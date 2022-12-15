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

ssid = "ECCI-Estudiantes"
password = "Estudiantes2021."
telegramToken = "5872726487:AAEYHjUeXAYTi91exu8g-UfOtVmSjvBMrtA" # Ojo aqui va el token de su BOT no del mio 

print("\n\n -------------------------- Inicio del programa --------------------------\n\n")

i2c = I2C(0, scl=Pin(18), sda=Pin(19), freq=400000)
#display = sh1106.SH1106_I2C(128, 64, i2c, None, 0x3c)
display = ssd1306.SSD1306_I2C(128, 64, i2c)
display.fill(0)
display.show()
display.text("MicroPython ECCI", renglon1["x"], renglon1["y"], 1)
display.text("El mensaje del bot es: ", renglon2["x"], renglon2["y"], 1)
display.show()

wlan = network.WLAN(network.STA_IF) # create station interface
wlan.active(True)

def Connect2Wifi():
    print("Connecting to WiFi ...")
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        pass
    print("Connected")
    uping.ping("google.com")

def get_message(message):
    value = message['message']['text']
    print(value)
    display.fill_rect(renglon3["x"], renglon3["y"], 127, 7, 0)
    #display.fill(0)
    display.show()
    display.text(value,renglon3["x"], renglon3["y"], 1)
    display.show()
    #bot.send(message['message']['chat']['id'], message['message']['text'].upper())

def reply_ping(message):
    print(message)
    #bot.send(message['message']['chat']['id'], 'pong')

def Principal():
    Connect2Wifi()

    if wlan.isconnected():
        print("Creating telegram bot")
        bot = utelegram.ubot(telegramToken)
        #bot.register('/ping', reply_ping)
        bot.set_default_handler(get_message)
        print("The Telegram bot was created")
    
    print("The bot is listening")
    bot.listen()

print("\n\n -------------------------- Termino el programa --------------------------\n\n")