# 匹配括号

from stack import Stack

def parChecker(symbolString):
    s = Stack()
    blance = True
    index = 0

    while index < len(symbolString) and blance:
        symbol = symbolString[index]

        if symbol == '(':
            s.push(symbol)
        else:
            # ())))
            if s.isEmpty():
                blance = False
            else:
                s.pop()
        index += 1
    
    if blance and s.isEmpty():
        return True
    else:
        return False


def parChecker2(symbolString):
    s = Stack()
    blance = True
    index = 0

    while index < len(symbolString) and blance:
        symbol = symbolString[index]

        if symbol in '([{':
            s.push(symbol)
        else:
            # ())))
            if s.isEmpty():
                blance = False
            else:
                top = s.pop()
                if not match(top, symbol):
                    blance = False
        index += 1
    
    if blance and s.isEmpty():
        return True
    else:
        return False

def match(open, close):
    opens = "([{"
    closes = ")]}"

    return opens.index(open) == closes.index(close)