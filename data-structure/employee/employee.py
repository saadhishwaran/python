def create(): 
    dict1 = {}
    n = int(input('enter the no: '))
    for i in range(n):
        name = input('enter the name: ')
        age = int(input('enter the age: '))
        salary = float(input('enter eemploye salary: '))
        postition = input('enter eemploye position: ')
        # dict1.setdefault({'name':name,'age':age,'salary':salary,'position':postition})
        list1.append({'name':name,'age':age,'salary':salary,'position':postition})
    print(list1)

def update():
    list1.clear()
    n = int(input('enter the no: '))
    for i in range(n):
        name = input('enter the name: ')
        age = int(input('enter the age: '))
        salary = float(input('enter eemploye salary: '))
        postition = input('enter eemploye position: ')
        list1.append({'name':name,'age':age,'salary':salary,'position':postition})
    print(list1)  
    
def search():
    s = input('enter the username to be found: ')
    r = []
    for d in list1:
        if d.get('name') == s :
            r.append(d)
    print(r)

def display():
    print(list1[0])
    print('___x___X___x')
    print(list1[1])

def delete():
    s = input('enter the username to delete: ')
    for d in list1:
        if d.get('name') == s :
            list1.remove(d)
    print(list1)

list1 = [{'name':'aadthiya','age':30,'salary':100000.0,'position':'regional maneger'},{'name':'gokul','age':20,'salary':20000000.0,'position':'chief excecutive officer'}]
list2 = []
# print(list1)
print("____x____X____x____")