import eemploye

print("to update the details enter:'create'")
print("to push the value enter:'update'")
print("to search the particular element:'search'")
print("to get all the values:'display'")
print("to delete the values enter: 'delete'")

op = input("enter any one of the given operation: ").strip().lower()

if op == 'create':
    eemploye.create()
elif op == 'update':
    eemploye.update()
elif op == 'search':
    eemploye.search()
elif op == 'display':
    eemploye.display()
elif op == 'delete':
    eemploye.delete()
else:
    print('invalid operator given:')
