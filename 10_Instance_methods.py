class Dog:
    def __init__(self, name, breed):
        self.name = name      # instance variable
        self.breed = breed    # instance variable

    def bark(self):
        print(f"{self.name} says: Bow! bow!")

# Example usage:
dog1 = Dog("Ash", "Husky")
dog2 = Dog("Max", "German Shepherd")

dog1.bark()   
dog2.bark()   
