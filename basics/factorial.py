a = int(input('enter a number: '))
b = 1

if a == 0 :
    print('the value is: 1;')
elif a == 1:
    print('the value is: 1;')
else:
    for i in range(1,a+1):
        b *= i
    print('the value is:',b)

    