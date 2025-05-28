# Every time I guess mid point (m), then submit to API
# If m > answer -> guess(m) = -1 -> means the answer is in the left side of the array -> reduce the right boundary to m - 1
# If m < answer -> guess(m) = 1

class Solution:
    def guessNumber(self, n: int) -> int:
      l, r = 1, n
      
      while True:    # Infinite loop until the answer is correct
        m = (l + r) // 2
        result = guess(m)
        if result > 0:
          l = m + 1
        elif result < 0:
          r = m - 1
        else:
          return m
        
