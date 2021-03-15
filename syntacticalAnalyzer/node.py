class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def treeToString(root: Node, string: list):

	if root is None:
		return

	string.append(str(root.data))

	if not root.left and not root.right:
		return

	string.append('(')
	treeToString(root.left, string)
	string.append(')')

	if root.right:
		string.append('(')
		treeToString(root.right, string)
		string.append(')')