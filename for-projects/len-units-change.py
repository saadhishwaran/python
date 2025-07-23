def centi():
    print('from this you can convert to inch and foot')
    print('Press:')
    print('     inch for inches')
    print('     fot for foots')
    b = input('enter what do you want to convert:')
    d = int(input('enter the no to convert: '))
    c = 0
    if b.lower() == 'inch':
        c = d / 2.54
        print('the inch value of given is:',c)
    elif b.lower() == 'fot':
        c = d / 30.48
        print('the foot value of given is:',c)

def inches():
    print('from this you can convert to centimeter and foot')
    print('Press:')
    print('     cem for centimeters')
    print('     fot for foots')
    b = input('enter what do you want to convert:')
    d = int(input('enter the no to convert: '))
    c = 0
    if b.lower() == 'cem':
        c = d * 2.54
        print('the centimeter value of given is:',c)
    elif b.lower() == 'fot':
        c = d / 12
        print('the foot value of given is:',c)

def foots():
    print('from this you can convert to inch and cem')
    print('Press:')
    print('     inch for inches')
    print('     cem for centimeters')
    b = input('enter what do you want to convert:')
    d = int(input('enter the no to convert: '))
    c = 0
    if b.lower() == 'inch':
        c = d * 12
        print('the inch value of given is:',c)
    elif b.lower() == 'cem':
        c = d * 30.48
        print('the centimeters value of given is:',c)

print('avilable units are: ')
print('     cm for centimeter;')
print('     inch for inches;')
print('     fot for foots;')
a = input('enter the unit which is to be given: ')

if a.lower() == 'cm':
    centi()
elif a.lower() == 'inch':
    inches()
elif a.lower() == 'fot':
    foots()
else:
    print('Invalid operator given;')