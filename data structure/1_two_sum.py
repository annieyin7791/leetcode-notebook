# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# Ex. nums = [2,7,11,15], target = 9
# Out: [0,1]

# Solution 1: 2 for loops -> cost lots of memory
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      for i in range(len(nums)):
        for j in range(i + 1, len(nums)):   # i + 1 to Avoid repeat number
          if nums[i] + nums[j] == target:
            return [i, j]

# Solution 2: 1 loop + hash table
# Hint: target - num1 = num2
