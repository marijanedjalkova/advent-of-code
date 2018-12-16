from datetime import datetime, date, timedelta

DATE_INDEX = 2
BEGIN_SHIFT_LENGTH = 6
GUARD_ID_INDEX = 3


class Shift:

    def __init__(self, log_line):
        self.shift_date = None
        self.asleep_time = None
        self.awake_time = None
        self.guard_id = None
        self.start_time = None
        self.update(log_line)

    def update(self, log_line):
        self.shift_date = log_line.shift_date
        if log_line.type == "GUARD":
            self.guard_id = log_line.guard_id
            self.start_time = log_line.event_time
        elif log_line.type == "falls":
            self.asleep_time = log_line.event_time
        elif log_line.type == "wakes":
            self.awake_time = log_line.event_time
        else:
            print("Unknown value")

    def get_sleep_time(self):
        if not self.awake_time and not self.asleep_time:
            return 0
        date_time_a = datetime.combine(date.today(), self.awake_time)
        date_time_b = datetime.combine(date.today(), self.asleep_time)
        date_time_difference = date_time_a - date_time_b
        return date_time_difference.total_seconds() / 60

    def get_asleep_minutes(self):
        if not self.awake_time and not self.asleep_time:
            return []
        return range(self.asleep_time.minute, self.awake_time.minute)

    def __repr__(self):
        return "DATE: {self.shift_date} {self.guard_id}: \n \
        START {self.start_time}, SLEEP {self.asleep_time} - {self.awake_time}".format(self=self)


def get_date(date_str):
    trimmed = date_str[1:-1]
    return datetime.strptime(trimmed, "%Y-%m-%d %H:%M")


class LogLine:

    def __init__(self, note_details=None):
        self.guard_id = None
        self.timestamp = get_date(" ".join(note_details[:DATE_INDEX]))
        self.shift_date = self.get_shift_date()
        self.event_time = self.timestamp.time()
        if len(note_details) == BEGIN_SHIFT_LENGTH:
            self.type = "GUARD"
            self.guard_id = note_details[GUARD_ID_INDEX]
        else:
            self.type = note_details[2]

    def get_shift_date(self):
        if self.timestamp.hour == 23:
            return (self.timestamp + timedelta(days=1)).date()
        return self.timestamp.date()
