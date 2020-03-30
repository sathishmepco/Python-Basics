from datetime import datetime

now = datetime.now()
print('Now is -',now)
print('Day is -',now.strftime('%A'))
print('Short Day is -',now.strftime('%a'))

print('Year is -',now.year)
print('Month is -',now.month)
print('Date is -',now.day)
print('Hour is -',now.hour)
print('Minute is -',now.minute)
print('Second is -',now.second)

print('------Set the date time object')
date = datetime(2020, 5, 17)
print(date)