#get month function
def get_month():
   month = int(input("Enter a month number: "))
   month_is_bad = True
   if month < 13 and month > 0:
      month_is_bad = False
   while month_is_bad:
      print("Month must be between 1 and 12.")
      month = int(input("Enter a month number: "))
      if month < 12 and month > 0:
         month_is_bad = False
   return month

#get year function
def get_year():
   year = int(input("Enter year: "))
   while year < 1752:
      print("Year must be 1753 or later.")
      year = input("Enter year: ")
   return year;

#offset from jan 1753
def offset_from_jan_1753(year):
   temp_year = int(1753)
   temp_offset = int(0)
   while temp_year < year:
      if (temp_year % 100 == 0 and temp_year % 400 != 0):
         temp_offset += 1
      elif temp_year % 4 == 0:
         temp_offset += 2
      elif temp_year % 4 != 0:
         temp_offset += 1
      temp_year += 1
   return temp_offset % 7

#days in feb
def days_in_feb(year):
   if (year % 100 == 0 and year % 400 != 0):
      return 28
   elif (year % 4 == 0):
      return 29
   elif (year % 4 != 0):
      return 28

#offset for current year
def offset_current_year(month, year, days_in_month):
   days = int(0)
   while month > 0:
      days = days + days_in_month[month - 1]
      month -= 1
   return days % 7

#compute offset
def compute_offset(month, year, days_in_month):
   offset = int(offset_from_jan_1753(year))
   offset = offset + offset_current_year(month, year, days_in_month)
   offset = offset % 7
   offset += 1
   return offset

#header function
def out_calendar(offset, year, month, days):
   month_names = ["where are my pants?", "January", "February", 
                  "March", "April", "May", "June", "July",
                  "August", "September", "October", "November",
                  "December"]
   print(month_names[month], ", ", year)
   print("   Su   Mo   Tu   We   Th   Fr   Sa")
   if offset != 7:
      offset_copy = offset
   else:
      offset_copy = 0
 
   while offset_copy != 0:
      print("     ", end="")
      offset_copy -= 1
   ## print the days of the calendar
   temp_day = int(1)
   while days > 0:
      if temp_day < 10:
         print("   ", temp_day, end="")
      elif temp_day > 9:
         print("  ", temp_day, end="")
      if (temp_day + offset) % 7 == 0:
         print()
      days -= 1
      temp_day +=1

## main
month = get_month()
year = get_year()
days_in_month = [0, 31, days_in_feb(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
offset = compute_offset(month, year, days_in_month)
out_calendar(offset, year, month, days_in_month[month])