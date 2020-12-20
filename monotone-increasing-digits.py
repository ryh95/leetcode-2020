class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        i,j = 0,0
        n_str = str(N)
        while j < len(n_str)-1 and int(n_str[j+1]) >= int(n_str[j]):
            if int(n_str[j+1]) - int(n_str[j]) >= 1:
                i = j + 1
            j += 1
        if j == len(n_str)-1:
            return N
        else:
            return int(n_str[:i] + str(int(n_str[i])-1) + (len(n_str)-1-i) * '9')

tests = [
# 3499,3399,1234,9,299,667999
    3549,3443,1234,10,332,668841
]
for test in tests:
    print(Solution().monotoneIncreasingDigits(test))