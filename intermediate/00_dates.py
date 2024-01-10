## Dates ##

# Obtencion de informacion de fecha y hora
from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta

now = datetime.now()

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)

year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second
print(year, month, day, hour, minute, second)
# La marca de tiempo o marca de tiempo de Unix es el número de segundos transcurridos desde el 1 de enero de 1970 UTC.
print("Timestamp:", now.timestamp())
print(f"{day}/{month}/{year}, {hour}:{minute}:{second}")

# Formateo de la salida de fecha mediante strftime
new_year = datetime(2025,1,1)
print(new_year)

year = new_year.year
month = new_year.month
day = new_year.day
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(year, month, day, hour, minute, second)
print(f"{day}/{month}/{year}, {hour}:{minute}:{second}")

# Python cheatsheet strftime https://strftime.org/
t = now.strftime("%I:%M:%S %p.")
print(t)
time_one = now.strftime("%m/%d/%y %I:%M:%S %p.")
print(time_one)
time_two = now.strftime("%d/%m/%y %I:%M:%S %p.")
print(time_two)

# Cadena a tiempo usando strptime
date_string = "10 January, 2024"
print(date_string)
print(type(date_string))

date_object = datetime.strptime(date_string, "%d %B, %Y")
print(date_object)
print(type(date_object))

# Segundo ejemplo
date_string = "06/02/1976 09:32:10"
print(date_string)
print(type(date_string))

date_object_1 = datetime.strptime(date_string, "%d/%m/%Y %H:%M:%S")
print("date_object_1",date_object_1)
date_object_2 = datetime.strptime(date_string, "%m/%d/%Y %H:%M:%S")
print("date_object_2",date_object_2)

# Uso de la fecha de la fecha y hora
d = date(1997,8,10)
print(d)
print("Current date:", d.today())
today = date.today()
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

# Objetos de tiempo para representar el tiempo

# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)
# time(hour, minute, second)
b = time(9,40,10)
print("b =", b)
# time(hour=9, minute=40, second=10)
c = time(hour=9, minute=40, second=10)
print("c =", c)
# time(hour, minute, second, microsecond)
d = time(9, 40, 10, 100897)
print("d =", d)

# Diferencia entre dos puntos en el tiempo
today = date.today()
new_year = date(2025,1,1)
time_left_to_new_year = new_year - today
print(time_left_to_new_year)

t1 = datetime.now()
t2 = datetime(2024,1,12,4,30,50)
diff = t2 - t1
print(diff)

# Diferencia entre dos puntos en el tiempo usando timedelta
# t1 = timedelta(weeks=8, days=10, hours=10, minutes=43, seconds=40)
# t2 = timedelta(weeks=5, days=23, hours=16, minutes=23, seconds=20)
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)