import random

def create():
    a = input('enter the customer name: ')
    b = int(input('enter the customer age: '))
    c = input('enter the customer job: ')
    d = random.randint(1111111111,99999999999)
    e = int(input('enter the 4 digits for password: '))
    f = float(input('enter the amount: '))
    i = int(input('enter the door no: '))
    j = input('enter the street name: ')
    h = input('enter the city name: ')
    list1.append({'name':a,'age':b,'job':c,'account_no':d,'password':e,'balance':f,'address':{'door_no':i,'street':j,'city':h}})
    print(list1)

def deposit():
    a = int(input('enter the amount to deposit: '))
    for i in list1:
        i['balance'] += a
    print(list1)

def withdraw():
    a = int(input('enter the amount to deposit: '))
    for i in list1:
        i['balance'] -= a
    print(list1)

list1 = [{'name':'gokul','age':45,'job':'teacher','account_no':5555555555,'password':7878,'balance':780000.0,'address':{'drro_no':54,'steeet':'north street','city':'paramathi'}}]
