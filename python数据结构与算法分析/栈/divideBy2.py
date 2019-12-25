# 将十进制数转二进制

from stack import Stack

def divideBy2(decNumber):
    remStack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remStack.push(rem)
        decNumber = decNumber // 2

    binString = ""
    while not remStack.isEmpty():
        binString = binString + str(remStack.pop())
    
    return binString


# 十进制转任意进制，设置一个字符串用于查询大于9的余数的值
def baseConverter(decNumber, base):
    digits = '0123456789ABCDEF'

    remStack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remStack.push(rem)
        decNumber = decNumber // base

    binString = ""
    while not remStack.isEmpty():
        binString = binString + digits[remStack.pop()]
    
    return binString
