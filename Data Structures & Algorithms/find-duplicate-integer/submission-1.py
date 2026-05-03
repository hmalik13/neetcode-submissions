class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # use floyd's algorithm
        # treat array elements as pointers
        # and indices as nodes in linked list
        slow = 0
        fast = 0
        # first pass
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        # second pass
        # start of cycle will be the node with the duplicate
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
