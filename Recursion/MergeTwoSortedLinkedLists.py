class ListNode: 
    def __init__(self, value, node=None): 
        self.v = value
        self.next = node
    
    def addNode(self, node):
        self.next = node
        

def merge(hOne, hTwo): 
    if hOne == None: 
        return hTwo
    if hTwo == None: 
        return hOne

    if hOne.v < hTwo.v: 
        hOne.next = merge(hOne.next, hTwo)
        return hOne
    else: 
        hTwo.next = merge(hOne, hTwo.next)
        return hTwo
    
n6 = ListNode(6)
n4 = ListNode(4, n6)
n2 = ListNode(2, n4)   

n5 = ListNode(5)
n3 = ListNode(3, n5) 
n1 = ListNode(1, n3)  

p = merge(n1, n2)

while p != None: 
    print(p.v)
    p = p.next


    
    
