def lengthOfLongestSubstring(s): 
    
    unique = set()
    l = 0 
    ans = 0
    
    for i in range(len(s)): 
        while s[i] in unique: 
            unique.remove(s[l])
            l += 1
            
        unique.add(s[i])
        ans = max(ans, i-l+1) 
    return ans
    
    
    
    
print(lengthOfLongestSubstring("pwwkew"))