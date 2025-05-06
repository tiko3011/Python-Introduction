import datetime

day_delta = datetime.timedelta(days=1)

start_date = datetime.date.today()
end_date = start_date + 7 * day_delta

for i in range((end_date - start_date).days):
    print(start_date + i*day_delta)

print(start_date-end_date)


date = datetime.date(2025, 1, 2)
print(date)

today = datetime.date.today()
print(today)

time = datetime.time(22, 15, 0)
print(time)

now = datetime.datetime.now()
now = now.strftime("%H %M %S %m %d %Y")
print(now)

targetDateTime = datetime.datetime(2020, 1, 2, 12, 30, 1)
currentDateTime = datetime.datetime.now()
if targetDateTime < currentDateTime:
    print("Past")
else:
    print("Future")
