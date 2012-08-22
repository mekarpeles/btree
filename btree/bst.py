#-*- coding: utf-8 -*-

"""
    bst - binary trees
    ~~~~~~~~~~~~~~~~~~
    Simple binary tree utility to construct basic Binary Trees +
    perform searches for nodes having a value closest to user defined
    values

    :authors: Mek
    :license: GPLv3
"""

import argparse

class BinaryTree(object):

    def insert_lst(self, values):
        """Wrapper over insert which allows a list to be provided
        instead of a single value
        """
        [self.insert(v) for v in values]

    def insert(self, value, node=None):
        """Insert a Node iteratively within the BinaryTree"""
        if not getattr(self, 'root', None):
            self.root = Node(value)
            return

        current = node if node else self.root
        
        if current.value == value:
            return
        
        if value < current.value:
            if not current.left:
                current.left = Node(value)
                return 
            else:
                return self.insert(value, current.left)

        if value > current.value:
            if not current.right:
                current.right = Node(value)
                return 
            else:
                return self.insert(value, current.right)
    
    def draw(self):
        """Draws the binary tree recursively using a DFS strategy

        example:
        >>> btree = BinaryTree()
        >>> btree.insert([10,11,6,9,8,7])
        >>> btree.draw()
        (6)<-L-[10]
        [6]-R->(9)
        (8)<-L-[9]
        (7)<-L-[8]
        [10]-R->(11)
        """
        current = self.root
        self._draw(current)

    def _draw(self, node=None):
        """Helper func for self.draw() which takes current node as arg"""
        if node.left:
            print "(%s)<-L-[%s]" % (node.left.value, node.value)
            self._draw(node.left)
        if node.right:
            print "[%s]-R->(%s)" % (node.value, node.right.value)
            self._draw(node.right)

    def get_nearest(self, k):
        """O(log n) - Find the node which contains the value which
        closest to the value 'k' within a binary-tree (iterative
        solution)

        example:
        >>> btree = BinaryTree()
        >>> btree.insert_lst([10,11,6,9,8,7])
        >>> btree.find_nearest(5)
        <bs.Node object at 0xb739020c>
        >>> btree.get_nearest(5).value
        6
        """
        best = self.root
        current = self.root

        while True:
            if k == current.value:
                return current

            if k < current.value:
                if not current.left:
                    return best
                if abs(current.left.value - k) < abs(best.value - k):
                    best = current.left
                current = current.left
                    
            if k > current.value:
                if not current.right:
                    return best
                if abs(current.right.value - k) < abs(best.value - k):
                    best = current.right
                current = current.right

            if not (current.left or current.right):
                return best

    def _get_nearest_old(self, k):
        """Yu, This was the first, incorrect interview attempt"""
        best_distance = abs(current_node.value - k)
        current_node = tree.root

        # Break/return when we notice that both of the children
        # have a greater difference than the parent
        while True:
            distance_parent = abs(current_node.value - k)
            if not (current_node.left and current_node.right):
                return current_node

            if current_node.left:
                distance_left = abs(current_node.left.value - k)

            if current_node.right:
                distance_right = abs(current_node_.right.value - k)            

            if current_node.right and distance_right < distance_parent:
                # continue loop, use distance_right as parent_node
                current_node = current_node.right

            elif current_node.left and distance_left < distance_parent:
                current_node = current_node.left

class Node(object):
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def setup():
    """Configures argparser to handle command line arguments"""
    parser = argparse.ArgumentParser(description='Builds a Binary Search Tree ' \
                                         '(BST) and finds the node containing ' \
                                         'the closest value to some value k')
    parser.add_argument('-i', '--items', type=str,
                        help='An ordered csv of int items to insert into ' \
                            'the binary tree, e.g: -i 10,11,6,9,8,7')
                        
    parser.add_argument('-k', '--nearest', type=int,
                        help='Find the node containing the abs(value) closest '\
                            'to that if value k')
    return parser.parse_args()

if __name__ == "__main__":
    args = setup()
    btree = BinaryTree()
    if args.items:
        btree.insert_lst(map(int, args.items.split(",")))
        btree.draw()
        if args.nearest:
            nearest = btree.get_nearest(args.nearest)
            print nearest.value
