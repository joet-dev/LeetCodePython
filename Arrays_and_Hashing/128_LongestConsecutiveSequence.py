def longestConsecutive(nums): 
    nums.sort()

    max = 1
    count = 1
    prev = nums[0] 
    for val in nums[1:]: 
        if val == prev: 
            continue
        if val == prev + 1:
            count += 1
        else: 
            if count > max: 
                max = count
            count = 1
        prev = val
    
    if count > max:
        max = count 
    return max

print(longestConsecutive([1,2,0,1]))