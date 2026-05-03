# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # point right to the nth node in the list
        while n > 0 and right:
            right = right.next
            n -= 1
        
        # now left and right are n nodes apart
        while right:
            left = left.next
            right = right.next
        
        # now right is at null and left is at node
        # before the node we want to delete
        left.next = left.next.next
        return dummy.next