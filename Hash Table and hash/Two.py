class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        mapping_s_t = {}
        mapping_t_s = {}

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]

            if char_s in mapping_s_t:
                if mapping_s_t[char_s] != char_t:
                    return False
            else:
                mapping_s_t[char_s] = char_t

            if char_t in mapping_t_s:
                if mapping_t_s[char_t] != char_s:
                    return False
            else:
                mapping_t_s[char_t] = char_s

        return True

        