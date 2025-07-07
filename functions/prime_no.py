import math

n = int(input('enter an number: '))

if n <= 1:
    print(f'{n} is not a  prime')
elif n>1 :
    for i in range(2,n):
        if n%i == 0:
            print(f'{n} is not a prime number')
            print(f'{n}  is the factor of {i}')
            break
    else:
        print(f'{n} is prime')