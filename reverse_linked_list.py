# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def reverseList(self, head: ListNode) -> ListNode:
		cur_n = head
		# save values of linked list into a list 
		vals = []
		while cur_n is not None:
			vals.append(cur_n.val)
			cur_n = cur_n.next
		if not vals: return head # if head is none 
		# reverse the list and generate the linked list
		head = ListNode(vals[-1])
		a = head
		for val in vals[-2::-1]:
			b = ListNode(val)
			a.next = b
			a = b
		return head

# test
vals = []
head = ListNode(vals[-1])
a = head
print(a.val)
for val in vals[-2::-1]:
	b = ListNode(val)
	a.next = b
	a = b
	print(a.val)

# cur_n = head
# vals2 = []
# while cur_n is not None:
#     vals2.append(cur_n.val)
#     cur_n = cur_n.next
# print(vals2)