class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      if not nums:
        return 0
      longest = 1
      hashset = set(nums)
      for i in range(len(nums)):
        nextNum = nums[i] + 1
        curLongest = 1
        while nextNum in hashset:
            curLongest += 1
            nextNum += 1
        longest = max(longest, curLongest)
      return longest
    