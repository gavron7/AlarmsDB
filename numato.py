from telnetlib import Telnet as tn
import math
import time
import threading
import sys

class numato16:

    def __init__(self, ip, login, password):
        self.konfig = {
            'ip': ip,
            'login': login,
            'password': password,
        }
        self.is_connected=False
        self.tn = tn()
        self.__connect()

    def __connect(self):
        if self.is_connected:
            return
        print("Łączenie z numato16... ", end="")
        try:
            self.tn.close()
            self.tn.open(host=self.konfig['ip'], port=23, timeout=1)
            self.is_connected = True
            print("CONNECTED")
        except TimeoutError:
            self.tn.close()
            self.is_connected = False
            print("ERROR")
        if self.is_connected:
            self.__login()
        # sys.exit()

    def __login(self):
        print("LOGIN")
        pass

    def tick(self, value):
        print("tick", value)
