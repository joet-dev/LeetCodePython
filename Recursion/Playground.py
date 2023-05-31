def reverseString(input):
    if len(input) == 0: 
        return input
    
    return reverseString(input[1:]) + input[0]


def isPalindrome(input): 
    if len(input) == 0 or len(input) == 1: 
        return True
    
    if input[0] == input[len(input)-1]: 
        return isPalindrome(input[1:-1])
    
    return False


def decimalToBinary(num, res):
    print(num, res)
    if num == 0:
        return res 
    
    res = str(num % 2) + res
    return decimalToBinary(num // 2, res)


def binarySearch(nums, left, right, x): 
    
    if left > right: 
        return -1
    
    mid = (left+right)//2
    print(left, mid, right)
    
    if x == nums[mid]: 
        return mid
    
    if x < nums[mid]:
        return binarySearch(nums, left, mid-1, x)
    
    return binarySearch(nums, mid+1, right, x)


def mergeSort(nums, s, e):
    if s < e: 
        mid = (s + e) // 2
        mergeSort(nums, s, mid)
        mergeSort(nums, mid+1, e)
        merge(nums, s, e, mid)
        
        
def merge(nums, s, e, mid): 
    temp = [0] * (e-s+1)
    
    i = s
    j = mid + 1
    k = 0
    
    while i <= mid and j <= e:
        if nums[i] <= nums[j]:
            temp[k] = nums[i]
            i += 1
            k += 1
        else: 
            temp[k] = nums[j]
            j += 1
            k += 1

    while i <= mid: 
        temp[k] = nums[i]
        k += 1
        i += 1
    while j <= e: 
        temp[k] = nums[j] 
        k += 1
        j += 1
        
    for i in range(s, e-1):
        nums[i] = temp[i-s]


