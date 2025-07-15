def create(): 
    n = int(input('enter the no: '))
    for i in range(n):
        name = input('enter the name: ')
        expirence = int(input('enter the expirence: '))
        salary = float(input('enter eemploye salary: '))
        postition = input('enter eemploye position: ')
        age = int(input('enter the age: '))
        father = input('enter father name: ')
        mother = input('enter mother name: ')
        mariage = input('enter yes if mariaged, no if not:')
        city = input('enter the cty: ')
        list1.append({'name':name,'expirence':expirence,'salary':salary,'position':postition,'perso-info':{'age':age,'father':father,'mother':mother,'mariage-stat':mariage,'city':city}})
    print(list1)



def update():
    list1.clear()
    n = int(input('enter the no: '))
    for i in range(n):
        name = input('enter the name: ')
        expirence = int(input('enter the expirence: '))
        salary = float(input('enter eemploye salary: '))
        postition = input('enter eemploye position: ')
        age = int(input('enter the age: '))
        father = input('enter father name: ')
        mother = input('enter mother name: ')
        mariage = input('enter yes if mariaged, no if not:')
        city = input('enter the cty: ')
        list1.append({'name':name,'expirence':expirence,'salary':salary,'position':postition,'perso-info':{'age':age,'father':father,'mother':mother,'mariage-stat':mariage,'city':city}})
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

list1 = [{'name':'jhon','expirence':3,'salary':1000,'position':'typewriter','perso_info':{'age':30,'father':'lim','mother':'ken','mariage_stat':'no','city':'washington'}},{'name':'jhony','expirence':4,'salary':3000,'position':'clearck','perso_info':{'age':31,'father':'liam','mother':'rose','mariage_stat':'yes','city':'newrorck'}}]
print(list1)