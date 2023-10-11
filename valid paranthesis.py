class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        self.s = s
        count = 0
        stack = []

        if len(s) == 1:
            return False

        if len(s) % 2 == 1:
            return False

        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif i == ')' or i == '}' or i == ']':
                if len(stack) == 0:
                    return False
                p = stack.pop()
                if i == ')' and p == '(':
                    count += 1
                if i == '}' and p == '{':
                    count += 1
                if i == ']' and p == '[':
                    count += 1

        if count == len(s) // 2:
            return True








