import random

def random_number():
    number = random.randint(1, 49)
    # Generate a random number between 1 to 49
    print(number)

# Call the function to generate 6 set of numbers
for i in range(6):
    random_number()