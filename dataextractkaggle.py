import datetime, calendar

lastFriday = datetime.date.today()
print(lastFriday)
oneday = datetime.timedelta(days=1)
print(oneday)
x = lastFriday.weekday()
print(x)
y = calendar.THURSDAY
print (y)

while lastFriday.weekday() != calendar.THURSDAY:
    lastFriday -= oneday

print (lastFriday.strftime("%D"))
print (lastFriday)