"""
class BSTPrinter  -- implements a singleton tree printer --

@author: Bart Gerritsen
@date: Sep 15, 2019
@version: 2019-1.0

@description
------------
class BSTPrinter supports the following tree printing formats:

pre: str(Node) implemented

1. print all nodes 
2. print nodal data in order, using an inorder tree traversal
3. print tree structure 

All these methods can be prepended by a header

@restrictions

@change proposals
-----------------
- TestNode class could be turned into a factory class
"""

class BSTPrinter:
	"""prints a tree structure in text (singleton)"""

	__instance = None


	@staticmethod
	def print_tree_node(node):
		"""print the data member of the node, using node.__str__()"""
		print(f'{str(node):s}', end=' ')

	@staticmethod
	def get_instance():
		"""return the singleton instance"""
		if BSTPrinter.__instance is None:
			BSTPrinter()
		return BSTPrinter.__instance

	@staticmethod
	def __call__():
		"""provide clue on the use of this class"""
		raise TypeError('Singleton. Access through `get_instance()`.')


	def __init__(self):

		if BSTPrinter.__instance is not None:
			raise Exception("singleton class. No multiple instances")
		else:
			BSTPrinter.__instance = self


	@classmethod
	def print_header(cls, title, banner=True, width=80):
		if banner == True:
			print(''.join(['-' for s in range(width)]))
			print(title)
		if banner == True:
			print(''.join(['-' for s in range(width)]))


	@classmethod
	def print_tree_structure(cls, tree, title='', header=True):
		"""print tree BSTNodes in a tree structure"""

		def _print_subtree(subtree, level=0):
			if subtree is None:
				return
			else:
				# walk down the right subtree first ...
				_print_subtree(subtree.right,level+1)
				# ... now print the BSTNode ...
				_print_BSTNode_at_level(subtree, level)
				# ... and walk down the left subtree ...
				_print_subtree(subtree.left, level+1)

		def _print_BSTNode_at_level(node, level):
			TAB, SPACE = (6, ' ')
			line = '' + SPACE * (TAB*level) + str(node.data)
			print(line)

		if header == True:
			cls.print_header(title, width=40)
		if tree is None:
			print('tree is None')
		# now start walking the tree and print ...
		_print_subtree(tree, level=0)

	@classmethod
	def print_BSTNodes_sorted(cls, tree, title='', header=True):
		"""print tree BSTNodes in order"""
		if header == True:
			cls.print_header(title, width=40)
		if tree is None:
			print('print tree structure: cannot print None tree')
		else:
			# print the tree 
			tree.traverse_tree_in_order(BSTPrinter.print_tree_node)
			print()

