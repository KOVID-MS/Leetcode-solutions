class Solution(object):
    def reverseWords(self, s):
        s = s.split(' ')
        s = [i for i in s if i!='']
        return ' '.join(reversed(s))

