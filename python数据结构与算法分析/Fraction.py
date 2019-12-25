class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def show(self):
        print(self.num, '/', self.den)

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = self.gcd(newnum, newden)
        return Fraction(newnum//common, newden//common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum
    
    def gcd(self, m,n):
        while m%n != 0:
            oldm = m
            oldn = n
            m = oldn
            n = oldm%oldn
        return n