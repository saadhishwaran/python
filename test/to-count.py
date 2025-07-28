import string

def count(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

a = input('enter a string: ')
print("Number of vowels:", count(a))
