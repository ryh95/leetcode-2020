from utils import generate_linked_list,print_linked_list
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        #
        if head is None: return head 
        # init
        l,i = ListNode(None),head,
        j = i.next
        if j is None: return head
        k = j.next
        # first round
        l.next = j
        j.next = i
        i.next = k
        head = j # special
        l = i
        i = k
        if k is None: return head
        j = k.next
        while j is not None:
            k = j.next
            #
            l.next = j
            j.next = i
            i.next = k
            #
            l = i
            i = k
            if k is None: break
            j = k.next
        return head

# test
head = generate_linked_list(2)
# print_linked_list(head)
head_ = Solution().swapPairs(head)
print_linked_list(head_)