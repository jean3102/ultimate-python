from datetime import datetime, timedelta

# Define two datetime objects
start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 2, 1)

# Add 3 weeks to a date
three_weeks_later = start_date + timedelta(weeks=3)
print(f"Three weeks after {start_date.date()}: {three_weeks_later.date()}")

# Show original date again for comparison
print(f"Original start date: {start_date.date()}")

# Calculate the difference between two dates
delta = start_date - end_date

# Display the difference components
print(f"Timedelta (start - end): {delta}")
# Seconds part of leftover time only
print(f"Seconds (within the day): {delta.seconds}")
print(f"Microseconds: {delta.microseconds}")
print(f"Total seconds (including negative days): {delta.total_seconds()}")
