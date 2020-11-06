# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        i = head
        while i is not None:
            if hasattr(i,visit): return True
            i.visit = True
            i = i.next
        return False