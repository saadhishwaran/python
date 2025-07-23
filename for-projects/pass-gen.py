import random

def generator(length):
    charr = name + ag 
    for i in range(length) :
        password = ''.join(random.choice(charr))
        print(password,end = '')

length = int(input('Enter how long the password should be: '))
name = input('enter the name: ')
age = input('enter year of birth: ')
ag = str(age)
generator(length)