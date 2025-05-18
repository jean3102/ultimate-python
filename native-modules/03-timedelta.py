from datetime import datetime, timedelta

date1 = datetime(2025, 1, 1)
date2 = datetime(2025, 2, 1)


date3 = datetime(2025, 1, 1) + timedelta(weeks=3)
date4 = datetime(2025, 1, 1)
print(f"date3: {date3}")
print(f"date4: {date4}")

delta = date1 - date2
print(f"secound: {delta.seconds}")
print(f"microseconds: {delta.microseconds}")
print(f"microseconds: {delta.total_seconds()}")
