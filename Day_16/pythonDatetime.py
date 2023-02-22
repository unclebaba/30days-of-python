# Get the current day, month, year, hour, minute and timestamp from datetime module
import datetime
# current date
now = datetime.datetime.now()

# extract day, month, year, hour, minute from current date and time
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute

# timestamp
timestamp = datetime.datetime.timestamp(now)

print("current date and time:", now)
print("day:", day)
print("month:", year)
print("hour:", hour)
print("minute:", minute)
print("timestamp:", timestamp)

## Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
import datetime

# get current date and time
now = datetime.datetime.now()

# format the current date and time
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")

# print the formatted date
print("Formatted date:", formatted_date)


## Today is 5 December, 2019. Change this time string to time.
import datetime

# create a string representing the time
time_string = "5 December, 2019"

# use strptime() to convert the time string to a datetime object
time_obj = datetime.datetime.strptime(time_string, "%d %B, %Y")

# extract the time from the datetime object
time = time_obj.time()
print("Time:", time)


## Calculate the time difference between now and new year.
import datetime

# get the current date and time
now = datetime.datetime.now()

# create a datetime object for New Year's Day of the next year
new_year = datetime.datetime(now.year + 1, 1, 1)

# calculate the time difference between now and New Year's Day
time_diff = new_year - now
print("Time until New Year's Day:", time_diff)
print("Days:", time_diff.days)
print("Seconds:", time_diff.seconds)

## Calculate the time difference between 1 January 1970 and now.
import datetime

# get current date and time
now = datetime.datetime.now()

# get datetime object corresponding to Unix epoch
epoch = datetime.datetime.utcfromtimestamp(0)

# calculate the time difference between now and the Unix epoch
time_difference = now - epoch
print("Time difference in seconds:", time_difference.total_seconds())
print("Time difference in days:", time_difference.days)

## Think, what can you use the datetime module for? Examples:
# Time series analysis
# To get a timestamp of any activities in an application
# Adding posts on a blog