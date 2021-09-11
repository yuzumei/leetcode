class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ans=ListNode(-1)
        ans.next=head
        temp=ans.next
        prev=ans
        while temp and temp.next:
            if temp.val!=temp.next.val:
                temp=temp.next
                prev=prev.next
            else:
                t=temp.val
                while t==temp.val:
                    temp=temp.next
                prev.next=temp
        return ans.next
