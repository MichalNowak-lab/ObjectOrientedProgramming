import random
class Thermometer:
    def init(self):
        self.is_on=False
        self.temp=0
    def turn_on(self):
        self.is_on=True
    def turn_off(self):
        self.is_on=False
    def measure(self):
        if self.is_on:
            self.temp=round(random.uniform(34.0,42.0),1)
    def display(self):
        if self.is_on:
            if self.temp>=37 and self.temp<41:
                print(f'Temperature: {self.temp}C (fever)')
            elif self.temp>41:
                print(f'Temperature: {self.temp}C (CRITICAL TEMPERATURE)')
            else:
                print(f'Temperature: {self.temp}C')
