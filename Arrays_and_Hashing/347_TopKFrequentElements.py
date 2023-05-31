def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    if len(nums) == 1: 
        return nums
    
    numsDict = {}
    for i in range(len(nums)): 
        numsDict[nums[i]] = numsDict.get(nums[i], 0) + 1

    sortedDict = sorted(numsDict.items(), key=lambda x:x[1])
    
    result = []
    for i in range(-k, 0, 1): 
        result.append(sortedDict[i][0])

    return result

print(topKFrequent([1, 1, 1, 2, 2, 3], 2))