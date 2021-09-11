[[1,4,5],[1,3,4],[2,6]]
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        import heapq
        dummy = ListNode(0)
        p = dummy
        head = []
        for i in range(len(lists)):
            if lists[i] :
                heapq.heappush(head, (lists[i].val, i))
                lists[i] = lists[i].next
        while head:
            val, idx = heapq.heappop(head)
            p.next = ListNode(val)
            p = p.next
            if lists[idx]:
                heapq.heappush(head, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return dummy.next

        import heapq
        ans=ListNode(-1)
        cur=ans
        head=[]
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(head,(lists[i].val,i))
                lists[i]=lists[i].next
        while head:
            temp,num=heapq.heappop(head)
            cur.next=ListNode(temp)
            cur=cur.next
            if lists[num]:
                heapq.heappush(head,(lists[num].val,num))
                lists[num]=lists[num].next
        return ans.next
        '''超时'''
        # if len(lists)<2:
        #     return lists[0]
        # def merge(l1,l2):
        #     ans=ListNode(-1)
        #     cur=ans
        #     while l1 and l2:
        #         if l1.val<=l2.val:
        #            cur.next=ListNode(l1.val)
        #            l1=l1.next
        #         else:
        #             cur.next=ListNode(l2.val)
        #             l2=l2.next
        #         cur=cur.next
        #     if l1:
        #         cur.next=l1
        #     elif l2:
        #         cur.next=l2
        #     return ans
        # res=merge(lists[0],lists[1])
        # for i in range(2,len(lists)):
        #     res=merge(res,lists[i])
        # return res