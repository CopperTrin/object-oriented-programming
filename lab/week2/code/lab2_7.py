
def is_leap(year):
  if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    return True
  else:
    return False
  
def day_of_year(day, month ,year):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap(year):
        days_in_month[2] = 29 

    day_of_years = sum(days_in_month[:month]) + day
    return day_of_years


print(is_leap(1200))
print(day_of_year(3, 8, 1200))