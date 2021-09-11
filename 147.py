class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        support=ListNode(0)
        support.next=head
        lastsorted=head
        cur=head.next

        while cur:
            if lastsorted.val<=cur.val:
                lastsorted=lastsorted.next
            else:
                start=support
                while start.next.val<=cur.val:
                    start=start.next
                lastsorted.next=cur.next
                cur.next=start.next
                start.next=cur
            cur=lastsorted.next
        return support.next
        # lastSorted = head
        # curr = head.next
        #
        # while curr:
        #     if lastSorted.val <= curr.val:
        #         lastSorted = lastSorted.next
        #     else:
        #         prev = dummyHead
        #         while prev.next.val <= curr.val:
        #             prev = prev.next
        #         lastSorted.next = curr.next
        #         curr.next = prev.next
        #         prev.next = curr
        #     curr = lastSorted.next
        #
        # return dummyHead.next
