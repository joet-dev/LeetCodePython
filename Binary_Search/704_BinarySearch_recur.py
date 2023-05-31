def search(nums, target): 
    l = len(nums)
    print(nums)
    
    def find(s, e): 
        print(s, e)
        if e - s < 2: 
            if nums[s] == target:
                return s
            if nums[e] == target: 
                return e
            return -1
            
        c = s + ((e-s) // 2)
        print(s, c, e)
        if nums[c] < target: 
            return find(c+1, e)
        elif nums[c] > target: 
            return find(s, c-1)
        else: 
            return c
    
    return find(0, len(nums)-1)

print(search([2, 5], 0))