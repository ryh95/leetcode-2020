# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        l_a,l_b = 0,0
        p_a,p_b = headA,headB
        if not headA or not headB: return None
        while p_a:
            p_a = p_a.next
            l_a += 1
        while p_b:
            p_b = p_b.next
            l_b += 1
        i,j = headA,headB
        # 将A，B的长度调整为一样长
        # 然后同时向前走
        while l_a < l_b:
            j = j.next
            l_b -= 1
        while l_b < l_a:
            i = i.next
            l_a -= 1
        while i and j:
            if i == j:
                return i
            i,j = i.next,j.next
        return None