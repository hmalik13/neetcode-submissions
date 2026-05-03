class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # initialize output array
        result = [1] * (len(nums))
        # prefix = product of all values to the left
        # populate output with prefix values
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        # postfix = product of all values to the right
        # populate output with postfix values
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result