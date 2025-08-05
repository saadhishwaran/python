import random

def create():
    name = input('enter the customer name: ')
    age = int(input('enter the customer age: '))
    job = input('enter the customer job: ')
    account_no = random.randint(1111111111,99999999999)
    password = int(input('enter the 4 digits for password: '))
    balance = float(input('enter the amount: '))
    door_no = int(input('enter the door no: '))
    street = input('enter the street name: ')
    city = input('enter the city name: ')
    list1.append({'name':name,'age':age,'job':job,'account_no':account_no,'password':password,'balance':balance,'address':{'door_no':door_no,'street':street,'city':city}})
    print(list1)

def deposit():
    deposit = int(input('enter the amount to deposit: '))
    for i in list1:
        i['balance'] += deposit
    print(list1)

def withdraw():
    withdraw = int(input('enter the amount to deposit: '))
    for i in list1:
        i['balance'] -= withdraw
    print(list1)

list1 = [{'name':'gokul','age':45,'job':'teacher','account_no':5555555555,'password':7878,'balance':780000.0,'address':{'door_no':54,'street':'north street','city':'paramathi'}}]
