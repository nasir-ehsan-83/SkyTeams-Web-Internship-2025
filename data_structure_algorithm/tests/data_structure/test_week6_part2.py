import unittest

from data_structure_algorithm.data_structure.week6.question1 import TreeNode
from data_structure_algorithm.data_structure.week6.question11 import diameterOfTree
from data_structure_algorithm.data_structure.week6.question12 import isSubtree
from data_structure_algorithm.data_structure.week6.question13 import isBST
from data_structure_algorithm.data_structure.week6.question14 import countSingleValuedSubtrees
from data_structure_algorithm.data_structure.week6.question15 import zigzagLevelOrder
from data_structure_algorithm.data_structure.week6.question16 import boundaryTraversal
from data_structure_algorithm.data_structure.week6.question17 import buildTree
from data_structure_algorithm.data_structure.week6.question18 import bstFromPreorder
from data_structure_algorithm.data_structure.week6.question19 import lowestCommonAncestor
from data_structure_algorithm.data_structure.week6.question20 import printAncestors

class TestWeek6Part2(unittest.TestCase):
    def test_diameter(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        self.assertEqual(diameterOfTree(root), 4)

    def test_subtree(self):
        s = TreeNode(3)
        s.left = TreeNode(4)
        s.right = TreeNode(5)
        s.left.left = TreeNode(1)
        s.left.right = TreeNode(2)

        t = TreeNode(4)
        t.left = TreeNode(1)
        t.right = TreeNode(2)

        self.assertTrue(isSubtree(s, t))

    def test_is_bst(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        self.assertTrue(isBST(root))
        root.right.val = 0
        self.assertFalse(isBST(root))

    def test_count_single_valued(self):
        root = TreeNode(5)
        root.left = TreeNode(1)
        root.right = TreeNode(5)
        root.right.right = TreeNode(5)
        root.right.left = TreeNode(5)
        self.assertEqual(countSingleValuedSubtrees(root), 4)

    def test_zigzag(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        self.assertEqual(zigzagLevelOrder(root), [[1],[3,2],[4,5]])

    def test_boundary(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(6)
        root.right.left = TreeNode(7)
        self.assertEqual(boundaryTraversal(root), [1,2,4,5,7,6,3])

    def test_build_tree(self):
        preorder = [3,9,20,15,7]
        inorder = [9,3,15,20,7]
        root = buildTree(preorder, inorder)
        self.assertEqual(root.val, 3)
        self.assertEqual(root.left.val, 9)
        self.assertEqual(root.right.val, 20)
        self.assertEqual(root.right.left.val, 15)
        self.assertEqual(root.right.right.val, 7)

    def test_bst_from_preorder(self):
        preorder = [8,5,1,7,10,12]
        root = bstFromPreorder(preorder)
        self.assertEqual(root.val, 8)
        self.assertEqual(root.left.val, 5)
        self.assertEqual(root.right.val, 10)
        self.assertEqual(root.left.left.val, 1)
        self.assertEqual(root.left.right.val, 7)
        self.assertEqual(root.right.right.val, 12)

    def test_lca(self):
        root = TreeNode(3)
        root.left = TreeNode(5)
        root.right = TreeNode(1)
        root.left.left = TreeNode(6)
        root.left.right = TreeNode(2)
        root.right.left = TreeNode(0)
        root.right.right = TreeNode(8)
        p = root.left
        q = root.right
        self.assertEqual(lowestCommonAncestor(root, p, q).val, 3)

    def test_ancestors(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        self.assertEqual(printAncestors(root, 5), [2,1])

    
if __name__ == "__main__":
	unittest.main()