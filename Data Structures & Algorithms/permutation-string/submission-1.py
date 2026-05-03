class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        chars = {}
        window = {}
        for c in s1:
            chars[c] = 1 + chars.get(c, 0)
        
        for r in range(len(s2)):
            # if window exceeds length of s1
            # shrink from the left
            if r - l + 1 > len(s1):
                window[s2[l]] = window.get(s2[l]) - 1
                if window[s2[l]] == 0:
                    del window[s2[l]]
                l += 1
            # add to window from right
            window[s2[r]] = 1 + window.get(s2[r], 0)
            if window == chars:
                return True
        return False
