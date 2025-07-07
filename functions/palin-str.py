def is_palindrome(s):
    s = s.lower()  
    length = len(s)
    
    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
            return False
    return True

a = input("Enter a word: ")

if is_palindrome(a):
    print(f'{a} is Palindrome')
else:
    print(f'{a} is not a palindrome')
