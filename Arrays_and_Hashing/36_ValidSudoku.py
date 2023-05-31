import collections

def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
   
    cols = collections.defaultdict(set)
    boxes = collections.defaultdict(set)

    for y in range(len(board)):
        row = set() 
        for x, val in enumerate(board[y]): 
            if val == ".": 
                continue
        
            # check row
            if (val in row or val in cols[x] or val in boxes[(y//3, x//3)]):  
                return False
            
            row.add(val)
            cols[x].add(val)
            boxes[(y//3, x//3)].add(val)
            
    return True

isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])