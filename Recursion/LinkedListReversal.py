class ListNode: 
    def __init__(self, value, node=None): 
        self.v = value
        self.next = node
    
    def addNode(self, node):
        self.next = node
        

def reverseList(head): 
    if head == None or head.next == None: 
        return head
    
    p = reverseList(head.next)
    head.next.next = head
    head.next = None
    return p

n6 = ListNode(6)
n5 = ListNode(5, n6)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)       
n2 = ListNode(2, n3)       
n1 = ListNode(1, n2)
node = reverseList(n1)

while node != None: 
    print(node.v)
    node = node.next