class Solution:
    def isNumber(self, s: str) -> bool:
        valid_c = set(list(str(i) for i in range(10))+['.','+','-','e','E'])
        s = s.strip()
        if set(s) - valid_c: return False
        split_s = s.lower().split('e')
        if len(split_s) == 1:
            return self.isReal(split_s[0])
        elif len(split_s) == 2:
            return self.isReal(split_s[0]) and self.isInteger(split_s[1])
        else:
            return False

    def isReal(self,s):
        split_s = s.split('.')
        if len(split_s) == 1:
            return self.isInteger(split_s[0])
        elif len(split_s) == 2:
            if not split_s[0]:
                # .342
                return self.isUnsignedInteger(split_s[1])
            if not split_s[1]:
                # +1.
                return self.isInteger(split_s[0])

            if (split_s[0] == '+' or split_s[0] == '-') and self.isUnsignedInteger(split_s[1]): return True # +.8

            return self.isInteger(split_s[0]) and self.isUnsignedInteger(split_s[1])
        else:
            return False

    def isInteger(self,s):
        if not s: return False
        if len(s) == 1:
            return True if s[0].isdigit() else False
        else:
            is_unsigned = self.isUnsignedInteger(s[1:])
            if (s[0] == '+' and is_unsigned) or (s[0] == '-' and is_unsigned) or (s[0].isdigit() and is_unsigned):
                return True
            else:
                return False

    def isUnsignedInteger(self,s):
        if not s: return False
        for c in s:
            if not c.isdigit(): return False
        return True

test = '+100'
test = '5e2'
test = '-123'
test = '3.1416'
test = '-1E-16'
test = '0123'
test = '12e'
test = '1a3.14'
test = '1.2.3'
test = '+-5'
test = '12e+5.4'
test = 'e2'
test = '.e2'
test = '1.e2'
# test = '1.0e2'
test = '1 '
test = '+.8'
sol = Solution()
print(sol.isNumber(test))