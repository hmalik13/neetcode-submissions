class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      if not nums:
        return 0
      hashset = set(nums)
      longest = 1
      for n in nums:
        if n - 1 not in hashset:
            curLongest = 1
            while n + 1 in hashset:
                curLongest += 1
                n += 1
            longest = max(curLongest, longest)
      return longest
                 
      
    