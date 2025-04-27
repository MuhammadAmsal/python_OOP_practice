class Bank:
    Bank_Name="Habib Al Habib Limited"

    @classmethod
    def Change_Bank_Name(cls,name):
        cls.Bank_Name=name
    
    def display(self):
        print(f"Bank Name: {self.Bank_Name}")


customer1=Bank()
customer1.display()
customer1.Change_Bank_Name("United Bank Limited")
customer2=Bank()
customer2.display()
customer3=Bank()
customer3.display()