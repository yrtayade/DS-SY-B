stack = [None] * 100
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
    global top
    if top == -1:
        print("Empty")
    else:
        x = stack[top]
        top = top - 1
        return x


   

myname = "Mahesh" 
for i in myname:
    push(i)

while top != -1:    
        print(pop(), end = "")

print()
