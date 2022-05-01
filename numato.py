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
        self.try_to_reconnect = True
        self.moderror = False
        self.tn = tn()
        self.__connect()

    def __connect(self):
        if self.is_connected:
            return
        if not self.try_to_reconnect:
            return
        print("Łączenie z numato16... ", end="")
        try:
            self.tn.close()
            self.tn.open(host=self.konfig['ip'], port=23, timeout=1)
            # self.tn.open(host='192.168.200.3', port=80, timeout=1)
            self.tn.set_debuglevel(9)
            self.is_connected = True
            self.try_to_reconnect = True
            self.__no_error()
            print("CONNECTED")
        except ConnectionRefusedError:
            self.__set_error("Brak połączenia z numato16. Nie ponawiam próby połączenia.")
            self.try_to_reconnect = False
        except TimeoutError:
            self.tn.close()
            self.is_connected = False
            self.try_to_reconnect = True
            self.__set_error("Brak połączenia z numato16. Ponawiam próbę połączenia.")
            print("ERROR")
        if self.is_connected:
            return self.__login()
        return False

    def __read(self):
        return self.tn.read_very_eager().decode('utf-8')

    def __write(self, value):
        self.tn.write(value.encode('utf-8'))

    def __readtill(self, co, timeout=1):
        s = time.time()
        out = ""
        while time.time() - s < timeout:
            a = self.__read()
            out += a
            if co in a:
                return out
        return False

    def __login(self):
        login_error = False
        if not self.__readtill("User Name:"):
            login_error = True
        else:
            self.__write(self.konfig['login'] + "\n")
        if login_error or not self.__readtill("Password:"):
            login_error = True
        else:
            self.__write(self.konfig['password'] + "\n")
        if login_error or not self.__readtill(">"):
            login_error = True
        if login_error:
            self.try_to_reconnect = True
            self.is_connected = False
            self.tn.close()
            return False
        else:
            self.is_connected = True
            return True

    def __set_error(self, value):
        self.moderror = value

    def __no_error(self):
        self.__set_error(False)

    def get_error(self):
        return self.moderror

    def __gpio_set(self, gpio, value):
        cmd = "gpio "
        if value == "1":
            cmd += "set"
        else:
            cmd += "clear"
        cmd += " " + str(gpio) + "\r\n"
        self.__write(cmd)
        self.__readtill(">")

    def tick(self, value, pin=1):
        print("tick", value, pin)
        self.__gpio_set(pin, value)
