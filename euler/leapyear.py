def monthdays(month, year):
    if month in (4, 6, 9, 11):
        return 30
    elif month == 2:
        if year%4 == 0 and year%100 != 0 or year%400 == 0:
        #if year%4 == 0 and year != 1900:
            return 29
        return 28
    return 31

def incdate(date):
    wd, day, month, year = date
    wd += 1
    if wd > 6:
        # it's sunday!
        wd = 0
    day += 1
    if day > monthdays(month, year):
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1
    return wd, day, month, year

weekdays = range(7)
weekdays[0] = "monday"
weekdays[1] = "tuesday"
weekdays[2] = "wednesday"
weekdays[3] = "thursday"
weekdays[4] = "friday"
weekdays[5] = "saturday"
weekdays[6] = "sunday"
months = range(12)
months[0] = "jan"
months[1] = "feb"
months[2] = "mar"
months[3] = "apr"
months[4] = "may"
months[5] = "jun"
months[6] = "jul"
months[7] = "aug"
months[8] = "sep"
months[9] = "oct"
months[10] = "nov"
months[11] = "dec"
date = [0, 1, 1, 1900]
acc = False
while date[3] != 2001:
    wd, day, month, year = date
    if not acc and year == 1901:
        acc = 1
    if acc:
        if wd == 6 and day == 1:
            acc += 1
    print weekdays[wd], day, months[month-1], year, "\t", acc
    date = incdate(date)
    #raw_input()
print acc - 1