def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    mydic = {}

    if len(s) != len(t): 
        return False 
        
    for i in range(len(s)): 
        # mydic[s[i]] = mydic.get(s[i], 0) + 1
        if s[i] in mydic: 
            mydic[s[i]] += 1
        else: 
            mydic[s[i]] = 1
    
    for i in range(len(t)): 
        if t[i] not in mydic: 
            return False
        
        if t[i] in mydic: 
            if mydic[t[i]] == 0: 
                return False
            
            mydic[t[i]] -= 1
        
    return True

print(isAnagram("anagram", "nagaram"))