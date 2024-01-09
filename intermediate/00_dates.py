## Dates ##

# Obtencion de informacion de fecha y hora
from datetime import datetime

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

#Python cheatsheet strftime https://strftime.org/
t = now.strftime("%I:%M:%S %p.")
print(t)