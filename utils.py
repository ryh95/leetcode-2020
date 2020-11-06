from itertools import tee

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def generate_linked_list(size):
	values = range(1,size)
	Nodes = [ListNode(i) for i in values]
	for node_i,node_j in pairwise(Nodes):
		node_i.next = node_j
	return Nodes[0]

def generate_linked_list2(values):
	if not values: return None
	Nodes = [ListNode(i) for i in values]
	for node_i, node_j in pairwise(Nodes):
		node_i.next = node_j
	return Nodes[0]

def generate_tree(values):
	'''
	generate trees with reverse operations of level traversal
	'''
	if not values: return None
	T,j = {0:TreeNode(values[0])},0
	for i in range(len(values)):
		root = T[i]
		if not root: continue
		left,right = j * 2 + 1, j * 2 + 2
		try:
			root.left = TreeNode(values[left]) if values[left] is not None else None
			root.right = TreeNode(values[right]) if values[right] is not None else None
			T[left], T[right] = root.left, root.right
			j += 1
		except IndexError:
			break
	return T[0]

def print_linked_list(head):
	i = head
	while i is not None:
		print(i.val)
		i = i.next