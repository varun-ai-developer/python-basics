#	1.1	Print numbers 1 to 10 using for loop

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Using For Loop:\n")

for number in numbers:
    print(number)

#	1.2	Print numbers 1 to 10 using while loop

i = 1
print("\n\nUsing While Loop:\n")

while i <= 10:
    print(i)
    i += 1

# 	2.	Print even numbers between 1 to 100

i2 = 2
print("\n\nEven numbers between 1 to 100\n")

while i2 <= 100:
    print(i2)
    i2 += 2

#3.	Table of any number using loops (like table of 5)

table = 5
print("\n\nMaking Table using Loop\n")

while table <= 50:
    print(table)
    table += 5

#	4.	Print sum of numbers 1 to 50

sum_1_to_50 = 0
i3 = 1

while i3 <= 50:
    sum_1_to_50 += i3
    i3 += 1

print("\n\nSum of numbers from 1 to 50:", sum_1_to_50)

#   5. Make a “password checker” (loop till correct password)

correct_password = "vatsvarun.121"

while True:
    user_input = input("\n\nEnter the password: ")
    if user_input == correct_password:
        print("Access Granted")
        break
    else:
        print("Incorrect Password, Try again.")
