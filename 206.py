class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        ans=ListNode(head.val)
        head=head.next
        while head:
            temp=ListNode(head.val)
            temp.next=ans
            ans=temp
            head=head.next
        return ans