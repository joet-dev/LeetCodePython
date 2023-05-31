def maxProfit(prices): 
    """
    :type prices: List[int]
    :rtype: int
    """
    profit = 0
    low = prices[0]
    
    for p in prices: 
        if p < low:
            low = p 
        elif p - low > profit: 
            profit = p - low
        
    return profit
    
            
            
    
print(maxProfit([7,1,5,3,6,4]))