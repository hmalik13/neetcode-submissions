class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0) 
        return max(count, key=count.get)