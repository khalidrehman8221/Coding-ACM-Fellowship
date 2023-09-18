class Solution(object):
    def findAnagrams(self, s, p):
        result = []
        len_s, len_p = len(s), len(p)

        if len_s < len_p:
            return result

        p_count = [0] * 26
        s_count = [0] * 26

        # Count the characters in the pattern string p
        for char in p:
            p_count[ord(char) - ord('a')] += 1

        # Initialize the sliding window
        for i in range(len_p):
            s_count[ord(s[i]) - ord('a')] += 1

        # Check if the initial window is an anagram
        if s_count == p_count:
            result.append(0)

        # Move the sliding window and update the character counts
        for i in range(len_p, len_s):
            s_count[ord(s[i - len_p]) - ord('a')] -= 1
            s_count[ord(s[i]) - ord('a')] += 1

            # Check if the current window is an anagram
            if s_count == p_count:
                result.append(i - len_p + 1)

        return result
