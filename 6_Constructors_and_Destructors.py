class Logger:
    def __init__(self):
        print("Object is Created.")

    def __del__(self):
        print("Object destroyed.")

obj1=Logger()
print(obj1)