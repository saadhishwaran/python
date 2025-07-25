a = int(input('enter the no: '))
b = []
c = []

for i in range(1,a+1):
    for j in range(1,i+1):
        if i%j != 0:
            c.append(j)
    else:
        b.append(a)
print(c)
print(b)