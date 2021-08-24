#A program that displays the days in a particular month
def is_leap(year):
    """checks if a year is leap or not"""
    if year %4 ==0:
        if year %100 ==0:
            if year % 400==0:
                return True
            else:
               return False
        else:
            return True
    else:
        return False
def days_in_month(year,month):
    """generates the number of days in a month"""
    if month<1 or month>12:
         return "Invalid"
    month_days=[31,28,31,30,31,31,30,31,30,31,30,31]
    if is_leap(year) and month==2:
         return 29
     
    return month_days[month-1]
year = int(input("enter a year:"))
month = int(input("enter a month:"))
days = days_in_month(year,month)
print(f"this month has {days} days")