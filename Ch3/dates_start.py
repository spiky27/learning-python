#
# Example file for working with date information
#

from datetime import date
from datetime import time
from datetime import datetime

def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
#    today = date.today()
#    print("today date is ", today)
#
#  # print out the date's individual components
#    print("date components: ", today.day, today.month, today.year)
#  
#  # retrieve today's weekday (0=Monday, 6=Sunday)
#    ddays = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
#    print("weekday: ", today.weekday(), " which is a ", ddays[today.weekday()])
  
  ## DATETIME OBJECTS
  # Get today's date from the datetime class
    today = datetime.now()
    print("Today is ", today)

  # Get the current time
    t = datetime.time(today)
    print("time is ", t)
 

  
if __name__ == "__main__":
  main();
  
