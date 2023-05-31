import collections as c 

def threeSum(nums):
    
    nums.sort()
    ans = []
    
    for i, val in enumerate(nums): 
        if i > 0 and val == nums[i-1]: 
            continue
        
        s, e = i+1, len(nums)-1
        
        while s < e: 
            sumThree = val + nums[s] + nums[e] 
            if sumThree > 0: 
                e -= 1
            elif sumThree < 0: 
                s += 1
            else: 
                ans.append([val, nums[s], nums[e]])
                s += 1
                while nums[s] == nums[s-1] and s < e: 
                    s += 1
                    
    return ans
    
print(threeSum([-1,0,1,2,-1,-4]))

# print(threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))
