from statistics import median


class Statistics:
    def __init__(self):
        self.numbers = []
        self.max = 0
        self.min = 0
        self.mean = 0.00
        self.median = 0
    def add_numbers(self,number):
        self.numbers.append(number)
        self.numbers=sorted(self.numbers)
    def display(self):
        numbers = ''
        for i in range(len(self.numbers)):
            if i == 0:
                numbers+=f'{self.numbers[0]},'
            if i == len(self.numbers)-1:
                numbers+=f' {self.numbers[-1]}'
            else:
                numbers+=f' {self.numbers[i]},'
    def greatest(self):
        self.max=max(self.numbers)
    def smallest(self):
        self.min=min(self.numbers)
    def arithmetic_mean(self):
        total = sum(self.numbers)
        lenght = len(self.numbers)
        self.mean = total/lenght
    def mediana(self):
        self.numbers=sorted(self.numbers)
        lenght = len(self.numbers)
        if lenght%2 == 0:
            median1 = self.numbers[lenght//2]
            median2 = self.numbers[lenght//2-1]
            self.median = (median1+median2)/2
        else:
            self.median = self.numbers[lenght//2]
    def stats(self):
        print(f'Min: {self.min}, Max: {self.max}, Arithmetic mean: {self.mean}, Median: {self.median}')
stats = Statistics()
stats.add_numbers(12)
stats.add_numbers(37)
stats.add_numbers(6)
stats.add_numbers(9)
stats.add_numbers(17)
stats.display()
stats.greatest()
stats.smallest()
stats.arithmetic_mean()
stats.mediana()
stats.stats()