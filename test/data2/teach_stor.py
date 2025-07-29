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
    print(list1)

def update():
    name = input('enter the name to be updated: ')
    for i in list1:
        if i['name'].lower() == name.lower():
            i['age'] = int(input('enter the student age : '))
            i['course'] = input('enter the students course: ')
            i['exam']['sem'] = int(input('enter the semester: '))
            i['exam']['sem']['subjects']['sub'] = input('enter the first subject: ')
            i['exam']['sem']['subjects']['marks'] = int(input('enter the first mark: '))
            i['exam']['sem']['subjects']['sub'] = input('enter the second subject: ')
            i['exam']['sem']['subjects']['marks'] = int(input('enter the second mark: '))
            i['exam']['sem']['subjects']['sub'] = input('enter the third subject: ')
            i['exam']['sem']['subjects']['marks'] = int(input('enter the third mark: '))
            i['exam']['sem']['subjects']['sub'] = input('enter the fourth subject: ')
            i['exam']['sem']['subjects']['marks'] = int(input('enter the fourth mark: '))
            i['exam']['sem']['subjects']['sub'] = input('enter the fifth subject: ')
            i['exam']['sem']['subjects']['marks'] = int(input('enter the fifth mark: '))

def search():
    print('aaaa')

def display():
    print('aaaa')

def delete():
    print('aaaa')


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
    }
]
