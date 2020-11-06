# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow,fast = head,head
        t = 0
        while slow is not None and fast is not None:
            slow,fast = slow.next,fast.next
            if fast is None: return None
            fast = fast.next
            t += 1
            if slow is fast: break
        if fast is None or slow is None: return None
        p = head
        if p is slow: return p
        for _ in range(t):
            p,slow = p.next,slow.next
            if p is slow: return p

# test
# a=ListNode(3)
# b=ListNode(2)
# c=ListNode(0)
# d=ListNode(-4)
# a.next = b
# b.next = c
# c.next = d
# d.next = b
a=ListNode(1)
b=ListNode(2)
a.next = b
b.next = b

node = Solution().detectCycle(a)
print(node.val)