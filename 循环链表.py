class Node(object):
    """链表的结点"""
    def __init__(self, item):
        # item存放数据元素
        self.item = item
        # next是下一个节点的标识
        self.next = None

class SingleCycleLinkList(object):
    def __init__(self):
        self._head=None
    def is_empty(self):
        return self._head is None
    def length(self):
        if self.is_empty():
            return 0
        #链表不为空
        cnt=1
        cur=self._head
        while cur.next!=self._head:
            cnt+=1
            cur=cur.next
        return cnt
    def items(self):
        if self.is_empty():
            return
        cur=self._head
        while cur.next!=self._head:
            yield cur.item
            cur=cur.next
        yield cur.item
    def add(self,item):
        '''头部增加节点'''
        node=Node(item)
        if self.is_empty():
            self._head=node
            node.next=self._head
        else:
            node.next=self._head
            cur=self._head
            while cur.next!=self._head:
                cur=cur.next
            cur.next=node
        self._head=node
    def append(self,item):
        """尾部"""
        node=Node(item)
        if self.is_empty():
            self._head=node
            node.next=self._head
        else:
            cur=self._head
            while cur.next!=self._head:
                cur=cur.next
            cur.next=node
            node.next=self._head
    def insert(self,index,item):
        if index<=0:
            self.add(item)
        elif index>self.length()-1:
            self.append(item)
        else:
            node=Node(item)
            cur=self._head
            for i in range(index-1):
                cur=cur.next
            node.next=cur.next
            cur.next=node
    def remove(self,item):
        if self.is_empty():
            return
        cur=self._head
        pre=None
        '''如果第一个就是要删的'''
        if cur.item==item:
            #链表不止一个元素
            if cur.next!=self._head:
                while cur.next!=self._head:
                    cur=cur.next
                cur.next=self._head.next
                self._head=self._head.next
            else:
                self._head=None
        else:
            pre=self._head
            while cur.next!=self._head:
                if cur.item==item:
                    pre.next=cur.next
                    return True
                else:
                    pre=cur
                    cur=cur.next
        #删除的是最后一个
        if cur.item==item:
            pre.next=self._head
            return True
    def find(self,item):
        return item in self.items()

if __name__ == '__main__':
    link_list = SingleCycleLinkList()
    print(link_list.is_empty())
    # 头部添加元素
    for i in range(5):
        link_list.add(i)
    print(list(link_list.items()))
    # 尾部添加元素
    for i in range(6):
        link_list.append(i)
    print(list(link_list.items()))
    # 添加元素
    link_list.insert(3, 45)
    print(list(link_list.items()))
    print(link_list.length())
    print('*'*50)
    # 删除元素
    link_list.remove(5)
    print(list(link_list.items()))
    # 元素是否存在
    print(5 in link_list.items())