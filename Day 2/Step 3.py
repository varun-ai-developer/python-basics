#	1.	Write a program to check if a number is even or odd.

num1 = int(input("Enter a number to check if it is even or odd:"))

if num1 % 2 == 0:
    print(num1, "is a even number.")
else:
    print(num1, "is a odd number.")


#	2.	Write a program to check if a number is positive, negative, or zero.

num2 = int(input("Enter a number to check if it is positive, negative or zero:"))

if num2 > 0:
    print(num2, "is positive.")
elif num2 < 0:
    print(num2, "is negative")
else:
    print(num2, "is zero")

#	3.	Write a program that asks marks and gives grade:

num3 = int(input("Enter Marks to check Grade:"))
if num3 >= 90:
    print("Grade A")
elif num3 >= 75:
    print("Grade B")
elif num3 >= 50:
    print("Grade C")
else:
    print("Fail")
