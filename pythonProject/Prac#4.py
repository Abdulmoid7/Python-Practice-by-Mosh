from datetime import date
today = date.today()
print("Today's date:", today)

from datetime import datetime, timedelta

# Get today's date
today = datetime.today()

# Calculate yesterday's date by subtracting one day
yesterday = today - timedelta(days=1)

print("Yesterday's date:", yesterday.date())


print("Today's date is: " + str(date.today()))
print("Yesterday's date is: " + str(date.today()))

parsecs = 11
lightyears = parsecs * 3.26
print(str(parsecs) + " parsecs is " + str(lightyears) + "lightyears")

