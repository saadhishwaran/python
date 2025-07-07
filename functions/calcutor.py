import math

def add(a,b):
    print(f'adding:{a}+{b}')
    return a+b

def sub(a,b):
    c = a-b
    print(c)

def multi(a,b):
    c = a*b 
    print(c)

def divid(a,b):
    if b == 0:
        print('division noy possible')
    else:
        c = a/b
        print(c)

def power(a,b):
    c = a**b
    print(c)

def root(a,b):
    c = math.sqrt(a)
    print(c)

def modulas(a,b):
    c = a%b
    print(c)

def floor(a,b):
    c = a//b
    print(c)

a = int(input("enter a: "))
b = int(input('enter b: '))
c = 0
op = input("enter any of one op = '+','-','*','/','po','sq','mod','flo'")

if op =='+' :
    print(add(a,b))
elif op == '-' :
    print(sub(a,b))
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