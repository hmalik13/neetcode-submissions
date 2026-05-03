class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        freq = {}

        for r in range(len(s)):
            # update hashmap with current char
            freq[s[r]] = 1 + freq.get(s[r], 0)
            # calculate number of replacements needed
            while r - l + 1 - max(freq.values()) > k:
                # shrink window from left
                freq[s[l]] -= 1
                l += 1
            # compare current window length to current res
            res = max(res, r - l + 1)
        return res
