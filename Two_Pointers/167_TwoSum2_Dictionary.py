def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    numdic = {} 

    for i, num in enumerate(numbers):
        
        if numdic.get(num) != None:  
            return [numdic[num], i+1]
        numdic[target-num] = i + 1
    
print(twoSum([2, 7, 11, 15], 9))  
    