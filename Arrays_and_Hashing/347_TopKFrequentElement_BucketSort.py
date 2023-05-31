def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    count = {}
    freq = [[] for i in range(len(nums) + 1)]
    
    for n in nums: 
        count[n] = 1 + count.get(n, 0)
    
    for n, c in count.items(): 
        freq[c].append(n)

    result = [] 
    for i in range(len(freq) - 1, 0, -1): 
        for n in freq[i]: 
            result.append(n) 
            if len(result) == k: 
                return result 

print(topKFrequent([1, 1, 1, 2, 2, 3], 2))