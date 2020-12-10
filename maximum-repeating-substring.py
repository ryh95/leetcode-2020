class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        ls,lw = len(sequence),len(word)
        max_res = 0
        # if sequence == word: return 1
        for i in range(ls-lw+1):
            if sequence[i:i+lw] == word:
                res = 1
                j = i + lw
                while j <= ls - lw:
                    if sequence[j:j+lw] != word:
                        break
                    res += 1
                    j += lw
                max_res = max(max_res,res)
        return max_res

sequence = "ababc"
word = "ab"
# sequence = "ababc"
# word = "ba"
# sequence = "ababc"
# word = "ac"
# sequence = 'a'
# word = 'a'
# sequence = 'bbba'
# word = 'a'
print(Solution().maxRepeating(sequence,word))