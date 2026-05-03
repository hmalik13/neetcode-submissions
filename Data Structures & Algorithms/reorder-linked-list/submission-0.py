# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle of the list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # second is head of second half
        second = slow.next

        # reverse second half of the list
        prev = None
        # point first node to null so it becomes tail
        slow.next = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        # merge the lists
        first = head
        # prev now points to first node of second list
        second = prev
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2