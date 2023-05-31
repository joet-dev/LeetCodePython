def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    answer = [1] * len(nums) 

    # answer[i] == product of all nums except nums[i]. 

    pre = 1
    for i in range(len(nums)): 
        answer[i] = pre
        pre *= nums[i] 

    
    post = 1
    for i in range(len(nums) -1, -1, -1): 
        answer[i] *= post
        post *= nums[i]
  
    return answer
    

print(productExceptSelf([1,2,3,4]))