class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        res = 1
        l = 0
        chars = set()

        for r in range(len(s)):
            while s[r] in chars:
                # shrink from the left
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            length = r - l + 1
            res = max(res, length)
        return res
