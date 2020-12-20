from collections import Counter, deque


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        cout = Counter(s)
        stack,chars = deque(),set()
        for c in s:
            if c not in chars:
                # add to stack
                while stack and c < stack[-1] and cout[stack[-1]] > 0:
                    chars.remove(stack.pop())
                stack.append(c)
                chars.add(c)
            cout[c] -= 1
        return ''.join(stack)


s = "cbacdcbc"
# s = "bcabc"
# s = 'a'
# s = 'acbacd'
# s = "bbcaac"
print(Solution().removeDuplicateLetters(s))