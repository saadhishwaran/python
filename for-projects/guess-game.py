import random

c = int(input('enter your guess: '))
a = int(input('enter the min in range: '))
b = int(input('enter the max in range: '))

inte = random.randint(a,b)

if inte == c :
    print('your right; ')
else:
    print('your worng; ',inte)