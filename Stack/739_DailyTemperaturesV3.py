def dailyTemperatures(temperatures):
    """
    :type temperatures: List[int]
    :rtype: List[int]
    """
    n = len(temperatures)
    max = 0
    answer = [0] * n

    # iterate backwards
    # (day=n-1, day>=0, day--)
    for curr_day in range(n-1, -1, -1):
        curr_temp = temperatures[curr_day]

        #is day hottest so far?
        if curr_temp >= max:
            max = curr_temp
            continue

        days = 1 #else, next warmest must be >= day+1

        # iterate until hotter temp found
        while temperatures[curr_day + days] <= curr_temp:
            days += answer[curr_day + days]
        
        answer[curr_day] = days

    return answer

print(dailyTemperatures([73,74,75,71,69,72,76,73]))