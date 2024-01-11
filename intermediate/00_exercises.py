from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta

# 1 Get the current day, month, year, hour, minute and timestamp from datetime module
now = datetime.today()
print("Current year:", now.year)
print("Current month:", now.month)
print("Current day:", now.day)
print("Current hour:", now.hour)
print("Current minute:", now.minute)
print("Timestamp:", now.timestamp())
print(now)

# 2 Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
current_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print(current_date)

# 3 Today is 5 December, 2019. Change this time string to time.
date_string = "11 January, 2024"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print(date_object)

# 4 Calculate the time difference between now and new year.
today = date.today()
new_year = date(2025, 1, 1)
diff = new_year - today
print(diff)

# 5 Calculate the time difference between 1 January 1970 and now.
now = datetime.now()
epoch = datetime(1970, 1, 1)
diff = now - epoch
print(diff)