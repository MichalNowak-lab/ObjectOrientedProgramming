class C:
    def __init__(self,name,surname,age,seniority):
        self.name = name
        self.surname=surname
        self.age=age
        self.seniority=seniority
    def __str__(self):
        str=''
        str+=f'{self.surname}{self.name[0]}{self.seniority}'
        if self.age<18:
            str = str.lower()
            return str
        else:
            str=str.upper()
            return str
employee = C('Anna','May',17,7)
print(employee)
employee1 = C('Anna','May',21,7)
print(employee1)