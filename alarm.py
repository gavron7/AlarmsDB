import math
import time
import threading
import sys

class run_alarm:
    def __init__(self, bitrate, telnet):
        self.telnet = telnet
        self.pozycja = 0
        self.alarm = "0"
        self.old_time = 0
        self.bitrate = bitrate
        self.pid = False
        self.running = True

    def start(self):
        self.pid = threading.Thread(target=self.__run_foreground)
        self.pid.start()

    def stop(self):
        self.running = False
        self.pid.join()

    def add(self, alarm):
        self.pozycja = 0
        self.alarm = alarm

    def _is_time(self):
        if time.time() - self.old_time < 1 / self.bitrate:
            return False
        self.old_time = time.time()
        return True

    def __tick(self):
        akt = self.alarm[self.pozycja]
        self.pozycja += 1
        if self.pozycja >= len(self.alarm):
            self.pozycja = 0
        self.telnet.tick(akt)

    def __run_foreground(self):
        while self.running:
            if self._is_time():
                self.__tick()
            time.sleep(1 / (self.bitrate*1000))
