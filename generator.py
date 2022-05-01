import math
import time
import threading
import sys

class alarm_generator:

    piority = [
        {'ilosc_piskow_na_sekunde': 2, 'przerwa_impuls': 5, 'powtorzenia': 1, 'przerwa': 1},
        {'ilosc_piskow_na_sekunde': 3, 'przerwa_impuls': 3, 'powtorzenia': 1, 'przerwa': 1},
        {'ilosc_piskow_na_sekunde': 5, 'przerwa_impuls': 2, 'powtorzenia': 1, 'przerwa': 1},
    ]
    bitrate = 10 # Hz

    def __init__(self):
        self.list = []
        self.old_a = 0
        self.oldlist = []
        self.changed = False

    def _top(self):
        try:
            return self.piority[self.list[0]]
        except:
            return False

    def __gen_sinus(self, alarm, precyzja=10):
        # generowanie sekundy sygnału o danej częstotliwości
        _output = ""
        piski = alarm['ilosc_piskow_na_sekunde']
        if 2 * piski > self.bitrate:
            piski = int(self.bitrate / 2)
        for i in range(int(round(2 * math.pi)) * precyzja):
            wynik =  math.sin(i * piski / precyzja)
            if wynik > 0:
                wynik = 1
            elif wynik <= 0:
                wynik = 0
            _output += str(wynik)
        return _output

    def __gen_silent(self):
        # generowanie sekundy ciszy
        return "0" * self.bitrate

    def __gen_wait(self):
        # generowanie sekundy pauzy
        return "w" * self.bitrate

    def __make_alarm(self, alarm):
        _sek_sin = self.__make_cut(self.__gen_sinus(alarm))
        _sek_sil = self.__gen_silent() * alarm['przerwa_impuls']
        _output = ""
        for i in range(alarm['powtorzenia'] + 1):
            _output += _sek_sin + _sek_sil
        if alarm['powtorzenia'] > 0 and alarm['przerwa_impuls'] > 0:
            _output = _output[:-len(_sek_sil)]
        _output += self.__gen_wait() * alarm['przerwa']
        return _output

    def __make_cut(self, alarm):
        # ucinanie wyniku do x bitów
        __tmp = ""
        for i in range(1, len(alarm), int(len(alarm) / self.bitrate)):
            __tmp += alarm[i]
        return __tmp

    def __generate(self):
        a = self.__make_alarm(self._top())
        self.old_a = a
        return a

    def __find_top_alarm(self):
        self.list.sort(reverse=True)
        try:
            __old = self.oldlist[0]
        except:
            __old = []
        try:
            __new = self.list[0]
        except:
            __new = []
        if __new != __old:
            self.oldlist = self.list.copy()
            self.changed = True

    def is_changed(self):
        a = self.changed
        self.changed = False
        return a

    def add(self, pio):
        if pio > len(self.piority):
            pio = len(self.piority) - 1
        elif pio < 0:
            pio = 0
        self.list.append(pio)
        self.__find_top_alarm()

    def remove(self, pio):
        try:
            self.list.remove(pio)
        except:
            pass
        self.__find_top_alarm()

    def run(self):
        if not self._top():
            self.old_a = "0"
            return self.old_a
        a = self.__generate()
        return a