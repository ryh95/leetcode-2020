# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        i,j = 0,0
        pre_a,p_b = list1,list1
        while j < b:
            p_b = p_b.next
            j += 1

        while i < a - 1:
            pre_a = pre_a.next
            i += 1
        pre_a.next = list2

        list2_end = list2
        while list2_end.next:
            list2_end = list2_end.next
        list2_end.next = p_b.next

        return list1


