class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if (root == None):
            return None

        def Prefix(root, res):
            if not root:
                return
            Prefix(root.left, res)
            res.append(root.val)
            Prefix(root.right, res)

        dummy_head = Node(0)
        dummy_tail = Node(0)
        current = dummy_head
        dummy_head.right = dummy_tail
        dummy_tail.left = dummy_head

        linear_tree = []
        Prefix(root, linear_tree)

        for num in linear_tree:
            temp = Node(num)
            temp.right = current.right
            current.right.left = temp
            current.right = temp
            temp.left = current
            current = current.right

        dummy_tail.left.right = dummy_head.right
        dummy_head.right.left = dummy_tail.left

        return dummy_head.right

X = Solution()
root = Node(3)
root.left = Node(2)
root.left.left = Node(1)
root.right = Node(4)
root.right.right = Node(5)

curr = ans = X.treeToDoublyList(root)

loop_print_counter = 0
while(curr):
    print(curr.val)
    curr= curr.right
    if(curr==ans):
        break





