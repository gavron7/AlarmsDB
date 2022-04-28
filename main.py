def log(co):
    print(co)

class alarms:
    standard = "xxX         "
    high = "xXxXxXxXxXxXxXxX         "

    def __init__(self):
        self.alarms_list = {}
        self.alarms_top = ""
        pass

    def add(self, name, type):
        log("dodano alarm: '" + name + "' typ: '" + type + "'")
        self.alarms_list[name] = type
        self.find_top_alarm()

    def find_top_alarm(self):
        log("finding top alarm")
        max = 0
        for i in self.alarms_list:
            if max < len(self.alarms_list[i]):
                self.alarms_top = i
                max = len(self.alarms_list[i])
        log("top alarm: '" + self.alarms_top + "'")
a = alarms()
a.add('alarm2', a.high)
a.add('alarm1', a.standard)
a.add('alarm3', a.standard)

