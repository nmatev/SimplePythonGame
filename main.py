print("Welcome to my first game!")
userName = input("What is your name? ")
age = int (input("What's your age? "))

print("Hello", userName, "you are", age, "years old.")

if age >= 18:
    print("You are old enough!")
elif age >= 14:
    print("You can play with supervision.")
else:
    print("You are not old enough to play...")