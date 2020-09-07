# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printList(self):
        while(self):
            print(self.val)
            self= self.next

class Solution(object):
    def removeNthFromEnd(self, head, n):

        dummy = ListNode(0, head)
        ptr1 = dummy
        ptr2 = dummy
        counter = 0

        while (ptr2):
            if (counter == n):
                break
            counter = counter + 1
            ptr2 = ptr2.next

        while (ptr2):
            if (ptr2.next == None):
                ptr1.next = ptr1.next.next
                break
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return dummy.next

LL = ListNode(1)
LL.next = ListNode(2)
LL.next.next = ListNode(3)
LL.next.next.next = ListNode(4)
LL.next.next.next.next = ListNode(5)

X = Solution()
answer =X.removeNthFromEnd(LL,2)
answer.printList()




