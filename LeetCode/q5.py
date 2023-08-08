class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        s = s.strip()

        words = s.split()
        if not words:
            return 0

        return len(words[-1])