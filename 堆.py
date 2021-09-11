class heap(object):
    import heapq
    def __init__(self):
        self.data_list=[]

    def get_parent_index(self,index):
        if index==0 or index>len(self.data_list)-1:
            return None
        else:
            return (index-1)>>1 #父节点下标

    def swap(self,index_a,index_b):
        self.data_list[index_a],self.data_list[index_b]=self.data_list[index_b],self.data_list[index_a]

    def insert(self,data):
        #元素放到最后，以大顶堆为例 如果插入元素比父节点大，则交换
        self.data_list.append(data)
        index=len(self.data_list)-1
        parent=self.get_parent_index(index)
        while parent is not None and self.data_list[parent]>self.data_list[index]:
            # 循环，直到该元素成为堆顶，或小于父节点（对于大顶堆)
            self.swap(parent,index)
            index=parent
            parent=self.get_parent_index(parent)

    def removemax(self):
        remove_data=self.data_list[0]
        self.data_list[0]=self.data_list[-1]
        del self.data_list[-1]

    def heapify(self, index):
        # 从上往下堆化，从index 开始堆化操作 (大顶堆)
        total_index = len(self.data_list) - 1
        while True:
            maxvalue_index = index
            if 2 * index + 1 <= total_index and self.data_list[2 * index + 1] > self.data_list[maxvalue_index]:
                maxvalue_index = 2 * index + 1
            if 2 * index + 2 <= total_index and self.data_list[2 * index + 2] > self.data_list[maxvalue_index]:
                maxvalue_index = 2 * index + 2
            if maxvalue_index == index:
                break
            self.swap(index, maxvalue_index)
            index = maxvalue_index