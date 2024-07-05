def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    self.s = s
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
                continue
            if i == '}' and p == '{':
                continue
            if i == ']' and p == '[':
                continue
            else:
                return False

    if stack:
        return False
    return True