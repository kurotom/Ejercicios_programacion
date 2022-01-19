# -*- coding:utf-8 -*-

"""
Sample Input

6
3
5
4
7
2
1

Sample Output

3 2 5 1 4 7

"""


class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data
class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left,data)
                root.left = cur
            else:
                cur = self.insert(root.right,data)
                root.right = cur
        return root

    def levelOrder(self, root):
        #Write your code here
        res = []
        lista = []
        if root is not None:
            lista.insert(0, root)
            while lista:
                root = lista.pop()
                res.append(str(root.data)),
                if root.left:
                    lista.insert(0, root.left)
                if root.right:
                    lista.insert(0, root.right)
        a = ""
        for i in res:
            a += " "
            a += i
        print(a.strip())



T=int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root,data)
myTree.levelOrder(root)