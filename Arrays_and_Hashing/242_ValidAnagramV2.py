def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t): 
        return False
    if ''.join(sorted(s)) == ''.join(sorted(t)): 
        return True
    return False

print(isAnagram("anagram", "nagaram"))