class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            match t:
                case "+":
                    ans = stack.pop() + stack.pop()
                    stack.append(ans)
                case "-":
                    second = stack.pop()
                    first = stack.pop()
                    stack.append(first - second)
                case "*":
                    ans = stack.pop() * stack.pop()
                    stack.append(ans)
                case "/":
                    second = stack.pop()
                    first = stack.pop()
                    stack.append(int(first / second))
                case _:
                    stack.append(int(t))
        return int(stack.pop())