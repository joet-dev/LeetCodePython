def search(nums, target): 
    
    s, e = 0, len(nums)-1
    
    while s < e: 
        c = (e+s)//2
        if target > nums[c]: 
            s = c+1
        elif target < nums[c]: 
            e = c-1
        else: 
            return c
    return -1
    
    
print(search([-1,0,3,5,9,12], 9))
