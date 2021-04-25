number = input("Enter a number : ").strip()

while True:   
    if number.isdecimal():
        break
    else:
        number = input(" It is an invalid entry. Don't use non-numeric, float, or negative values! : ")

sum_digit = 0

for i in range(len(number)):
    sum_digit += int(number[i]) ** len(number)


if sum_digit == int(number):
    print(f"{number} is an Armstrong number.")
else :
    print(f"{number} is not an Armstrong number.")
