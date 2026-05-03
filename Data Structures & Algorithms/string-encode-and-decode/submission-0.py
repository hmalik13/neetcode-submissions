class Solution:
    # given list of strings, convert to one string
    def encode(self, strs: List[str]) -> str:
        result = ""
        # append length of string and # delimiter 
        # to beginning of each string
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    # given string, convert to list of strings
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
# 5#hello
# ij
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            # get length of string
            length = int(s[i:j])
            # index of start of string
            i = j + 1
            # index of end of string
            j = i + length
            # add string to list
            result.append(s[i:j])
            i = j
        return result


