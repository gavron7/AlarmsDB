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
    if round(time.time() - s, 2) == 1.0:
        lista.add(1)
        print(1,'dodano 1')
        stat()
    if round(time.time() - s, 2) == 3.0:
        lista.remove(1)
        print(2,"usunieto 1")
        stat()
    if round(time.time() - s, 2) == 5.0:
        print(3,'dodano 0')
        lista.add(0)
        stat()
    if round(time.time() - s, 2) == 7.0:
        lista.remove(0)
        print(4,"usunieto 0")
        stat()
    if round(time.time() - s, 2) == 25.0:
        lista.remove(0)
        print(5,"usunieto 0")
        stat()

    x = lista.run()
    if lista.is_changed():
        print('zmiana',x)
        alarm.add(x)
        # print(len(x), lista.is_changed())
    time.sleep(0.01)

print("juz")
print(lista.list)
alarm.stop()
