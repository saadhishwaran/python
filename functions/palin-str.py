a = input("Enter a word: ")

s = a.lower()  
length = len(s)
is_palin = True

for i in range(length // 2):
    if s[i] != s[length - 1 - i]:
        is_palin = False
        break  

if is_palin:
    print(f'{a} is a palindrome.')
else:
    print(f'{a} is not a palindrome.')
