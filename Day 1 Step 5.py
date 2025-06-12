name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print(name + ", you are eligible to vote! 🗳️")
elif age >= 13:
    print(name + ", you are teenager. Enjoy learning! 📚")
else:
    print(name + ", you are a kid! Have fun 🧸")