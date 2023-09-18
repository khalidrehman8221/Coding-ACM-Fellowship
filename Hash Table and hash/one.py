class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def get_next(n):
            next_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                next_sum += digit ** 2

            return next_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1    
