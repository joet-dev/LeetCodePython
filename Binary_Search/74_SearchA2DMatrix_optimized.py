def searchMatrix(matrix, target): 
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    numR = len(matrix)
    numC = len(matrix[0])
    row = 0 
    col = numC - 1
    
    while row < numR and col >= 0: 
        if matrix[row][col] == target: 
            return True
        elif matrix[row][col] > target: 
            col -= 1
        else:
            row += 1
            
    return False
        
    
    
    
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 4))