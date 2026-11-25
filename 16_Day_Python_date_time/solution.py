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

now = datetime.now()
new_year = datetime(now.year + 1, 1, 1)
time_left = new_year - now
print(f"Days left: {time_left.days}")
print(f"Exact countdown: {time_left}")

old_year = datetime(1970, 1, 1)
diff = now - old_year
print(f"Days diff: {diff.days}")
print(f"Exact time diff: {diff}")