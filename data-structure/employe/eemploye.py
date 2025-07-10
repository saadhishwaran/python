def create():
    dict1 = {}
    name = input('enter eemploye name: ')
    age = int(input('enter eemploy age: '))
    salary = float(input('enter eemploye salary: '))
    postition = input('enter eemploye position: ')
    dict1.update({'name':name,'age':age,'salary':salary,'position':postition})
    list2.append(dict1)
    print(dict1)
    print(list2)

def update():
    dict1 = {}
    name = input('enter eemploye name: ')
    age = int(input('enter eemploy age: '))
    salary = float(input('enter eemploye salary: '))
    postition = input('enter eemploye position: ')
    dict1.update({'name':name,'age':age,'salary':salary,'position':postition})
    list2.append(dict1)
    print(dict1)
    print(list2)

def search():
    print('uhhhh')
    

def display():
    print(List1[0])
    print(List1[1])

List1 = [{'name':'aadthiya','age':30,'salary':100000.0,'position':'regional maneger'},{'name':'gokul','age':20,'salary':20000000.0,'position':'chief excecutive officer'}]
list2 = []
print(List1)
print("____x____X____x____")