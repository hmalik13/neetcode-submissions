class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            # if we're in a sorted array
            if nums[l] < nums[r]:
                # compare leftmost value to current min
                res = min(nums[l], res)
                break

            mid = (l + r) // 2
            res = min(nums[mid], res)
            # if we're in the left subarray
            if nums[mid] >= nums[l]:
                # we want to search the right subarray
                l = mid + 1
            # if we're in the right subarray
            else:
                # we want to search the left subarray
                r = mid - 1
        return res

            