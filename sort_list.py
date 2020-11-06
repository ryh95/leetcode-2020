# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        pass

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        i,j = l1,l2
        # boundary case
        if not i and not j: return None
        if not i: return l2
        if not j: return l1
        p = l1 if l1.val <= l2.val else l2
        head = p
        if p == i:
            i = i.next
        else:
            j = j.next
        while i or j:
            if i and (not j or i.val <= j.val):
                p.next = i
                p = i
                i = i.next
            elif j and (not i or i.val > j.val):
                p.next = j
                p = j
                j = j.next
        return head