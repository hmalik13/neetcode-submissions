class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        window = {}
        maxFreq = 0

        for r in range(len(s)):
            # num replacements = length of window - frequency of most frequent character
            window[s[r]] = 1 + window.get(s[r], 0)
            if window[s[r]] > maxFreq:
                maxFreq = window[s[r]]
            replacements = (r - l + 1) - maxFreq
            if replacements > k:
                window[s[l]] = window.get(s[l]) - 1
                l += 1
            length = r - l + 1
            res = max(res, length)
        return res