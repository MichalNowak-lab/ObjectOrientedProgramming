class C:
    def __init__(self,sectors):
        self.fans = sectors
    def m1(self,s,n):
        self.fans[s]=n
    def m2(self,s):
        total = 0
        keys = ''
        for key in self.fans:
            keys+=key
        for letter in s:
            if letter not in keys:
                continue
            total+=self.fans[letter]
        print(total)
stadium = C({"A":120,"D":150,"G":90,"K":110})
stadium.m1('G',130)
stadium.m2('GD')
stadium.m2('KEJ')