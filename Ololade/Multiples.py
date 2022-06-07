first_integers = int(input("Enter first integer: "))

second_integers = int(input("Enter second integer: "))

int_tripled = first_integers * first_integers * first_integers
int_doubled = second_integers * second_integers

if int_tripled % int_doubled == 0:
    print("it is divisible")

else:
    print("It is not divisible")