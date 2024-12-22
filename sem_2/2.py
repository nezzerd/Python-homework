def is_palindrome(s):
    return s == s[::-1]


def is_almost_palindrome(s):
    letters = [char for char in s if char.isalpha()]
    if is_palindrome(letters):
        print("YES")
        return
    for i in range(len(letters)):
        modified = letters[:i] + letters[i + 1:]
        if is_palindrome(modified):
            print("YES")
            return

    print("NO")


input_string = input()
is_almost_palindrome(input_string)
