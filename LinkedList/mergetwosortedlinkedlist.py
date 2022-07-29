# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
       
        #This is the a node for a singly-linked list, which is capable of holding an type of Object. A ListNode consists of two data members: The data we are keeping track of at this node (Object) The next ListNode in the chain.
        dummy=ListNode()
        ##Will intially refer to zero 
        tail=dummy
        while l1 and l2:
            if l1.val< l2.val:
                tail.next=l1
                l1=l1.next
            else:
                tail.next=l2
                l2=l2.next
            tail=tail.next
            
        if l1:
            tail.next=l1
        elif l2:
            tail.next=l2
        
        return dummy.next