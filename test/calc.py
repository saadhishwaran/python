def add():
    a = int(input('enter a: '))
    b = int(input('enter b: '))
    c = a+b
    print(c)

def sub():
    a = int(input('enter a: '))
    b = int(input('enter b: '))
    c = a-b
    print(c)

def multi():
    a = int(input('enter a: '))
    b = int(input('enter b: '))
    c = a*b
    print(c)

def divid():
    a = int(input('enter a: '))
    b = int(input('enter b: '))
    if b == 0:
        print('no division possible: ')
    else:
        c = a/b
    print(c)

a = input("Enter any one operator = '+','-','*','/': ")

if a == '+':
    add()
elif a == '-':
    sub()
elif a == '*':
    multi()
elif a == '/':
    divid()
else:
    print('invalid operator given ;')