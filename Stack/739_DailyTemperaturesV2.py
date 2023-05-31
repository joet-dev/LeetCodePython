def dailyTemperatures(temp):
    """
    :type temperatures: List[int]
    :rtype: List[int]
    """
    ans = [0] * len(temp)
    stack = []

    for i, t in enumerate(temp):

        while stack and stack[-1][0] < t: 
            sTemp, sIdx = stack.pop()
            ans[sIdx] = i - sIdx
        stack.append([t, i])
        
    return ans
        
print(dailyTemperatures([73,74,75,71,69,72,76,73]))