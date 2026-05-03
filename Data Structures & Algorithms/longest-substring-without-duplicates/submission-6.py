class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        res = 0
        l = 0

        for r in range(len(s)):
            # first check if window is valid
            while s[r] in window:
                # shrink window from the left
                window.remove(s[l])
                l += 1
            # expand window from the right
            window.add(s[r])
            # get window length
            length = r - l + 1
            res = max(length, res)
        return res