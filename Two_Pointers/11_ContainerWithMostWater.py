def maxArea(height): 
    """
    :type height: List[int]
    :rtype: int
    """
    max = 0 
    maxs = 0
    maxe = 0
    
    s, e = 0, len(height)-1

    while s < e:
        if height[s] < maxs: 
            s += 1 
            continue
        else: 
            maxs = height[s] 
        if height[e] < maxe: 
            e -= 1
            continue
        else: 
            maxe = height[e] 
   
        vol = (e-s) * min(height[s], height[e])
        
        if vol > max: 
            max = vol
            
        if height[s] > height[e]: 
            e -= 1
        else: 
            s += 1
             
    return max 
    
print(maxArea([1,2,4,3]))