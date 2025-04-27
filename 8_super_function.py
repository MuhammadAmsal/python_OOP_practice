class Person:
    def __init__(self,name):
        self.name=name

class Teacher(Person):
    def __init__(self, name,subject):
        super().__init__(name)
        self.course=subject
    
    def display(self):
        print(f"Teacher Name: {self.name}\nCourse: {self.course}")

teahr1=Teacher("Wahab","Science")
teahr1.display()