import math
import time

class alarm:

    piority = [
        {'ilosc_piskow_na_sekunde': 1, 'powtorzenia': 3, 'przerwa': 10},
        {'ilosc_piskow_na_sekunde': 1, 'powtorzenia': 5, 'przerwa': 10},
        {'ilosc_piskow_na_sekunde': 2, 'powtorzenia': 5, 'przerwa': 8},
        {'ilosc_piskow_na_sekunde': 2, 'powtorzenia': 8, 'przerwa': 8},
        {'ilosc_piskow_na_sekunde': 10, 'powtorzenia': 10, 'przerwa': 5},
    ]

    def __init__(self):
        self.list = []
        self.oldtime = 0
        self.position = 0

    def add(self, pio):
        self.list.append(pio)
        self.find_top_alarm()

    def find_top_alarm(self):
        l = self.list
        self.list.sort(reverse=True)
        if l != self.list:
            self.position = 0

    def remove(self, pio):
        try:
            self.list.remove(pio)
        except:
            pass
        self.find_top_alarm()

    def top(self):
        try:
            return self.piority[self.list[0]]
        except:
            return False

    def _make_alarm(self, alarm):
        out = ""
        f = alarm['ilosc_piskow_na_sekunde']
        xmax = math.pi * 2
        xmax = int(round(xmax))
        for i in range(xmax ):
            wynik =  math.sin(i)
            if wynik > 0:
                wynik = 1
            elif wynik <= 0:
                wynik = 0
            out += str(wynik)
        return out

    def run(self):
        if not self.top() or time.time() - self.oldtime < 2 * math.pi:
            # czy alarm jest włączony oraz czy upłynął czas od ostatniego wywołania
            return
        a = self._make_alarm(self.top())
        return a

a = alarm()
a.add(4)
print(a.list)
print(a.top())
s=time.time()
while time.time() - s < 3:
    x = a.run()
    if x:
        print(len(x), x)

