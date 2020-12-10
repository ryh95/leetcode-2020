# Definition for singly-linked list.
from utils import print_linked_list, generate_linked_list2


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head: return None

        j = head
        new_head = head
        while j.next:
            # insert a[i] into a[:i]

            # 1. cut off the next node
            i = j.next
            j.next = i.next if i else None

            # 2. the insertion procedure
            k,k_prev = new_head,ListNode(None)
            k_prev.next = k
            while (k_prev is not j) and k:
                if i.val <= k.val:
                    break
                k = k.next
                k_prev = k_prev.next

            # 3. insert
            k_prev.next = i
            i.next = k

            # 4. update the new head
            if i.val <= new_head.val: new_head = i
            if j.val < i.val: j = j.next

        return new_head

# test = [4,2,1,3]
# test = [1]
# test = [1,1,0]
# test = [1,1]
test = [-1,5,3,4,0]
llst = generate_linked_list2(test)
sort_llst = Solution().insertionSortList(llst)
print_linked_list(sort_llst)