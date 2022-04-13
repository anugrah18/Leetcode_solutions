
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def partition(self, head, x):
        node1 = ListNode()
        node2 = ListNode()

        ptr = head
        ptr1 = node1
        ptr2 = node2

        while (ptr):
            if (ptr.val < x):
                ptr1.next = ListNode(ptr.val)
                ptr1 = ptr1.next
            else:
                ptr2.next = ListNode(ptr.val)
                ptr2 = ptr2.next
            ptr = ptr.next

        ptr1 = node1
        ptr2 = node2

        if (ptr1.next == None):
            return ptr2.next
        elif (ptr2.next == None):
            return ptr1.next
        else:
            while (ptr1.next):
                ptr1 = ptr1.next

            ptr1.next = ptr2.next

        return node1.next

node = ListNode(1)
node.next = ListNode(4)
node.next.next = ListNode(3)
node.next.next.next = ListNode(2)
node.next.next.next.next = ListNode(5)
node.next.next.next.next.next = ListNode(2)

X = Solution()
resNode = X.partition(node,3)
