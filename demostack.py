stack = [None] * 3
size  = len(stack)
top = -1

def push(data):
    global top
    if top == (size-1):
        print("FULL")
    else:
        top =top + 1
        stack[top]= data

def pop():
    if top == -1:
        print("Empty")
    else:
        x = stack[top]
        top = top - 1
        return x
    
def display():
    if top == -1:
        print("Empty")
    else:
        for i in range(0, top+1):
            print(stack[i] , end= " " )
    print()

push(11)
push(17)
push(2)
display()
print(pop())