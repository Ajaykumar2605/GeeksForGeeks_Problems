class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char=set()
        l=0
        result=0
        for r in range(len(s)):
            while s[r] in char:
                char.remove(s[l])
                l+=1
            char.add(s[r])
            result = max(result,r-l+1)
        return result
