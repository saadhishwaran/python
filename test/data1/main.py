import employee

a = input("select an option = 'create','deposit','withdraw'")

if a == 'create':
    employee.create()
elif a == 'deposit':
    employee.deposit()
elif a == 'withdraw':
    employee.withdraw()
else:
    print('Invalid option given; ')