def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    print(set(max([s,t], key=len)))
    for i in set(max([s, t], key=len)):
        if t.count(i) != s.count(i):
            return False
    return True

print(isAnagram("anagram", "nagaram"))