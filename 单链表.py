'''1.定义节点'''
'''节点的数据结构为数据元素item和指针next'''
class Node(object):
    def __init__(self,item):
        self.item=item
        '''next是下一个节点的标识'''
        self.next=None

class SingleLinkList(object):
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
        '''遍历列表'''
        cur=self._head
        print(type(cur))
        while cur is not None:
            yield cur.item
            cur=cur.next
    def add(self,item):
        '''链表头部增加元素'''
        node=Node(item)
        node.next=self._head
        self._head=node
    def append(self,item):
        '''尾部增加'''
        node=Node(item)
        if self.is_empty():
            self._head=node
        else:
            cur=self._head
            while cur.next is not None:
                cur=cur.next
            cur.next=node
    def insert(self,index,item):
        """指定位置插入"""
        if index==0:
            self.add(item)
        if index>(self.length()-1):
            self.append(item)
        else:
            node=Node(item)
            cur=self._head
            for i in range(index-1):
                cur=cur.next
            node.next=cur.next
            cur.next=node
    def remove(self,item):
        cur=self._head
        pre=None
        while cur is not None:
            #找到指定元素
            if cur.item==item:
                #如果第一个就是要删除的
                if not pre:
                    self._head=cur.next
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next=cur.next
                return True
            else:
                pre=cur
                cur=cur.next
    def find(self,item):
        return item in self.items()

'''举例'''
if __name__=='__main__':
    link_list=SingleLinkList()
    for i in range(5):
        link_list.append(i)
    link_list.add(6)
    for i in link_list.items():
        print(i)
    link_list.insert(3,9)
    print(list(link_list.items()))
    link_list.remove(0)
    print(link_list.find(4))