import math

def is_palindrome(word):
    j = len(word)-1
    result = 0
    for i in range(len(word)):
        if word[i] == word[j]:
            result = result +1
        if i >= j:
            break
        j = j - 1

    if result == math.ceil(len(word)/2):
        return True