class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distributeCoins(self, root):
        self.ans = 0

        def dfs(node):
            if not node:
                return 0
            L, R = dfs(node.left), dfs(node.right)
            self.ans += abs(L) + abs(R)
            return node.val + L + R - 1

        dfs(root)
        return self.ans

root = TreeNode(3)
root.left = TreeNode(0)
root.right = TreeNode(0)
X = Solution()
print(X.distributeCoins(root))