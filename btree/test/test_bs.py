import unittest
from btree import bst

BTREE = [1,5,3,7,6,2,9,20,18]

class BinarySearch_Test(unittest.TestCase):

    def test_insert_left(self):
        btree = bst.BinaryTree()
        btree.insert(5)
        btree.insert(3)
        left = btree.root.left
        self.assertTrue(left.value, "No node left of root.")
        self.assertTrue(left.value == 3,
                        "Node left of root has value %s, expected 3" % left.value)

    def test_insert_right(self):
        btree = bst.BinaryTree()
        btree.insert(5)
        btree.insert(7)
        right = btree.root.right
        self.assertTrue(right, "No node right of root.")
        self.assertTrue(right.value == 7,
                        "Node left of root has value %s, expected 7" % right.value)

    def test_nearest(self):
        btree = bst.BinaryTree()
        btree.insert_lst(BTREE)
        node = btree.get_nearest(10)
        self.assertTrue(node.value == 9, "Got the incorrect value when trying to "\
                            "retrieve closest value to 9 in binary tree: %s" % \
                            BTREE)
