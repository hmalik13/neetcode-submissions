class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # treat the value of the array element
        # as the linked list "next" pointer
        # and the index as the node value
        fast = 0
        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # the duplicate will be at the start of the cycle
        # so use floyd's algorithm 
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                # slow is the value of the duplicate number
                return slow

