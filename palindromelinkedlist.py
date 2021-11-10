# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        len=0
        dummy=head
        while dummy:
            len +=1
            dummy=dummy.next
            
        mid=len // 2
        i=0
    
    
    
        def reverse(head):
            prev=None
            while head:
                temp=head
                head=head.next
                temp.next=prev
                prev=temp
            return prev    
    
        first=second=head
        while i< mid:
            second=second.next
            i +=1
    
    
    
        seond=reverse(second)
    
        while first and second:
            if first.val != second.val:
                return False
            else:
                first=first.next
                second=second.next
        return True