# create a custom exception
class InvalidAgeError(Exception):
    pass

# Function that checks if age is valid
def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Age must be above of 18.")
    else:
        return f"Age {age} is valid."


try:
    age = 15  
    print(check_age(age))
except InvalidAgeError as e:
    print(f"Error: {e}")  
