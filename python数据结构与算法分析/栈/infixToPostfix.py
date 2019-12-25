# from stack import Stack
import string

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)


# 中序表达式到后序表达式
def infixToPostfix(infixexpr):
    # 定义优先级
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1

    opStack = Stack()
    postList = []

    tokenList = infixexpr.split()

    for token in tokenList:
        if token in string.ascii_uppercase:
            postList.append(token)
        elif token == "(" :
            opStack.push(token)
        elif token == ")":
            topStack = opStack.pop()
            while topStack != "(":
                postList.append(topStack)
                topStack = opStack.pop()
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postList.append(opStack.pop())
            opStack.push(token)
    
    while not opStack.isEmpty():
        postList.append(opStack.pop())
    
    return " ".join(postList)


# 计算后序表达式
def postfixEval(postfixExpr):
    operandStack = Stack()

    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(result)
    
    return operandStack.pop()


def doMath(op, op1, op2):
    if op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2
    elif op == "*":
        return op1 * op2
    else:
        return op1 / op2