#write a program for average of 3 numbers using function, calculate sum in diffrent function and return result to average function to calculate average 


def addition(x,y,z):
    sum = (x+y+z)
    return sum
def average(a,b,c):
    avg = addition(a,b,c)/3
    print(avg)

average(4,5,6)

