class Countdown:
    def __init__(self, start):
        self.start = start  

    def __iter__(self):
        """Return the iterator object (self)"""
        self.current = self.start 
        return self 

    def __next__(self):
        """Return the next value in the countdown"""
        if self.current <= 0:
            raise StopIteration 
        self.current -= 1  
        return self.current 

countdown = Countdown(10)

for number in countdown:
    print(number)
