def palindrome(string, index):
    left = index
    right = len(string) - 1 - index
    if left >= right:
        return f"{string} is a palindrome"
    left_letter = string[index]
    right_letter = string[len(string) - 1 - index]

    if not left_letter == right_letter:
        return f"{string} is not a palindrome"
    return palindrome(string, index+1)



print(palindrome("abcba", 0))
print(palindrome("peter", 0))