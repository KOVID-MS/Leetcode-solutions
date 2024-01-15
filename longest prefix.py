class Solution(object):
    def longestCommonPrefix(self, strs):
        output = ''
        l = min(len(s) for s in strs)
        string = ''
        if l == 0:
            return string
        if len(strs) == 1:
            return strs[0]
        for i in range(l):
            for s in strs:
                if s[i] != strs[0][i]:
                    return string
            string+=strs[0][i]
        return string