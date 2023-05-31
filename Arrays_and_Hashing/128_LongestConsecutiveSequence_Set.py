def longestConsecutive(nums): 
    numSet = set(nums)
    large = 0

    for val in nums: 
        if (val-1) not in numSet: 
            len = 0
            while (val + len) in numSet: 
                len += 1
            large = max(len, large)

    return large

    

print(longestConsecutive([1,2,0,1]))