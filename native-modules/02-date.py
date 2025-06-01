from datetime import datetime

# Define specific datetime objects
date1 = datetime(2025, 1, 1)
date2 = datetime(2025, 2, 1)

# Current datetime
now = datetime.now()

# Display datetime values
print(f"Date 1: {date1}")
print(f"Date 2: {date2}")
print(f"Now: {now}")

# Parse a date string and format it differently
parsed_date = datetime.strptime("04-06-2025", "%m-%d-%Y")
formatted_date = parsed_date.strftime("%Y/%m/%d")
print(f"Parsed date (from string): {parsed_date}")
print(f"Formatted date: {formatted_date}")

# Comparison between two dates
print(f"Is date1 > date2?: {date1 > date2}")

# Access individual components of the current date and time
print("Current datetime components:")
print(
    f"Year: {now.year}, Month: {now.month}, Day: {now.day}, "
    f"Hour: {now.hour}, Minute: {now.minute}, Second: {now.second}"
)
