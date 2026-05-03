class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # initialize l and r to index 1
        l = 1
        for r in range(1, len(nums)):
            # compare current value to previous
            if nums[r] != nums[r-1]:
                # assign new value to location of l
                nums[l] = nums[r]
                l += 1
        return l
                



            

