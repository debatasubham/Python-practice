import datetime as dt
now = dt.datetime.now()
year = now.year
month = now.month
weekday = now.weekday()
print(year)
print(month)
print(weekday)
date_of_birth = dt.datetime(year=2005,month=6,day=15)
print(date_of_birth)
