from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        count1 = Counter(s1) # freq of each char in s1
        window = Counter(s2[:n]) # freq of first window in s2

        if count1 == window:
            return True

        # we already checked first window, so start at next one
        for i in range(n, m):
            # update freq after adding char from right
            window[s2[i]] += 1
            # update freq after removing char from left
            window[s2[i - n]] -= 1
            # remove char from freq count if == 0
            if window[s2[i - n]] == 0:
                del(window[s2[i - n]])
            # check if window is anagram of s1
            if count1 == window:
                return True
        return False

        
