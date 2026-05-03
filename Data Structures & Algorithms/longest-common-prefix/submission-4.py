class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        strs.sort()
        first = strs[0]
        last = strs[len(strs) - 1]
        for i in range(len(min(first, last))):
            if first[i] != last[i]:
                return prefix
            prefix += first[i]
        return prefix


            


