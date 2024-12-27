class SinglyNode:

    def __init__(self,val,next=None):
        self.val = val
        self.next = next 

    def __str__(self):
        return str(self.val)
    
Head = SinglyNode(1)
A = SinglyNode(4)
B = SinglyNode(3)
C = SinglyNode(7)

Head.next = A
A.next = B
B.next = C

print(Head.next.next.next.next)