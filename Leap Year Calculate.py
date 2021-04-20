year = int(input("Enter the year that you want to learn \
if it's a leap year. : "))
a = year % 4  
b = year % 100  
c = year % 400  
d = bool(not a or not c and b)

print("The answer is", d, sep=" : ")

print("True means it'a leap year, False means it's not a leap year.")