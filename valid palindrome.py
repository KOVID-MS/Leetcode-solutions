class Solution(object):
    def isPalindrome(self, s):
        s = ''.join(i for i in s if i.isalnum()).lower()
        start,end = 0,len(s)-1
        while start <= end:
            if s[start] == s[end]:
                start+=1
                end-=1
            else:
                return False
        return True