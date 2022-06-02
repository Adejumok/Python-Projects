grade = int(input("Enter a grade: "))
if 100 >= grade >= 70:
    print("A")
elif 70 > grade >= 60:
    print("B")
elif 60 > grade >= 50:
    print("C")
elif 50 > grade >= 45:
    print("D")
elif 45 > grade >= 40:
    print("E")
elif grade < 45:
    print("F")
