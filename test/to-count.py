import string

a = input('enter a string: ')
b = len(a)
c = 0
d = 0

for i in range(b):
    if a.lower() == 'a' or 'e' or 'i' or 'o' or 'u':
        c += 1
        print(c)
    else :
        d += 1
        print(d) 
        break
