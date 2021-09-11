class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        ans=ListNode(-1)
        temp=[]
        cnt=1
        memo=0
        while head:
            if cnt==left:
                memo=len(temp)
            if left+1<=cnt<=right:
                temp.insert(memo,head.val)
            else:
                temp.append(head.val)
            cnt+=1
            head=head.next
        x=ans
        for item in temp:
            x.next=ListNode(item)
            x=x.next
        return ans.next