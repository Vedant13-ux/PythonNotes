import datetime
mytime=datetime.time(2,20,50,90)
print(mytime)
#returns-->02:20:50.000090
print(mytime.minute)
#Return -->20
print(mytime.hour)
#Return -->2

today=datetime.date.today()
print(today)
#Returns-->2020-06-30

#Some More Methods

print(today.ctime())
#Tue Jun 30 00:00:00 2020

print(today.year)


#When we want date and time together
from datetime import datetime

