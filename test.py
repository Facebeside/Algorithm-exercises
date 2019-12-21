# class Fraction:
#     def __init__(self, top, bottom):
#         self.num = top
#         self.den = bottom

#     def __str__(self):
#         return str(self.num) + '/' + str(self.den)

#     def show(self):
#         print(self.num, '/', self.den)

#     def __add__(self, otherfraction):
#         newnum = self.num * otherfraction.den + self.den * otherfraction.num
#         newden = self.den * otherfraction.den
#         common = self.gcd(newnum, newden)
#         return Fraction(newnum//common, newden//common)

#     def __eq__(self, other):
#         firstnum = self.num * other.den
#         secondnum = other.num * self.den
#         return firstnum == secondnum
    
#     def gcd(self, m,n):
#         while m%n != 0:
#             oldm = m
#             oldn = n
#             m = oldn
#             n = oldm%oldn
#         return n

class LogicGate:

    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label
    
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):

    def __init(self, n):
        super().__init__(n)

        self.pinA = None
        self.pinB = None
    
    def getPinA(self):
        return int(input("Enter PinA" + self.getLabel() + '-->'))

    def getPinB(self):
        return int(input("Enter PinB" + self.getLabel() + '-->'))


class UnaryGate(LogicGate):

    def __init(self, n):
        super().__init__(n)

        self.pin = None
    
    def getPin(self):
        return int(input("Enter Pin" + self.getLabel() + '-->'))

class AndGate(BinaryGate):
    
    def __init__(self,n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0 