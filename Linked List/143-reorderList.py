# Definition for singly-linked list.
class ListNode:
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next

class Solution:
    def reorderList(self,head):

        if not head:
            return

        # Find the middle of link list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second part of list in-place
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # Merge two sorted Link List
        first, second = head, prev

        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next

X = Solution()
Node = ListNode()
Node.next = ListNode(1)
Node.next.next = ListNode(2)
Node.next.next.next = ListNode(3)
Node.next.next.next.next = ListNode(4)

ans = Node.next
X.reorderList(ans)

while(ans):
    print(ans.val)
    ans = ans.next
