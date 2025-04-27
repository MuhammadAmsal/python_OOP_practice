class A:
    def show(self):
        print("Greetings from A")

class B(A):
    def show(self):
        print("Greeting from B")

class C(A):
    def show(self):
        print("Greeting from C")

class D(B, C):
    pass

d = D()
print(D.mro())   
