def generateParenthesis(n): 
    stack = [] 
    ans = [] 

    def backtrack(oNum, cNum): 
        print(oNum, cNum, stack)
        if oNum == cNum == n: 
            ans.append("".join(stack))

        if oNum < n: 
            stack.append("(")
            backtrack(oNum + 1, cNum) 
            stack.pop()
        
        if cNum < oNum: 
            stack.append(")") 
            backtrack(oNum, cNum + 1)
            stack.pop()
        
    backtrack(0, 0) 
    return ans

print(generateParenthesis(3))
