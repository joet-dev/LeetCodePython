class MinStack(object):
    def __init__(self):
        self.s = []     
        self.min = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
              
        self.s.append(val)        
        if len(self.s) == 1: 
            self.min.append(len(self.s)-1)
        elif val < self.s[self.min[-1]]: 
            self.min.append(len(self.s)-1)
        else: 
            self.min.append(self.min[-1])
        print(self.min)

    def pop(self):
        """
        :rtype: None
        """
        if self.s: 
            del self.s[-1]
            del self.min[-1]

    def top(self):
        """
        :rtype: int
        """
        return self.s[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.s[self.min[-1]]

obj = MinStack()
obj.push(5)
obj.push(10)
obj.push(1)
obj.push(5)
obj.push(3)
print(obj)
obj.pop()
obj.pop()
obj.pop()
print(obj.top())
print(obj.getMin())