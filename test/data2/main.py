import teach_stor

a = input("enter any one in the avilable option = 'create','update','search','display',delete': ")

if a == 'create':
    teach_stor.creat()
elif a == 'update':
    teach_stor.update()
elif a == 'search':
    teach_stor.search()
elif a == 'display':
    teach_stor.display()
elif a == 'delete':
    teach_stor.delete()
else:
    print('invalid operator given; ')