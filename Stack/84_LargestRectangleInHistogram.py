def largestRectangleArea(heights): 
    stackH = [] 
    stackP = [] 
    max = 0
    
    for i, h in enumerate(heights): 
        minPos = i
        while stackH and stackH[-1] > h: 
            calc = stackH[-1] * (i - stackP[-1])
            if calc > max: 
                max = calc
                
            stackH.pop()
            minPos = stackP.pop()
            
        stackH.append(h)  
        stackP.append(minPos)
        
        
    for i in range(len(stackH)): 
        calc = stackH.pop()*(len(heights) - stackP.pop()) 
        if calc > max: 
            max = calc
            
    return max


print(largestRectangleArea([2, 1, 5, 6, 2, 3]) )