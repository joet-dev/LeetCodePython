def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    answer = [] 

    # answer[i] == product of all nums except nums[i]. 

    pre = [nums[0]] 
    post = [nums[len(nums)-1]]
    for i in range(1, len(nums)): 
        pre.append(nums[i] * pre[i-1])
        post.insert(0, nums[-i-1] * post[-i])

    for i in range(len(nums)): 
        if i == 0: 
            answer.append(post[i+1])
        elif i == len(nums)-1: 
            answer.append(pre[i-1]) 
        else: 
            answer.append(pre[i-1] * post[i+1])

    return answer

print(productExceptSelf([1,2,3,4]))