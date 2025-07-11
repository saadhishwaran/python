s = input('enter the element to be found: ')
dict1 = [{'name':'bob','age':39 },{'name':'pob','age':29 }]
r = []
for d in dict1:
    if d.get('name') == s :
        r.append(d)
print(r)