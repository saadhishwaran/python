def creat():
    a = input('enter the students name: ')
    b = int(input('enter the student age : '))
    c = input('enter the students course: ')
    d = int(input('enter the semester: '))
    e1 = input('enter the first subject: ')
    f1 = int(input('enter the first mark: '))
    e2 = input('enter the sceond subject: ')
    f2 = int(input('enter the first mark: '))
    e3 = input('enter the third subject: ')
    f3 = int(input('enter the first mark: '))
    e4 = input('enter the fourth subject: ')
    f4 = int(input('enter the first mark: '))
    e5 = input('enter the fifth subject: ')
    f5 = int(input('enter the first mark: '))
    list1.append(
        {
            'name':a,
            'age':b,
            'course':c,
            'exam':[
                {
                    'sem':d,
                    'subjects':[
                        {'sub':e1,'marks':f1},
                        {'sub':e2,'marks':f2},
                        {'sub':e3,'marks':f3},
                        {'sub':e4,'marks':f4},
                        {'sub':e5,'marks':f5}
                     ]
                }
            ]
        }
    )
    print(display())

def update():
    name = input('enter the name to be updated: ')
    for i in list1:
        if i['name'].lower() == name.lower():
            i['age'] = int(input('enter the student age: '))
            i['course'] = input("enter the student's course: ")
            seme = int(input('enter the semester => 1 or 2 or 3:  ')) - 1
            if  seme < len(i['exam']):
                subj = i['exam'][seme]['subjects']
                for j in range(len(subj)):
                    sub = input('enter the sub: ')
                    marks = int(input('enter the marks: '))
                    if j < len(subj):
                        subj[j] = {'sub': sub, 'marks': marks}
                    else:
                        subj.append({'sub': sub, 'marks': marks})
            elif 8 > seme == len(i['exam']):
                n = int(input('enter the no of semester to add: '))
                for ij in range(n):
                    list2 = []
                    subj = i['exam'][0]['subjects']  
                    for j in range(len(subj)):
                        sub = input('Enter the subject: ')
                        marks = int(input('Enter the marks: '))
                        list2.append({'sub': sub, 'marks': marks})
                    i['exam'].append({'sem': seme + ij + 1, 'subjects': list2})
            print(display())
    else:
        print('student not found: ')
 
def search():
    list2 =[]
    variable = input('enter on what to search: ')
    if variable == 'name':
        name = input('enter the name to search: ')
        for i in list1: 
            if i['name'] == name:
                list2.append(i)
                print(display())
            else:
                print('not found: ')
    elif variable == 'age':
        age = int(input('enter the age to be found: '))
        for i in list1:
            if i['age'] == age:
                list2.append(i)
                print(display()) 
            else:
                print('not found: ')
    elif variable == 'course':
        course = input('enter the course to search: ')
        for i in list1:
            if i['course'] == course:
                list2.append(i)
                print(display())
            else:
                print('not found: ')
    else:
        print('invalid cerdinals; ')

def display():
    for i in list1:
        print('name:',i['name'])
        print('age:',i['age'])
        print('course:',i['course'])
        for j in i['exam']:
            print('sem:',j['sem'])
            for k in j['subjects']:
                print('subject:',k['sub'],'marks:',k['marks'])

def delete():
    name = input('enter the student to be removed: ')
    for i in list1:
        if i.get('name') == name.lower():
            list1.remove(i)
    print(display())


list1 = [
    {
        'name':'aadhi',
        'age':19,
        'course':'eee',
        'exam': 
        [
            {
                'sem': 1 , 
                'subjects': 
                [
                    {'sub':'eng', 'marks': 88},
                    {'sub':'tam', 'marks': 89},
                    {'sub':'phys','marks':87},
                    {'sub':'maths','marks':86},
                    {'sub':'computer','marks':85}
                ],
            },
            {
                'sem': 2 , 
                'subjects':
                [
                    {'sub':'eng', 'marks': 98},
                    {'sub':'tam', 'marks': 99},
                    {'sub':'phys','marks':97},
                    {'sub':'maths','marks':96},
                    {'sub':'computer','marks':95}
                ],
            },
            {
                'sem': 3 ,
                'subjects': 
                [
                    {'sub':'eng', 'marks': 100},
                    {'sub':'tam', 'marks': 99},
                    {'sub':'phys','marks':98},
                    {'sub':'maths','marks':96},
                    {'sub':'computer','marks':97}
                ]
            }
        ]
    },
    {
        'name':'aadhish',
        'age':20,
        'course':'ece',
        'exam': 
        [
            {
                'sem': 1 , 
                'subjects': 
                [
                    {'sub':'eng', 'marks': 98},
                    {'sub':'tam', 'marks': 99},
                    {'sub':'phys','marks':89},
                    {'sub':'maths','marks':96},
                    {'sub':'computer','marks':95}
                ],
            },
            {
                'sem': 2 , 
                'subjects':
                [
                    {'sub':'eng', 'marks': 88},
                    {'sub':'tam', 'marks': 89},
                    {'sub':'phys','marks':98},
                    {'sub':'maths','marks':86},
                    {'sub':'computer','marks':85}
                ],
            },
            {
                'sem': 3 ,
                'subjects': 
                [
                    {'sub':'eng', 'marks': 90},
                    {'sub':'tam', 'marks': 89},
                    {'sub':'phys','marks':99},
                    {'sub':'maths','marks':97},
                    {'sub':'computer','marks':87}
                ]
            }
        ]
    }
]
