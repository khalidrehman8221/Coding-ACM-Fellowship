class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        clean_s = ''.join(char.lower() for char in s if char.isalnum())
        return clean_s == clean_s[::-1]


        