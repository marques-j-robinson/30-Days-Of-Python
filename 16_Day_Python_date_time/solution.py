from datetime import date, datetime
today = date.today()
now = datetime.now()
print(now)
print(f'day {today.day}')
print(f'month {today.month}')
print(f'year {today.year}')
print(f'hour {now.hour}')
print(f'minute {now.minute}')
print(f'timestamp {now.timestamp()}')

print(now.strftime("%m/%d/%Y, %H:%M:%S"))

date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)