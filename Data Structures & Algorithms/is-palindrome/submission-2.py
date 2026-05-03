class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while right > left and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True


    # have one pointer start at beginning of string
    # have second pointer start at end of string
    # compare them to each other and check if they are 
    # equal until they point to the same character