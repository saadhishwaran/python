def fibonaci(a):
    b,c = 0,1
    for i in range(a):
        print(b,end=' ')
        b,c = c,c+b

a = int(input('enter a number: '))
fibonaci(a)