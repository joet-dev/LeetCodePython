def containsDuplicate(nums): 
    return len(set(nums)) != len(nums)

print(containsDuplicate([1, 1, 2, 3]))