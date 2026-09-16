CQ = [None] * 5
F = -1
R = -1
size = len( CQ )

def insert(data):
    global F,R
    if F == (R+1)%size:
        print("FULL")
    else:
        if F== -1:
            F = 0
        R = (R+1) % size
        CQ[R] = data

def delete():
    global F,R
    if F == -1:
        print("EMPTY")
    else:
        x = CQ[F]
        if F == R:
            F = -1
            R = -1
        else:
            F = (F+1) % size

def display():
    global F,R
    if F == -1:
        print("EMPTY")
    else:
        i = F
        while True:
            print(CQ[i], end = ' ')    
            if i == R:
                break
            i = (i+1)%size
        print()
    
insert('A')
insert('B')
insert('C')
insert('D')
insert('E')
display()
delete()
delete()
delete()
delete()
delete()
display()