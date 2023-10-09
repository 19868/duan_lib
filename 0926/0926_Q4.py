class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # 在链表末尾插入元素
    def append(self, data):
        new_node = Node(data)

        if not self.head:  # 链表为空
            self.head = new_node
        else:  # 链表不为空
            current = self.head
            while current.next:  # 下一节点不为空则不断循环，直至尾部
                current = current.next
            current.next = new_node

    # 删除指定元素
    def delete(self, data):
        if not self.head:  # 链表为空，无法删除
            return

        if self.head.data == data:  # 链表头部为空，则直接去除
            self.head = self.head.next
            return

        current = self.head  # 从头部开始遍历
        while current.next:
            if current.next.data == data:  # 找到该元素，将其去除
                current.next = current.next.next
                return
            current = current.next

    # 修改指定位置的元素值
    def update(self, index, data):
        if not self.head or index < 0:  # 链表为空或下标为负，则无法更改
            return

        current = self.head
        i = 0
        while current:
            if i == index:
                current.data = data
                return
            current = current.next
            i += 1

    # 查找指定元素的位置
    def find(self, data):
        if not self.head:
            return -1

        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1

        return -1

    # 打印链表
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


# 创建链表对象
linked_list = LinkedList()

# 向链表末尾插入元素
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

# 打印链表：1 2 3
linked_list.display()

# 删除指定元素
linked_list.delete(2)

# 打印链表：1 3
linked_list.display()

# 修改指定位置的元素值
linked_list.update(1, 4)

# 打印链表：1 4
linked_list.display()

# 查找指定元素的位置
index = linked_list.find(4)
print("Index of 4:", index)  # 输出：Index of 4: 1
