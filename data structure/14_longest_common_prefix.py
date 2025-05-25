# String Compare Solution

# Compare the word (i) of each string input
# If found difference -> stop the loop and return the current same word

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

      result = ""
      for i in range(len(strs)):
        for s in strs:
          if i = len(strs) or strs[i] != strs[0][i]:
            return result
        result += strs[0][i]
      return result
        
