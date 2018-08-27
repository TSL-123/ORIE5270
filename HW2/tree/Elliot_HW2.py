
# coding: utf-8

# In[7]:

import math


class Tree(object):

    def __init__(self, root, depth=1, max_depth=0, matrix=[[]]):
        """
        constructor
        :param root: the root node
        :param depth: depth of current node
        :param max_depth: max_depth we reached till now
        :param matrix: matrix to record the node value we went through
        """
        self.root = root
        self.depth = depth
        self.max_depth = max_depth
        self.matrix = matrix

    def get_value_root(self):
        """
        get the value of the root node
        :return: numerical return
        """
        return self.root.value

    def run_through_tree(self):
        """
        Function to go through the tree and record nodes in a way easy to print.
        Also get the max_depth to decide the size of the print matrix
        :return: current depth, max_depth we reached, The matrix recorded nodes in different layers
        """
        global depth
        global max_depth
        global matrix
        if self.depth > self.max_depth:
            self.max_depth = self.depth
            self.matrix.append([])
        if self.root.left is not None:
            self.depth, self.max_depth, self.matrix = \
                Tree(self.root.left, self.depth+1, self.max_depth, self.matrix).run_through_tree()
        else:
            self.matrix[self.depth].append('.')
        if self.root.right is not None:
            self.depth, self.max_depth, self.matrix = \
                Tree(self.root.right, self.depth+1, self.max_depth, self.matrix).run_through_tree()
        else:
            self.matrix[self.depth].append('.')
        self.matrix[self.depth-1].append(self.get_value_root())
        return self.depth-1, self.max_depth, self.matrix

    def print_tree(self):
        """
        With the max_depth and matrix from run_through_trees, print the tree iteratively
        Notes: '.' is uesd when some parent node is None. So that their children node is also '.'.
        :return: print_matrix, which is the matrix we want to print
        """
        self.matrix = [[]]
        self.max_depth = 0
        self.depth = 1
        self.depth, self.max_depth, self.matrix = self.run_through_tree()
        print_matrix = []
        for i in range(self.max_depth):
            print_matrix.append([])
            for j in range(2**self.max_depth-1):
                temp = 2**(self.max_depth-i+1)
                if (j+1) % (2**(self.max_depth-i-1)) == 0 and (j+1) % (2**(self.max_depth-i)) != 0:
                    if i == 0:
                        print_matrix[i].append(self.matrix[i].pop(0))
                    elif print_matrix[i-1][int(math.floor((j+1)/temp)*temp+temp/2-1)] != '.':
                        print_matrix[i].append(self.matrix[i].pop(0))
                    elif print_matrix[i-1][int(math.floor((j+1)/temp)*temp+temp/2-1)] == '.':
                        print_matrix[i].append('.')
                    else:
                        print_matrix[i].append('|')
                else:
                    print_matrix[i].append('|')
        for i in range(self.max_depth):
            for j in range(2**self.max_depth-1):
                if print_matrix[i][j] == '.':
                    print_matrix[i][j] = '|'
        return print_matrix


class Node(object):

    def __init__(self, value, left, right):
        """
        constructor for Node
        :param value: the value of the node
        :param left: left child of the node
        :param right: right child of the node
        """
        self.value = value
        self.left = left
        self.right = right
