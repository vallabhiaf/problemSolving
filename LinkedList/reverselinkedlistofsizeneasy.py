# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
          return None
        current = head
        next = None
        prev = None
        count = 0
  
        # Reverse first k nodes of the linked list
        while(current  and count < k):
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1
  
        # next is now a pointer to (k+1)th node
        # recursively call for the list starting
        # from current. And make rest of the list as
        # next of first node
        if next is not None:
            head.next = self.reverseKGroup(next, k)
  
        # prev is new head of the input list
        return prev