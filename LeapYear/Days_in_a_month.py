
#This will require the user to enter the year and month of choice
year = int(input("Enter the year of your choice: ")) 
month = int(input("Enter the month of your choice: ")) 


"""
    This function determines  whether a year is a leap year or not.
    
    Inside the parameters we find the year to be checked if its a leap year or not.

    A year must be divisible by 4 for it to be a leap year, but except for years that are divisble by 100 but not divisble by 400.

    The funtion will return True if its a leap year and False if its not a year.
    
    """
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False 

"""
    This function is responsible for getting the number of days in a month of a year.
    
    The parameters there is the year and the month to determine the number of days in a month of that year
    
    
    """
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if month == 2 and is_leap(year):
    return 29
  else:
    return month_days[month - 1]
  

 
if __name__=="__main__":
  leap = is_leap(year)
  days = days_in_month(year, month)
  print(f"Is this a leap year?:  {leap}")
  print(f"There are {days} days in this month.")