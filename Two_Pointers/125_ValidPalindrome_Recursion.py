import re
def isPalindrome(s): 
    s = ''.join(c for c in s if c.isalnum()).lower()
    if len(s) == 0 or len(s) == 1:
        return True
    
    if s[0] != s[-1]: 
        return False
    return isPalindrome(s[1:-1])

print(isPalindrome("Thiht!"))
