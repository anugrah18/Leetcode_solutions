class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def Inorder(root):
    if not root:
        return
    Inorder(root.left)
    print(root.val)
    Inorder(root.right)

class Solution:
    def buildTree(self, inorder, postorder):
        mapper = {}
        for i, v in enumerate(inorder):
            mapper[v] = i

        def helper(low, high):
            if low > high:
                return None

            root = TreeNode(postorder.pop())
            mid = mapper[root.val]
            root.right = helper(mid + 1, high)
            root.left = helper(low, mid - 1)

            return root

        return helper(0, len(inorder) - 1)

X= Solution()
root = X.buildTree([3,9,20,15,7],[9,3,15,20,7])
Inorder(root)