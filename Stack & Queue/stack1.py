class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        brackets_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in brackets_map.values():
                stack.append(char)
            elif char in brackets_map.keys():
                if not stack:
                    return False
                if stack[-1] != brackets_map[char]:
                    return False
                stack.pop()
            else:
                pass
        return len(stack) == 0
