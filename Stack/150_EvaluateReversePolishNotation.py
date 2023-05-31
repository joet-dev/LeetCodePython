import math 

def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    stack = [] 
    for t in tokens: 
        if t == "+": 
            stack.append(stack.pop() + stack.pop())
        elif t == "-": 
            secnd = stack.pop()
            stack.append(stack.pop() - secnd)
        elif t == "*": 
            stack.append(stack.pop() * stack.pop())
        elif t == "/": 
            secnd = stack.pop()
            stack.append(int(float(stack.pop()) / secnd))
        else: 
            stack.append(int(t))

    return stack[0]


print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))