import random

def create():
    a = input('enter the customer name: ')
    b = int(input('enter the customer age: '))
    c = input('enter the customer job: ')
    d = random.randint(10)
    e = int(input('enter the 4 digits for password: '))
    f = float(input('enter the amount: '))
    i = int(input('enter the door no: '))
    j = input('enter the street name: ')
    h = input('enter the city name: ')
    list1.append({'name':a,'age':b,'job':c,'account_no':d,'password':e,'balance':f,'address':{'door_no':i,'street':j,'city':h}})
    print(list1)

def deposit():
    print('eee')

def withdraw():
    print(445455445)

list1 = []