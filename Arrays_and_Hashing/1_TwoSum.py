def twoSum(nums, target): 
    hashSet = {} 

    for i, val in enumerate(nums): 
        if val in hashSet: 
            return [hashSet[val], i]
        else: 
            hashSet[target-val] = i



print(twoSum([2,7,11,15], 9))