import employe

print("to update the details enter:'update'")
print("to push the value enter:'creat'")
print("to search the particular element:'search'")
print("to get all the values:'display'")

op = input("enter any one of the given operation: ").lower()

if op == 'update':
    employe.update()
elif op == 'creat':
    employe.creat()
elif op == 'search':
    employe.search()
elif op == 'display':
    employe.display()
else:
    print('invalid operator given:')
