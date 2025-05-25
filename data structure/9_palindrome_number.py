# Math Solution 
# Find the left digit: try to find the division based on the number of digits of this number
# Find the right digit: Use % to find the remainder


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return false

        div = 1
        while x >= div * 10:
          div *= 10
        while x:
          right = x % 10
          left = x // div
          if left != right:
            return false
          x = (x % div) // 10
          # ex. x = 12321, div = 10000
          # 12321 % 10000 = 2321 
          # 2321 // 10 = 232  -> so that can continually compare "232"
          div = div / 100
          # After removing left & right digits, the number itself will also recude 2 number of digits
        return True
      
