import random


class Solution:
    def modifyString(self, s: str) -> str:
        letters = set('abcdefghijklmnopqrstuvwxyz')
        s_ = '0' + s + '0'
        list_s = [c for c in s_]
        for i in range(1,len(s_)-1):
            if s_[i] == '?':
                t = set([list_s[i - 1], list_s[i + 1]])
                c = (letters - t).pop()
                list_s[i] = c
        return ''.join(list_s[1:-1])

test = '??cs'
print(Solution().modifyString(test))