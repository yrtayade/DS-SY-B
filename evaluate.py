stack = []
exp = input("Enter an postfix expression sperated by space: ")

newexp =exp.split(" ")

for i in newexp:
    if i.isdigit():
        stack.append(i)
    else:
        num2 = int(stack.pop())
        num1 = int(stack.pop())
        if i == '+':
            result = num1 + num2 
            stack.append(result)
        elif i == '-':
            result = num1 - num2 
            stack.append(result)
        elif i == '*':
            result = num1 * num2 
            stack.append(result)
        elif i == '/':
            result = num1 / num2 
            stack.append(result)

print(  stack.pop() )

