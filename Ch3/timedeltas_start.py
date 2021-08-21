#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it
print(timedelta(days=365, hours=5, minutes=1))

# print today's date
now = datetime.now()
print("today is " + str(now))


# print today's date one year from now
print("one yer from now is ", now + timedelta(days=5))

# create a timedelta that uses more than one argument


# calculate the date 1 week ago, formatted as a string


### How many days until April Fools' Day?
today =date.today()
afd = date(today.year, 4, 1)


# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if afd < today:
    print("April fools day went by %d days ago" % ((today - afd).days))
else:
    print("April fools day is after ", afd - timedelta(days=today.day), " days")


# Now calculate the amount of time until April Fool's Day  

