#my horribly inefficient way of doing it. look for libraries in the future!

def time_list(mode, time, num_times):
    time_raw = int(time[0]) * 60 + int(time[2:4])
    if time[-2:] == "PM":
        time_raw = time_raw + 12 * 60
    time_list = []
    if mode == "awake":
        for ok_time in range(1,(num_times + 1)):
            new_time = time_raw - 90 * ok_time
            time_list.append(new_time)
    if mode == "asleep":
        for ok_time in range(1,(num_times + 1)):
            new_time = time_raw + 90 * ok_time
            time_list.append(new_time)
    for index, time in enumerate(time_list): 
        if time < 0:
            time_list[index] = time + (24 * 60)
    time_list = sorted(time_list)
    return time_list

def time_format(time_list):
    form_time_list = []
    for time in time_list:
        if time > (12 * 60):
            raw_time = time - 12 * 60
            hours, minutes = min_hour(str(raw_time / 60), str(raw_time % 60))
            form_time_list.append(hours + ":" + minutes + " PM")
        else:
            hours, minutes = min_hour(str(time / 60), str(time % 60))
            form_time_list.append(hours + ":" + minutes + " AM")
    return form_time_list

def min_hour(hours, minutes):
    if minutes == "0":
        minutes = "00"
    if hours == "0":
        hours = "12"
    return(hours, minutes)

print time_format(time_list("awake", "9:30 PM", 5))    
print time_format(time_list("awake", "9:30 AM", 6))
print time_format(time_list("awake", "4:40 AM", 6))
print time_format(time_list("asleep", "4:40 AM", 6))

# Reddit's best, using datetime libraries... d'oh!
from datetime import datetime, timedelta
def cycle(w):
    w = datetime.strptime(w, '%I:%M %p') + timedelta(0,0,0,0,0,12)
    s = [w + (timedelta(0,0,0,0,90) * i) for i in range(2,6)]
    return [t.strftime('%I:%M %p') for t in s]

print cycle('06:15 AM')