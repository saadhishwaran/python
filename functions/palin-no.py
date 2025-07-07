import math

a = int(input('enter the no'))
b = str(a)
c = b[::-1]

if b == c:
    print(f'{a} is palindrome')
else:
    print(f'{a} is not palindrome')