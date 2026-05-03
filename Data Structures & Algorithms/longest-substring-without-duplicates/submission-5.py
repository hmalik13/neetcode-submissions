class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        res = 0
        l = 0
        for r in range(0, len(s)):
            # shrink from the left
            while s[r] in window:
                window.remove(s[l])
                l += 1
            # get length of current valid window
            length = r - l + 1
            res = max(res, length)
            # expand from right
            window.add(s[r])
        return res



            
                

