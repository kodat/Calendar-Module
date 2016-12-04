# Enter your code here. Read input from STDIN. Print output to STDOUT
import datetime
import calendar
history = raw_input()
#month, day and hour
m, d, y = history.split()

date = datetime.datetime.strptime(y + '-' + m + '-' + d , '%Y-%m-%d')
day = calendar.day_name[date.weekday()]
#print value
print day.upper()