def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    s, e = 0, len(numbers)-1
    while s < e: 
        twosum = numbers[s] + numbers[e] 
        
        if twosum == target: 
            return [s+1, e+1] 
        
        if twosum < target: 
            s += 1
        else: 
            e -= 1
    
    
print(twoSum([2, 7, 11, 15], 9))  