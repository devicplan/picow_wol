# WOL with Raspberry Pico W 
# Micropython with Raspberry Pico W
# 26.03.2023 jd@icplan.de

import network, socket, time, ntptime, utime, machine, os, secrets

led = machine.Pin("LED",machine.Pin.OUT)
led.off()
time.sleep(1)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets.ssid, secrets.password)
    
# Wait for connect or fail
max_wait = 30

while max_wait > 0:                                                                # wait 30 sec for wifi connect
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    led.on()
    time.sleep(1)

# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )
    led.off()

# Start Programm

msg = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
wol_port = 9
magic = msg + (secrets.mac1 * 16)

soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for a in range (0,3,1):
    print("send magic paket")
    soc.sendto(bytes(magic),(secrets.broadcast,9))
    time.sleep_ms(1000)
soc.close()

while True:
    led.on()                                                                       # leds flash every 1 seconds for function control
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)
