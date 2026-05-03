class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create empty hash set
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            else:
                # add to hashset
                hashset.add(n)
        return False
