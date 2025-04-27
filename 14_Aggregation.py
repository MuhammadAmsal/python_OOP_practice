class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, name, employee):
        self.name = name
        self.employee = employee  

    def show(self):
        print(f"Department: {self.name}")
        print(f"Department: {self.employee.name}")
        


emp1 = Employee("Alice")
dept1 = Department("Human Resources", emp1)

dept1.show()
