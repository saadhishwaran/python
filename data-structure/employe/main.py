import employe

print("to update the details enter:'create'")
print("to push the value enter:'update'")
print("to search the particular element:'search'")
print("to get all the values:'display'")

op = input("enter any one of the given operation: ").strip().lower()

if op == 'create':
    employe.create()
elif op == 'update':
    employe.update()
elif op == 'search':
    employe.search()
elif op == 'display':
    employe.display()
else:
    print('invalid operator given:')
