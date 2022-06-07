first_integer = int(input("Enter first integer: "))

second_integer = int(input("Enter second integer: "))

third_integer = int(input("Enter third integer: "))

fourth_integer = int(input("Enter fourth integer: "))

fifth_integer = int(input("Enter fifth integer: "))

if first_integer > second_integer and first_integer > third_integer and first_integer > fourth_integer and first_integer > fifth_integer:
    print("the largest is ", first_integer)


elif second_integer > first_integer and second_integer > third_integer and second_integer > fourth_integer and \
        second_integer > fifth_integer:
    print("the largest is ", second_integer)

elif third_integer > first_integer and third_integer > second_integer and third_integer > fourth_integer and \
        third_integer > fifth_integer:
    print("the largest is ", third_integer)

elif fourth_integer > first_integer and fourth_integer > second_integer and fourth_integer > third_integer and \
        fourth_integer > fifth_integer:
    print("the largest is ", fourth_integer)

elif fifth_integer > first_integer and fifth_integer > second_integer and fifth_integer > third_integer and \
        fifth_integer > fourth_integer:
    print("the largest is ", fifth_integer)



