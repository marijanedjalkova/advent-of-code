from Day4.ShiftCls import LogLine, Shift


def get_shift(shift_map_by_guard, date):
    for guard_id, shift_map_by_date in shift_map_by_guard.items():
        if date in shift_map_by_date:
            return shift_map_by_date[date]
    return None


def check_unclaimed_logs(unclaimed_logs, shift):
    to_remove = []
    for log in unclaimed_logs:
        if log.shift_date == shift.shift_date:
            shift.update(log)
            to_remove.append(log)
    for item in to_remove:
        unclaimed_logs.remove(item)


def get_shift_map_by_guard(content_array):
    shifts = {}
    unclaimed_logs = []
    for note in content_array:
        note_details = note.split()
        if len(note_details) == 0:
            continue
        log_line = LogLine(note_details)
        if log_line.guard_id is None:
            that_night_shift = get_shift(shifts, log_line.shift_date)
            if that_night_shift is None:
                # nothing yet, don't attach anywhere
                unclaimed_logs.append(log_line)
            else:
                that_night_shift.update(log_line)
        else:
            # this is a starting line, can create a shift?
            if log_line.guard_id in shifts:
                if log_line.shift_date not in shifts[log_line.guard_id]:
                    new_shift = Shift(log_line)
                    shifts[log_line.guard_id][log_line.shift_date] = new_shift
                    check_unclaimed_logs(unclaimed_logs, new_shift)
                else:
                    shifts[log_line.guard_id][log_line.shift_date].update(log_line)
            else:
                # have not yet seen that guard id
                new_shift = Shift(log_line)
                shifts[log_line.guard_id] = {log_line.shift_date: new_shift}
                check_unclaimed_logs(unclaimed_logs, new_shift)
    return shifts


def get_overall_sleep_time(map_by_date):
    return sum([shift.get_sleep_time() for shift in map_by_date.values()])


def get_most_sleepy_guard(shifts):
    return max(shifts, key=lambda guard_id: get_overall_sleep_time(shifts[guard_id]))


def get_sleep_minutes(map_by_date):
    minutes_asleep = []
    for date, shift in map_by_date.items():
        minutes = list(shift.get_asleep_minutes())
        minutes_asleep.extend(minutes)
    return minutes_asleep


def get_minute_most_sleep(map_by_date):
    minutes_asleep = get_sleep_minutes(map_by_date)
    return max(set(minutes_asleep), key=minutes_asleep.count)


def get_times_asleep_at(minute, map_by_date):
    minutes = get_sleep_minutes(map_by_date)
    return minutes.count(minute)


def get_worst_time(shifts_by_date):
    minutes_asleep = get_sleep_minutes(shifts_by_date)
    if len(minutes_asleep) == 0:
        return 0, 0
    worst_minute = max(set(minutes_asleep), key=minutes_asleep.count)
    how_many_times = minutes_asleep.count(worst_minute)
    return worst_minute, how_many_times


def get_guard_most_asleep_at_same_time(shifts):
    stats = {}
    for guard_id, shifts_by_date in shifts.items():
        worst_minute, how_many_times = get_worst_time(shifts_by_date)
        stats[how_many_times / len(shifts_by_date)] = {worst_minute: guard_id}
    print(stats)
    worst_data = max(stats)
    data = stats[worst_data]
    for key, value in data.items():
        worst_time = key
        worst_guard = value
    return worst_time, worst_guard


def main():
    with open("input.txt") as task_input:
        content_array = task_input.read().split("\n")
        shifts = get_shift_map_by_guard(content_array)
        sleepiest_guard_id = get_most_sleepy_guard(shifts)
        worst_minute = get_minute_most_sleep(shifts[sleepiest_guard_id])
        print("final result", worst_minute * int(sleepiest_guard_id[1:]))
        worst_time, guard_most_freq_asleep_same_minute = get_guard_most_asleep_at_same_time(shifts)
        print("final result for part 2", worst_time * int(guard_most_freq_asleep_same_minute[1:]))


if __name__ == '__main__':
    main()
