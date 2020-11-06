# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head: return True # zero element case
        i,j = head,head.next
        if not j: return True # one element case
        while j:
            j.prev = i
            i = j
            j = j.next
        j = i
        i = head
        while i != j and j.next != i:
            if i.val != j.val:
                return False
            else:
                i = i.next
                j = j.prev
        return True