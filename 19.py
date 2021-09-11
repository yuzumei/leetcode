class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ans=ListNode(-1)
        ans.next=head
        cur=head
        for _ in range(n):
            cur=cur.next
        start=ans
        while cur:
            start=start.next
            cur=cur.next
        start.next=start.next.next
        return ans.next