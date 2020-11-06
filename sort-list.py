# Definition for singly-linked list.
from utils import generate_linked_list2, print_linked_list


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        l,j = 0,head
        while j:
            j = j.next
            l += 1
        head = self.merge_sort(head,l)
        return head

    def merge_sort(self, head: ListNode,l)-> ListNode:
        if not head: return None
        if not head.next: return head
        h1,h2 = self.cut(head,l)
        h1 = self.merge_sort(h1,l//2)
        h2 = self.merge_sort(h2,l - l//2)
        h = self.merge(h1,h2)
        return h

    def cut(self,head: ListNode,l):
        l1,i = l//2,1
        h1,j = head,head
        while i < l1:
            j = j.next
            i += 1
        h2 = j.next
        j.next = None
        return h1,h2

    def merge(self, h1: ListNode, h2: ListNode):
        h = ListNode(None)
        k,i,j = h,h1,h2
        while i and j:
            if i.val <= j.val:
                k.next, i = i, i.next
            else:
                k.next, j = j, j.next
            k = k.next
        k.next = i if i else j
        return h.next

h1 = [2,4]
# h1 = None
h2 = [1]
# h2 = None
h1 = generate_linked_list2(h1)
h2 = generate_linked_list2(h2)
# h = [4,2,3,1,3]
# h = generate_linked_list2(h)
sol = Solution()
h = sol.merge(h1,h2)
# h = sol.sortList(h)
print_linked_list(h)