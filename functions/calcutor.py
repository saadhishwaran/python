import math

def add(a,b):
    c = a+b
    print(c)

def sub(a,b):
    c = a-b
    print("the result is: ",c)

def multi(a,b):
    c = a*b 
    print("the result is: " ,c)

def divid(a,b):
    if b == 0:
        print('division noy possible')
    else:
        c = a/b
        print("the result is:",c)

def power(a,b):
    c = a**b
    print("the result is: ",c)

def root(a,b):
    if a < 0:
        print('can not find root of negative no')
    else:
        c = math.sqrt(a)
        print("the result is:",c)

def modulas(a,b):
    c = a%b
    print("the result is: ",c)

def floor(a,b):
    c = a//b
    print("the result is: ",c)

a = int(input("enter a: "))
b = int(input('enter b: '))
c = 0
print("the given operations are:")
print("'+'  for addition")
print("'-'  for subtraction")
print("'×'  for multiplication")
print("'/'  for division")
print("'po' for square")
print("'sq' for square root")
print("'mod' for modulas")
print("'flo' for floor division")
op = input("enter any of one of the given operations:").strip().lower()

if op =='+' :
    add(a,b)
elif op == '-' :
    sub(a,b)
elif op == '*' :
    multi(a,b)
elif op == '/' :
    divid(a,b)
elif op == 'po' :
    power(a,b)
elif op == 'sq' :
    root(a,b)
elif op == 'mod' :
    modulas(a,b)
elif op == 'flo' :
    floor(a,b)
else :
    print("invalid op given")