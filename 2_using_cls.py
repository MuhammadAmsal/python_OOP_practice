class Counter:
    count=0

    @classmethod
    def counter(cls):
        cls.count+=1
        print(f"{cls.count} object has been created")

Counter.counter()
Counter.counter()
Counter.counter()
Counter.counter()
