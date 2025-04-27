class TemperatureConverter:
    def __init__(self,temp):
        self.temp_c=temp
        self.temp_f=TemperatureConverter.celsius_to_fahrenheit(self.temp_c)
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
 
    def display(self):
        print(f"{self.temp_c}'C into Fahrenheit is {self.temp_f}")

#temperature converter from celcius to fahrenheit
temp_c = TemperatureConverter(50)
temp_c.display()
