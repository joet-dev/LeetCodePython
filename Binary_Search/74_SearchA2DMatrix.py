def searchMatrix(matrix, target): 
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    for row in matrix: 
        s, e = 0, len(row)-1
        
        if row[e] >= target: 
            while s <= e:
                c = (s+e)//2 
                if row[c] < target: 
                    s = c+1
                elif row[c] > target: 
                    e = c-1
                else: 
                    return True
                
            return False
            
    return False
        
        
    
    
    
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 4))