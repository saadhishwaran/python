def create(): 
    dict1 = {}
    n = int(input('enter the no: '))
    for i in range(n):
        name = input('enter the keys: ')
        age = int(input('enter the values'))
        salary = float(input('enter eemploye salary: '))
        postition = input('enter eemploye position: ')
        dict1.update({'name':name,'age':age,'salary':salary,'position':postition})
        list2.append(dict1)
    print(dict1)

def update():
    dict1 = {}
    n = int(input('enter the no: '))
    for i in range(n):
        name = input('enter the keys: ')
        age = int(input('enter the values'))
        salary = float(input('enter eemploye salary: '))
        postition = input('enter eemploye position: ')
        dict1.update({'name':name,'age':age,'salary':salary,'position':postition})
        list2.append(dict1)
    print(dict1)  
    
def search():
    s = input('enter the element to be found: ')
    r = []
    for d in List1:
        if d.get('name') == s :
            r.append(d)
    print(r)
    

def display():
    print(List1[0])
    print(List1[1])

List1 = [{'name':'aadthiya','age':30,'salary':100000.0,'position':'regional maneger'},{'name':'gokul','age':20,'salary':20000000.0,'position':'chief excecutive officer'}]
list2 = []
print(List1)
print("____x____X____x____")