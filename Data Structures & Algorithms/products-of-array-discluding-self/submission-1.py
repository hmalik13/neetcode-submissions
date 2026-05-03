class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        # populate result with prefix products
        # from left to right
        prefix = 1
        for i in range(len(nums)): 
            result[i] = prefix
            prefix *= nums[i]

        # multiply each element in result with postfix 
        # product from right to left
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        return result


            