# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        slow,fast = head,head.next
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
        second= slow.next
        slow.next=None
        prev=None
        
        while second:
            temp=second.next
            second.next=prev
            prev=second
            second=temp
        
        
        second=prev
        first=head
        while second and first:
            temp=first.next
            first.next=second
            temp2=second.next
            second.next=temp
            first=temp
            second=temp2
            
        