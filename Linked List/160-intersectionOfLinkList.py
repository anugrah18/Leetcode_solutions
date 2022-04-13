class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):

        head1 = headA
        head2 = headB
        dict = {}
        while (head1 != None):
            if (head1 not in dict):
                dict[head1] = "occupied"
            head1 = head1.next

        while (head2 != None):
            if (head2 in dict):
                return head2
            head2 = head2.next

        return None

LL1 = ListNode(4)
LL1.next = ListNode(7)
LL1.next.next = ListNode(8)
LL1.next.next.next = ListNode(3)

LL2 = ListNode(1)
LL2.next = ListNode(6)
LL2.next.next = LL1.next

X = Solution()
print(X.getIntersectionNode(LL1,LL2).val)