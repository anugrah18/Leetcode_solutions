# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printList(self):
        while(self):
            print(self.val)
            self=self.next


class Solution(object):
    def addTwoNumbers(self, l1, l2):

        n1 = 0
        n2 = 0

        while (l1):
            n1 = 10 * n1 + l1.val
            l1 = l1.next

        while (l2):
            n2 = 10 * n2 + l2.val
            l2 = l2.next

        n = n1 + n2
        root = curr = ListNode(0)

        for i in str(n):
            curr.next = ListNode(int(str(i)))
            curr = curr.next

        return root.next

L1 = ListNode(7)
L1.next = ListNode(2)
L1.next.next = ListNode(4)
L1.next.next.next = ListNode(3)

L2 = ListNode(5)
L2.next = ListNode(6)
L2.next.next = ListNode(4)

X =Solution()
L3 = X.addTwoNumbers(L1,L2)

L3.printList()