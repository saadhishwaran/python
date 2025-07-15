import employee

print("to update the details enter:'create'")
print("to push the value enter:'update'")
print("to search the particular element:'search'")
print("to get all the values:'display'")
print("to delete the values enter: 'delete'")

op = input("enter any one of the given operation: ").strip().lower()

if op == 'create':
    employee.create()
elif op == 'update':
    employee.update()
elif op == 'search':
    employee.search()
elif op == 'display':
    employee.display()
elif op == 'delete':
    employee.delete()
else:
    print('invalid operator given:')
