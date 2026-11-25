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

print(now.strftime("%Y-%m-%d %H:%M:%S"))