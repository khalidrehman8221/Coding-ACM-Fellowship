class Solution(object):
    def romanToInt(self, s):
       
        """
        :type s: str
        :rtype: int
        """
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        n = len(s)

        for i in range(n):
           
            if i < n - 1 and roman_numerals[s[i]] < roman_numerals[s[i + 1]]:
                total -= roman_numerals[s[i]]
            else:
                total += roman_numerals[s[i]]

        return total