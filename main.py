import time

class alarms:

    piority = [
        'krótki0',
        'krotki1',
        'krotki2',
        'krotki3',
        'krotki4',
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

    def run(self):
        if not self.top() or time.time() - self.oldtime < 0.2:
            return
        self.oldtime = time.time()
        a = self.top()[self.position]
        self.position += 1
        if self.position >= len(self.top()):
            self.position = 0
        return a

a = alarms()
a.add(1)
a.add(3)
a.add(2)
a.remove(3)
a.remove(1)
# a.remove(2)
print(a.list)
print(a.top())
s=time.time()
while time.time() - s < 10:
    x = a.run()
    if x:
        print(x)