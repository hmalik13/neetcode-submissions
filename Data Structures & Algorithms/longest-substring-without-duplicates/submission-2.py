class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l = 0
        maxLength = 1

        if not s:
            return 0

        for r in range(len(s)):
            # shrink window from left
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            length = (r - l) + 1
            maxLength = max(maxLength, length)
        return maxLength