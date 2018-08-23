
# coding: utf-8

# In[7]:

import numpy as np
import math

class Tree(object):

    def __init__(self, root,depth=1,max_depth=0,matrix=[[]]):
           self.root = root
           self.depth=depth
           self.max_depth=max_depth
           self.matrix=matrix
    

    def get_value_root(self):
           if self.root is not None:
            return self.root.value
           else:
            return None

    def run_through_tree(self):
        global depth
        global max_depth
        global matrix
        if self.depth>self.max_depth:
            #print(1,depth,max_depth)
            self.max_depth=self.depth
            self.matrix.append([])
        if self.root.left != None:
            #print(2,depth,max_depth)
            self.depth,self.max_depth,self.matrix=Tree(self.root.left,self.depth+1,self.max_depth,self.matrix).run_through_tree()
        else:
            self.matrix[self.depth].append('.')
        if self.root.right !=  None:
            #print(3,depth,max_depth)
            self.depth,self.max_depth,self.matrix=Tree(self.root.right,self.depth+1,self.max_depth,self.matrix).run_through_tree()
        else: 
            self.matrix[self.depth].append('.')
        self.matrix[self.depth-1].append(self.get_value_root())
        return self.depth-1,self.max_depth,self.matrix

    def print_tree(self):
        self.matrix=[[]]
        self.max_depth=0
        self.depth=1
        self.depth,self.max_depth,self.matrix=self.run_through_tree()
        #print(self.matrix)
        #print(self.max_depth)
        print_matrix=[]
        for i in range(self.max_depth):
            print_matrix.append([])
            for j in range(2**self.max_depth-1):
                temp=2**(self.max_depth-i+1);
                #print(temp)
                #print(int(math.floor((j+1)/temp)*temp+temp/2-1));
                if((j+1)%(2**(self.max_depth-i-1))==0 and (j+1)%(2**(self.max_depth-i))!=0):
                    if i==0:
                        print_matrix[i].append(self.matrix[i].pop(0))
                        #print(1)
                    elif(print_matrix[i-1][int(math.floor((j+1)/temp)*temp+temp/2-1)]!='.'):
                        print_matrix[i].append(self.matrix[i].pop(0))
                        #print(2)
                    elif print_matrix[i-1][int(math.floor((j+1)/temp)*temp+temp/2-1)]=='.':
                        print_matrix[i].append('.') 
                    else:
                        #print(3)
                        print_matrix[i].append('|')  
                else:
                    #print(3)
                    print_matrix[i].append('|')
                #print(print_matrix)
        for i in range(self.max_depth):
            for j in range(2**self.max_depth-1):
                if(print_matrix[i][j]=='.'):
                    print_matrix[i][j]='|'
        return print_matrix
        


class Node(object):

    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

