class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ")" : "(",
            "}" : "{",
            "]" : "[" 
            }
        stack = []
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            elif c == ")" or c == "}" or c == "]":
                if not stack or stack.pop() != brackets[c]:
                    return False
            else:
                return False
        if not stack:
            return True
        else:
            return False

            