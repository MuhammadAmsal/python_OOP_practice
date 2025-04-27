class Employee:
    def __init__(self,name,salary,ssn):
        self.name=name
        self._salary=salary
        self.__ssn=ssn

emp1=Employee("Ali",9000,7564746)
print(emp1.name)  # name is accessible because it is a public variable by default
#print(emp1.salary)  # not accessible because it is a protected variable 
#print(emp1.ssn)    # not accessible because it is a private variable