class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        test=str(x)
        temp=test[::-1]
        if test==temp:
            return True
        else:
            return False