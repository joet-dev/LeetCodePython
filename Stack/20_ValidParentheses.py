def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    
    hashMap = {"]": "[", "}": "{" , ")": "("}
    stack = []
    for char in s: 
        if char in hashMap.values(): 
            stack.append(char)
        elif len(stack) == 0:
            return False
        else: 
            if stack.pop() != hashMap[char]:
                return False
        
    return len(stack) == 0
            

print(isValid("]"))