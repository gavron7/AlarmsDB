from numato import numato16
from generator import alarm_generator
from alarm import run_alarm
import time
import threading
import sys


telnet = numato16(ip='192.168.170.48', login='admin', password='Qwerty!2')
lista = alarm_generator()
alarm = run_alarm(lista.bitrate, telnet, pin=1)
alarm.start()
lista.add(0)
def stat():
    print("LISTA:", lista.list)
    print("AKTYWNY:", lista._top())
stat()
s = time.time()
while time.time() - s < 30:
    x = lista.run()
    if lista.is_changed():
        print('zmiana',x)
        alarm.add(x)
        # print(len(x), lista.is_changed())
    time.sleep(0.01)

print("juz")
print(lista.list)
alarm.stop()
