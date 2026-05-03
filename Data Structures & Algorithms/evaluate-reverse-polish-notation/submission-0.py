class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            match t:
                case "+":
                    stack.append(stack.pop() + stack.pop())
                case "-":
                    x = stack.pop()
                    y = stack.pop()
                    stack.append(y - x)
                case "*":
                    stack.append(stack.pop() * stack.pop())
                case "/":
                    x = stack.pop()
                    y = stack.pop()
                    stack.append(int(y / x))
                case _:
                    stack.append(int(t))
        return stack[0]
