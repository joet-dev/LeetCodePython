def dailyTemperatures(temp):
    """
    :type temperatures: List[int]
    :rtype: List[int]
    """

    stack = [] 
    ans = [0] * len(temp)
    
    for i in range(len(temp) - 1): 
        # append all new temps to stack
        stack.insert(0, i)
        for idx in reversed(stack):
            ans[idx] += 1
            
            if temp[idx] < temp[i+1]:
            # if prev and current temps are smaller than future temp 
                stack.remove(idx)
            
    for idx in stack:
        ans[idx] = 0
        
    return ans

print(dailyTemperatures([73,74,75,71,69,76,3,80])) 