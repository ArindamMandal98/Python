import calendar
y=int(input('Enter the year:'))

for i in range(1,13):
    print(calendar.month(y,i))
