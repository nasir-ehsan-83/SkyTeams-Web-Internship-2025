import unittest

from data_structure_algorithm.data_structure.week6.question1 import TreeNode, treeHeight
from data_structure_algorithm.data_structure.week6.question2 import isIdentical
from data_structure_algorithm.data_structure.week6.question3 import mirrorTree
from data_structure_algorithm.data_structure.week6.question4 import isSymmetric
from data_structure_algorithm.data_structure.week6.question5 import isBalanced
from data_structure_algorithm.data_structure.week6.question6 import childrenSum
from data_structure_algorithm.data_structure.week6.question7 import sortedArrayToBST
from data_structure_algorithm.data_structure.week6.question8 import nodesAtDistanceK
from data_structure_algorithm.data_structure.week6.question9 import inorderSuccessor
from data_structure_algorithm.data_structure.week6.question10 import kthLargest

# a helper function for test_array_to_bs()
def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

class TestWeek6Part1(unittest.TestCase):
    def test_height(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        self.assertEqual(treeHeight(root), 3)
        self.assertEqual(treeHeight(None), 0)

    def test_identical(self):
        t1 = TreeNode(1)
        t1.left = TreeNode(2)
        t1.right = TreeNode(3)

        t2 = TreeNode(1)
        t2.left = TreeNode(2)
        t2.right = TreeNode(3)

        t3 = TreeNode(1)
        t3.left = TreeNode(2)

        self.assertTrue(isIdentical(t1, t2))
        self.assertFalse(isIdentical(t1, t3))

    def test_mirror(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        mirrored = mirrorTree(root)
        self.assertEqual(mirrored.left.val, 3)
        self.assertEqual(mirrored.right.val, 2)

    def test_symmetric(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(3)
        self.assertTrue(isSymmetric(root))

        root.right.right.val = 5
        self.assertFalse(isSymmetric(root))

    def test_balanced(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        self.assertTrue(isBalanced(root))

        root.left.left.left = TreeNode(6)
        self.assertFalse(isBalanced(root))

    def test_children_sum(self):
        root = TreeNode(10)
        root.left = TreeNode(4)
        root.right = TreeNode(6)
        self.assertTrue(childrenSum(root))

        root.right.val = 5
        self.assertFalse(childrenSum(root))

    def test_array_to_bst(self):
        arr = [1,2,3,4,5]
        root = sortedArrayToBST(arr)
        self.assertEqual(inorder(root), arr)
        

    def test_nodes_distance_k(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        self.assertEqual(nodesAtDistanceK(root, 2), [4,5])

    def test_successor(self):
        root = TreeNode(20)
        root.left = TreeNode(10)
        root.right = TreeNode(30)
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(15)
        node = root.left
        self.assertEqual(inorderSuccessor(root, node).val, 15)

    def test_kth_largest(self):
        root = TreeNode(20)
        root.left = TreeNode(10)
        root.right = TreeNode(30)
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(15)
        self.assertEqual(kthLargest(root, 1), 30)
        self.assertEqual(kthLargest(root, 3), 15)

    
if __name__ == "__main__":
	unittest.main()