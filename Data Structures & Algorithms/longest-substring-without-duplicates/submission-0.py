class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        maxLength = 0

        for r in range(len(s)):
            # while there are duplicates
            while s[r] in charSet:
                # shorten sliding window from the left
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            maxLength = max(maxLength, len(charSet))
        
        return maxLength