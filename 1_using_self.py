class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def display(self):
        print(f"Name: {self.name}\nMarks: {self.marks}")
        

student1=Student("Amsal",95)
student1.display()
