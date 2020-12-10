from collections import OrderedDict, Counter


class Solution:
    def sortString(self, s: str) -> str:

        c = Counter(s)
        d = OrderedDict(sorted(c.items(),key=lambda x: x[0]))
        n_remain_e,res = len(d),[]
        while n_remain_e > 0:
            for k in d.keys():
                if d[k] > 0:
                    res.append(k)
                    d[k] -= 1
                    if d[k] == 0: n_remain_e -= 1
            d = OrderedDict(reversed(d.items()))

        return ''.join(res)

s = "leetcode"
s = 'rat'
s = 'aaaabbbbcccc'
s = 'ggggggg'
s = 'spo'
s = 'l'
print(Solution().sortString(s))