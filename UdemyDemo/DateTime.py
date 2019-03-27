import datetime

t=datetime.time(17,15,40)
print(t)

print(datetime.time.max)
print("todays date :",datetime.date.today())

d=datetime.date(2020,2,2)
print('date is :',d)
d2=d.replace(year=2019)
print('date replaced is :',d2)