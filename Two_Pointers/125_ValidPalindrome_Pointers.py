def isPalindrome(s): 
    """
    :type s: str
    :rtype: bool
    """
    s = ''.join(c for c in s if c.isalnum()).lower()
    b, e = 0, len(s)-1
    
    while b < e: 
        if s[b] != s[e]: 
            return False
        b += 1
        e -= 1
        
    return True

    

print(isPalindrome("race a car"))