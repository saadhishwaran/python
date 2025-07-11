# s = input('enter the element to be found: ')
# dict1 = [{'name':'bob','age':39 },{'name':'pob','age':29 }]
# r = []
# for d in dict1:
#     if d.get('name') == s :
#         r.append(d)
# print(r)
dict1 = {}
n = int(input('enter the no: '))
for i in range(n):
    name = input('enter the keys: ')
    age = int(input('enter the values'))
    salary = float(input('enter eemploye salary: '))
    postition = input('enter eemploye position: ')
    dict1.update({'name':name,'age':age,'salary':salary,'position':postition})
print(dict1)