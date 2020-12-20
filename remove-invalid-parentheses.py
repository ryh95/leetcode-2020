import bisect
from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if not s: return ['']

        f_0 = [[0 for _ in range(len(s))] for _ in range(len(s))]
        f_1 = [[0 for _ in range(len(s))] for _ in range(len(s))]
        r_0 = [[set() for _ in range(len(s))] for _ in range(len(s))]
        r_1 = [[set() for _ in range(len(s))] for _ in range(len(s))]
        left_pos = [i for i,c in enumerate(s) if c == '(']
        for i,c in enumerate(s):
            if c != '(' and c != ')':
                f_0[i][i],f_1[i][i] = 1,1
                r_0[i][i].add(c)
                r_1[i][i].add(c)
        for l in range(1,len(s)):
            for i in range(0,len(s)-l):
                j = i + l
                if s[j] == '(':
                    # update length
                    f_0[i][j] = max(f_0[i][j-1],f_1[i][j-1])
                    # update result
                    ids = self.argmax(f_0[i][j-1],f_1[i][j-1])
                    r_0[i][j] = self.update_res([r_0[i][j-1],r_1[i][j-1]],ids)
                elif s[j] == ')':
                    # update length
                    f_0[i][j] = max(f_0[i][j - 1], f_1[i][j - 1])
                    # update result
                    ids = self.argmax(f_0[i][j - 1], f_1[i][j - 1])
                    r_0[i][j] = self.update_res([r_0[i][j - 1], r_1[i][j - 1]], ids)
                    # update length
                    inter_left_pos = self.find_left(i, j, left_pos)
                    if inter_left_pos:
                        f_inter = [max(f_0[i][max(i_ - 1,0)], f_1[i][max(i_ - 1,0)]) + max(f_0[i_ + 1][j - 1], f_1[i_ + 1][j - 1]) + 2 for i_ in
                         inter_left_pos]
                        f_1[i][j] = max(f_inter)
                        ids = self.argmax(*f_inter)
                        # update result
                        for id in ids:
                            i_ = inter_left_pos[id]
                            r_l = self.update_res([r_0[i][max(i_-1,0)],r_1[i][max(i_-1,0)]],self.argmax(f_0[i][max(i_-1,0)],f_1[i][max(i_-1,0)]))
                            r_r = self.update_res([r_0[i_+ 1][j - 1], r_1[i_ + 1][j - 1]], self.argmax(f_0[i_ + 1][j - 1], f_1[i_ + 1][j - 1]))
                            if not r_l and not r_r:
                                r_1[i][j].add('('+')')
                            elif (not r_l) and r_r:
                                for res2 in r_r:
                                    r_1[i][j].add('(' + res2 + ')')
                            elif (not r_r) and r_l:
                                for res1 in r_l:
                                    r_1[i][j].add(res1 + '(' + ')')
                            else:
                                for res1 in r_l:
                                    for res2 in r_r:
                                        r_1[i][j].add(res1 + '(' + res2 + ')')
                else:
                    f_0[i][j] = f_0[i][j-1] + 1
                    f_1[i][j] = f_1[i][j-1] + 1
                    if not r_0[i][j-1]:
                        r_0[i][j].add(s[j])
                    else:
                        for e in r_0[i][j-1]:
                            r_0[i][j].add(e+s[j])
                    if not r_1[i][j-1]:
                        r_1[i][j].add(s[j])
                    else:
                        for e in r_1[i][j-1]:
                            r_1[i][j].add(e + s[j])
        res = list(self.update_res([r_0[0][-1],r_1[0][-1]],self.argmax(f_0[0][-1],f_1[0][-1])))
        return res if res else ['']

    def argmax(self,*array):
        # find argmax of an array that has multiple max value
        e = max(array)
        return [i for i,a in enumerate(array) if e == a]

    def update_res(self,cand_res,ids):
        # given a list of set and a list of id,
        # merge the set that id in ids
        j = 0
        comb_res = set()
        for i,res in enumerate(cand_res):
            if j < len(ids) and i == ids[j]:
                comb_res |= res
                j += 1
        return comb_res

    def find_left(self,i,j,left_pos):
        # find position of left parentheses that >=i and <j
        lo = bisect.bisect_left(left_pos,i)
        hi = bisect.bisect_left(left_pos,j)
        return left_pos[lo:hi]

# test = "()())()"
# test = ')('
# test = '(a)())()'
test = '(a)()b)()'
# test = '(a))b)()c'
print(Solution().removeInvalidParentheses(test))