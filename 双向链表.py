class Node(object):
    """双向链表的结点"""
    def __init__(self, item):
        # item存放数据元素
        self.item = item
        # next 指向下一个节点的标识
        self.next = None
        # prev 指向上一结点
        self.prev = None

class BilateralLinkList(object):
    def __init__(self):
        self._head=None
    def is_empty(self):
        return self._head is None
    def length(self):
        cur=self._head
        cnt=0
        while cur is not None:
            cnt+=1
            cur=cur.next
        return cnt
    def items(self):
        cur=self._head
        while cur is not None:
            yield cur.item
            cur=cur.next
    def add(self,item):
        node=Node(item)
        if self.is_empty():
            self._head=node
        else:
            node.next=self._head
            self._head.prev=node
            self._head=node
    def append(self,item):
        node=Node(item)
        if self.is_empty():
            self._head=node
        else:
            cur=self._head
            while cur.next is not None:
                cur=cur.next
            cur.next=node
            node.prev=cur
    def insert(self,index,item):
        if index<=0:
            self.add(item)
        elif index>self.length()-1:
            self.append(item)
        else:
            node=Node(item)
            cur=self._head
            for i in range(index):
                cur=cur.next
            node.next=cur
            node.prev=cur.prev
            cur.prev.next=node
            cur.prev=node
    def remove(self,item):
        if self.is_empty():
            return
        cur=self._head
        if cur.item==item:
            if cur.next is None:
                self._head=None
                return True
            else:
                self._head=cur.next
                cur.next.prev=None
                return True
        while cur.next is not None:
            if cur.item==item:
                cur.prev.next=cur.next
                cur.next.prev=cur.prev
                return True
            cur=cur.next
        if cur.item==item:
            cur.prev.next=None
            return True
    def find(self,item):
        return item in self.items()
