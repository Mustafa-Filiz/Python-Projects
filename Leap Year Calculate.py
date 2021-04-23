year = int(input("Enter the year that you want to learn \
if it's a leap year. : "))

if (year % 4) == 0:
  leap = True
  if (year % 100) == 0:
    leap = False
    if (year % 400) == 0:
      leap = True
else:
  leap = False

print(leap)

print("True means it'a leap year, False means it's not a leap year.")