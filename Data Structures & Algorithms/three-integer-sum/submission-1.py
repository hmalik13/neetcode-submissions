class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i, a in enumerate(nums):
            # skip duplicates
            if i > 0 and a == nums[i-1]:
                continue
            # set up left and right pointers
            l = i + 1
            r = len(nums) - 1
            # use two sum algorithm
            while l < r: 
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    result.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # skip duplicates
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return result


        