class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")": "(",
                    "]": "[",
                    "}": "{"}
        stack = []
        for c in s:
            # if it's a closing bracket, check top of stack
            # if top is matching bracket, pop and continue
            if c in brackets:
                if stack and stack[-1] == brackets[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
        



