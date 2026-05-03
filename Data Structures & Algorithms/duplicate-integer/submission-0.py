class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_nums = []
        for number in nums:
            if number not in my_nums:
                my_nums.append(number)
            else:
                return True
        return False