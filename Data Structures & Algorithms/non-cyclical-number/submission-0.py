class Solution:
    def isHappy(self, n: int) -> bool:
        cycle = set()
        while n != 1:
            sumSquares = 0
            for digit in str(n):
                sumSquares += int(digit) ** 2
            n = sumSquares
            if n in cycle:
                return False
            cycle.add(n)
        return True
             
            
