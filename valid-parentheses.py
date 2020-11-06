class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return True
        stack = []
        stack.append(s[0])
        for c in s[1:]:
            if c is '(' or c is '[' or c is '{':
                stack.append(c)
            else:
                if stack:
                    if c is ')' and stack[-1] is '(': 
                        stack.pop()
                    elif c is ']' and stack[-1] is '[':
                        stack.pop()
                    elif c is '}' and stack[-1] is '{':
                        stack.pop()
                    else:
                        stack.append(c)
                else:
                    stack.append(c)
        return False if stack else True

print(Solution().isValid('()]')) 