def is_palindrome(string):
    if string.lower == string[::-1].lower:
        return 'YES'
    else:
        return 'NO'


string = input()

print(is_palindrome(string))
