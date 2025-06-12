#  1.	Make a function to check whether a number is even or odd

print("lets check number is even or odd\n")
def is_even_or_odd(num):
    if num % 2 == 0:
        return "Your Number is Even"
    else:
        return "Your Number is Odd"

Num = int(input("Enter your number: "))
result = is_even_or_odd(Num)
print("Result:", result)


#  2.	Create a function that returns the maximum of 3 numbers

print("\n\nlets find maximum of three numbers\n")
def max_of_three(a, b, c):
    return max(a, b, c)

x = int(input("Enter 1st Number: "))
y = int(input("Enter 2nd Number: "))
z = int(input("Enter 3rd Number: "))

maximum = max_of_three(x, y, z)
print("Result:", maximum)


#  	3.	Make a function that prints the table of a number

print("\n\nlets find table of a number\n")
def table(t):
    for i in range(1, 11):
        print(f"{t} x {i} = {t * i}")

tablenumber = int(input("Enter a Number for Table: "))
table(tablenumber)

#  	4.	Build a function that returns factorial of a number

print("\n\nlets Build a function that returns factorial of a number\n")
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

factnumber = int(input("Enter a Number for Factorial: "))
print("Result:", factorial(factnumber))