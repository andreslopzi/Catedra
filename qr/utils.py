from datetime import datetime

#
def compareDate (now, date,max):
    hour_min = 0
    hour_max = 0
    if max:
        print("true")
        date_max=now
        date_min=date
        hour_min = (date.hour+19)%24
        hour_max= now.hour
    else:
        print("false")
        date_max= date
        date_min= now
        hour_max = (date.hour+19)%24
        hour_min= now.hour

    print("year")
    if date_max.year < date_min.year:
        return False
    if date_max.year > date_min.year:
        return True
    print("month")
    if date_max.month < date_min.month:
        return False
    if date_max.month > date_min.month:
        return True
    print("day")
    if date_max.day < date_min.day:
        return False
    if date_max.day > date_min.day:
        return True
    print("hour")
    if hour_max < hour_min :
        return False
    if hour_max > hour_min:
        return False
    print("day")
    if date_max.minute < date_min.minute:
        return False
    if date_max.minute >= date_min.minute:
        return True

def compareDate2 (now, date, max):
    print(now)
    print(date)
    hour = date.hour -5
    day = date.day
    if hour < 0:
        hour = 24 + hour
        day = day -1

    cal_now= now.minute + now.hour*100 + now.day*10000 + now.month*1000000 + now.year*100000000
    cal_date= date.minute + hour*100 + day*10000 + date.month*1000000 + date.year*100000000
    print(cal_now)
    print(cal_date)
    print(str(max) +"|"+ str(False*max))
    if(cal_now>=cal_date):
        if max:
            return True
        return False
    if max:
        return False
    return True