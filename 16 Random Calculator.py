# These are the libraries I need to import for this.
import random
import time

#These let you type a number, and the program recognizes it.
num1 = input("Enter the first number.")
num2 = input("Enter the second number.")

# This is the fake "Doing stuff in the background" schpeel.
print("Randomizing...")
time.sleep(5)

# These are the variables that let you do math.
multiply = int(num1) * int(num2)
divide = int(num1) / int(num2)
subtract = int(num1) - int(num2)
addition =  int(num1) + int(num2)

# This randomizes it.
text = random.choice([multiply, divide, subtract, addition])

# This is the completed math! Or meth, I prefer meth.
print(text)
print("Math done! Enjoy this nonsensical answer!")