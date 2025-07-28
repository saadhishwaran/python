import math

def is_prime(n):
    if n <= 1:
        return False
    elif n>1 :
        for i in range(2,int(math.sqrt(n+1))):
            if n%i == 0:
                return False
        return True                            

def lis_prime(a):
    list1 = []
    for i in range(2,a+1):
        if is_prime(i):
            list1.append(i)
    print(list1)

a = int(input('enter tne no: '))
lis_prime(a)