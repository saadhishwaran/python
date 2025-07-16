def create(): 
    n = int(input('enter the no: '))
    for i in range(n):
        name = input('enter the name: ')
        experience = int(input('enter the expirence: '))
        salary = float(input('enter eemploye salary: '))
        postition = input('enter eemploye position: ')
        age = int(input('enter the age: '))
        father = input('enter father name: ')
        mother = input('enter mother name: ')
        marriage = input('enter yes if marriaged, no if not:')
        city = input('enter the cty: ')
        list1.append({'name':name,'experience':experience,'salary':salary,'position':postition,'perso-info':{'age':age,'father':father,'mother':mother,'marriage-stat':marriage,'city':city}})
    print(list1)

def update():
    name = input('enter the name to be updated: ')
    for i in list1:
        if i['name'].lower() == name.lower():
            i['experience'] = int(input('enter the new experience: '))
            i['salary'] = float(input('enter the salary: '))
            i['position'] = input('enter the position: ')
            i['perso_info']['age'] = int(input('enter the age: '))
            i['perso_info']['fatner'] = input('enter the father name: ')
            i['perso_info']['mother'] = input('enter the mother name: ')
            i['perso_info']['marriage-stat'] = input('enter marriage status')
            i['perso_info']['city'] = input('enter the home city: ')
    else:
        print('employee deatils must be created')        
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

list1 = [{'name':'jhon','experience':3,'salary':1000,'position':'typewriter','perso_info':{'age':30,'father':'lim','mother':'ken','marsiage_stat':'no','city':'washington'}},{'name':'jhony','experience':4,'salary':3000,'position':'clearck','perso_info':{'age':31,'father':'liam','mother':'rose','marriage_stat':'yes','city':'newrorck'}}]
print(list1)