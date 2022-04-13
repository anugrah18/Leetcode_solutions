class Node:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right =right

    def maxDepth(self,root):
        if(root == None):
            return 0
        else:
            lHeight = self.maxDepth(root.left)
            rHeight = self.maxDepth(root.right)
            return max(lHeight,rHeight)+1

tree=  Node(3)
tree.left = Node(9)
tree.right = Node(20)
tree.right.left = Node(15)
tree.right.right = Node(7)
tree.right.left.left = Node(25)

print(tree.maxDepth(tree))






