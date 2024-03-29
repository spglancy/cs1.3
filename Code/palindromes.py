#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# chars is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# chars is ascii_lowercase + ascii_uppercase
chars = list(string.ascii_letters)


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_iterative(text)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests
    if len(text) < 1:
        return True
    left = 0
    right = len(text)-1
    passing = True
    text = text.lower()
    while passing:
        while text[left] not in chars:
            left += 1
            if left >= right:
                return True
        while text[right] not in chars:
            right -= 1
            if right <= left:
                return True
        if left >= right:
            return True
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1

def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests
    if len(text) < 1:
        return True
    if left == None:
        left = 0
        right = len(text)-1
    while text[left] not in chars:
        left += 1
        if left >= right:
            return True
    while text[right] not in chars:
        right -= 1
        if right <= left:
            return True
    if left >= right:
        return True
    if text[left].lower() != text[right].lower():
        return False
    left += 1
    right -= 1
    return(is_palindrome_recursive(text, left, right))

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
