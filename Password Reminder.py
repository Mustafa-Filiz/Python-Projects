name = "Mustafa"
entered_name = input("What is your name? ").title()

if entered_name == name:
    print("Hello, {}! Your password is : W@12 ".format(name))
else :
    print("Hello, {}! See you later.".format(entered_name))
