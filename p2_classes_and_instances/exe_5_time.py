from datetime import datetime, timedelta


class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.time_object = datetime(100, 1, 1, hours, minutes, seconds)

    def set_time(self, hours, minutes, seconds):
        self.time_object = datetime(100, 1, 1, hours, minutes, seconds)
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        # Need to use a leading zero here.
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):
        # datetime time in python
        self.time_object += timedelta(seconds=1)
        self.hours = self.time_object.hour
        self.minutes = self.time_object.minute
        self.seconds = self.time_object.second
        return self.get_time()





