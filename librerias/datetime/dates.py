
from datetime import datetime



now =  datetime.now()




def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)


year_2025 = datetime(2027,6,23)

print_date(year_2025)



from datetime import time


current_time = time(21,6,0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2025,7,6)

### modificar fechas

current_date = date(current_date.year +1,current_date.month +1,current_date.day)


print(current_date)


diff = year_2025 -now
print(diff)
diff = year_2025.date() - current_date
print(diff)


from datetime import timedelta

time_delta = timedelta()

start_timedelta = timedelta(200,100,100,weeks=10)
end_timedelta = timedelta(300,100,100,weeks=13)


print(end_timedelta-start_timedelta)
print(end_timedelta + start_timedelta)

