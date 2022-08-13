def isCircular(head):
    # Code here
      if not head:
          return True
      if head.next == None:
          return False
      
      curr = head.next
      
      while curr:
          if curr == head:
              return True
          
          curr=curr.next
