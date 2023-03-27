# comparison operator

name = input("What is your name? ")

if len(name) < 3:
    validation_message = "Name must be at least 3 characters"
elif len(name) > 10:
    validation_message = "Name is too long"
else:
    validation_message = "Name looks good"
print(validation_message)
