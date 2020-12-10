import re
from collections import deque


class Solution:

    def __init__(self):
        self.match_num = re.compile('\d+')

    def decodeString(self, s: str) -> str:

        # base condition
        match_obj = re.search(self.match_num, s)
        if not match_obj: return s

        i,j = match_obj.span()
        j_ = self.get_closed_pos(s,j)
        return s[:i] + int(s[i:j]) * self.decodeString(s[j+1:j_]) + self.decodeString(s[j_+1:])

    def get_closed_pos(self,s,i):
        # s: string
        # i: start index, i.e. s[i] == '['

        ## the goal is to find the end index that close the bracket
        stack = deque(['['])
        j = i
        while stack:
            if s[j+1] == ']': stack.pop()
            if s[j+1] == '[': stack.append('[')
            j += 1
        return j

tests = [
    "3[a]2[bc]",
    "3[a2[c]]",
    "2[abc]3[cd]ef",
    "abc3[cd]xyz",
    '3[a2[c]]2[abc]',
    '1[abc2[bc]]',
    ''
]

for test in tests:
    print(Solution().decodeString(test))