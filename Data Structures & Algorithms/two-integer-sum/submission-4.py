class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # target - nums[i] = ans

        record = {}
        for i in range(len(nums)):
            ans = target - nums[i]
            if ans in record:
                return [record[ans], i]
            record[nums[i]] = i