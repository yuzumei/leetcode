l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans=ListNode(-1)
        cur=ans
        memo=0
        while l1 or l2:
            if not l1:
               num=l2.val+memo
               l2=l2.next
            elif not l2:
                num=l1.val+memo
                l1=l1.next
            else:
                num=l1.val+l2.val+memo
                l1 = l1.next
                l2 = l2.next
            memo=0 if num<10 else 1
            if num>=10:
                num-=10
            cur.next=ListNode(num)
            cur=cur.next
        if memo==1:
            cur.next=ListNode(1)
        return ans.next