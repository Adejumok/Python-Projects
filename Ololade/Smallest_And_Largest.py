first_integers = int(input('Enter first integer: '))

second_integers = int(input('Enter second integer: '))

third_integers = int(input('Enter third integer: '))

int_sum = first_integers + second_integers + third_integers
print("The sum is ", sum)

int_average = int_sum // 3
print("The average is ", int_average)

int_product = first_integers * second_integers * third_integers
print("The product is ", int_product)

if first_integers > second_integers and first_integers > third_integers:
    print("first_integers is the largest")

if second_integers > first_integers and second_integers > third_integers:
    print("second_integers is the largest")

if third_integers > first_integers and third_integers > second_integers:
    print("third_integers is the largest")

if first_integers < second_integers and first_integers < third_integers:
    print("first_integers is the smallest")

if second_integers < first_integers and second_integers < third_integers:
     print("second_integers is the largest")

if third_integers < first_integers and third_integers < second_integers:
    print("third_integers is the smallest ")


