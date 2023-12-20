
def is_leap(year):
  if year % 4 == 0 and year % 100 != 0 or year % 400 == 0: return True
  else: return False


def day_of_year(day, month ,year):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year):
        days_in_month[2] = 29 

    day_of_years = sum(days_in_month[:month]) + day
    return day_of_years

def day_in_year(year):
   return 366 if is_leap(year) else 365

def check_date(day, month, year):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month < 1 or month > 12:
        return False

    if is_leap(year):
        days_in_month[2] = 29

    if day < 1 or day > days_in_month[month]:
        return False

    return True

def date_diff(date_1, date_2):
  day1, month1, year1 = map(int, date_1.split("-"))
  day2, month2, year2 = map(int, date_2.split("-"))

  if not check_date(day1, month1, year1) or not check_date(day2, month2, year2):
        return -1

  day_count = day_in_year(year1) - day_of_year(day1,month1,year1) + 1 + day_of_year(day2, month2, year2)
  for i in range (year1+1,year2):
     day_count += day_in_year(i)
  return day_count

print(date_diff("28-2-1999","29-2-2000"))