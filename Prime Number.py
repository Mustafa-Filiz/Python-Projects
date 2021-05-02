n = int(input("Enter a number : "))

control = False

if n > 1:
    for i in range(2, n):
        if (n % i) == 0:
            control = True

if control:
    print(n, "is not a Prime number.")
else:
    print(n, "is a Prime number.")