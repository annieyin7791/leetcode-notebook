# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.
# Core logic: XOR & Hash set

# 10011 & 11 ^= 10000
# 10011 & 100 ^= 10111
# 10011 & 10011 ^= 00000

class Solution:
  def single(self, nums: List[int]) -> int:
    answer = 0
    for num in nums:
      answer ^= num
    return answer
