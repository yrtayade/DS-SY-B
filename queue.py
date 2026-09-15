queue = [None] * 3 
F = -1
R = -1
size = len( queue )

def insert(data):
    global F, R
    if R == (size -1 ):
        print("FULL")
    else:
        if F == -1:
            F = 0
        R = R + 1
        queue[R] = data

def delete():
    global F, R
    if F == -1 or F > R:
        print("EMPTY")
    else: 
        x = queue[F]
        F =  F + 1
        if F > R:
            F = -1
            R = -1
        return x

def display():
    global F, R
    if F == -1 or F > R:
        print("EMPTY")
    else:
        for i in range(F, R+1):
            print( queue[i] , end = " " )
    print()

insert('A')
insert('B')
insert('C')
display()
delete()
delete()
delete()
display()