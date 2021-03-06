# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printList(self):
        while (self):
            print(self.val)
            self = self.next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        answer = ListNode(0)
        merged = answer
        while (l1 and l2):
            if (l1.val < l2.val):
                newNode = ListNode(l1.val)
                answer.next = newNode
                answer = answer.next
                l1 = l1.next
            else:
                newNode = ListNode(l2.val)
                answer.next = newNode
                answer = answer.next
                l2 = l2.next

        if (l1 == None):
            answer.next = l2
        else:
            answer.next = l1

        return merged.next

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

X = Solution()
answer = X.mergeTwoLists(l1,l2)
answer.printList()