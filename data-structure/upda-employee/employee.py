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
    s = input('enter what are you going to use to search: ')
    r = []
    if s == 'name':
        a = input('enter the empolyee name: ')
        for d in list1: 
            if d.get('name') == a:
                r.append(d)
        else:
            print('not found;')
    if s == 'position':
        a = input('enter the empolyee position: ')
        for d in list1:
            if d.get('position') == a:
                r.append(d)
        else:
            print('not found;')
    if s == 'age':
        z = input('enter yes if range,and no if not: ')
        if z == 'yes':
            a = int(input('enter the min age range:'))
            b = int(input('enter the max age range: '))
            for d in list1:
                if d['perso_info']['age'] > a:
                    if d['perso_info']['age'] < b:
                        r.append(d)
            else:
                print('not found;')
        else: 
            a = int(input('enter the age: '))       
            for d in list1:
                if d['perso_info']['age'] == a:
                    r.append(d)
            else:
                print('not found;')
    if s == 'experience':
        z = input('enter yes if range,and no if not: ')
        if z == 'yes':
            a = int(input('enter the min experience: '))
            b = int(input('enter the max experience: '))
            for d in list1:
                if d['experience'] > a:
                    if d['experience'] < b:
                        r.append(d)
            else:
                print('not found;')
        else:
            a = int(input('enter the experience: '))
            for f in list1:
                if f['experience'] == a:
                    r.append(f)
            else: 
                print('not found;')
    if s == 'salary':
        z = input('enter yes if range,and no if not: ')
        if z == 'yes':
            a = float(input('enter the min salary: '))
            b = float(input('enter the max salary: '))
            for d in list1:
                if d['salary'] > a:
                    if d['salary'] < b:
                        r.append(d)
            else:
                print('not found;')
        else:
            q = float(input('enter the salary: '))
            for d in list1:
                if d.get('salary') == q:
                    r.append(d)
            else:
                print('not found;')
    print(r)

def display():
    for i in list1:
        print('name:',i['name'])
        print('experience:',i['experience'])
        print('salary:',i['salary'])
        print('position:',i['position'])
        print('personal information>>age:',i['perso_info']['age'])
        print('personal information>>father_name: ',i['perso_info']['father'])
        print('presonal information>>mother_name: ',i['perso_info']['mother'])
        print('presonal information>>city: ',i['perso_info']['city'])
        print('___x___X___x___')

def delete():
    s = input('enter the username to delete: ')
    for d in list1:
        if d.get('name') == s :
            list1.remove(d)
    print(list1)

list1 = [{'name':'jhon','experience':3,'salary':1000,'position':'typewriter','perso_info':{'age':30,'father':'lim','mother':'ken','marsiage_stat':'no','city':'washington'}},{'name':'jhony','experience':4,'salary':3000,'position':'clearck','perso_info':{'age':31,'father':'liam','mother':'rose','marriage_stat':'yes','city':'newrorck'}}]
print(list1)