import math
def carFleet(target, position, speed): 
    """
    :type target: int
    :type position: List[int]
    :type speed: List[int]
    :rtype: int
    """
    pair = [[p,s] for p, s in zip(position, speed)] 
    
    stack = []
    for p, s in sorted(pair)[::-1]:
        stack.append((target - p) /s)
        if len(stack) >= 2 and stack[-1] <= stack[-2]: 
            stack.pop()
    return len(stack)
        
        
        
print(carFleet(10, [0,4,2], [2,1,3]))