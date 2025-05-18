# import time
# print(time.time())

from datetime import datetime

date1 = datetime(2025, 1, 1)
date2 = datetime(2025, 2, 1)
now = datetime.now()
print(f"date1: {date1}")
print(f"date2: {date2}")
print(f"now: {now}")


date_str = datetime.strptime("04-06-2025", "%m-%d-%Y")
formated_date = date_str.strftime("%Y/%m/%d")
print(f"date_str: {date_str}")
print(f"formated_date: {formated_date}")

print(f"conditional: {date1 > date2}")

print(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second,
)
