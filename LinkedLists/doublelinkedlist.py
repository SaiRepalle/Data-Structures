class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList(object):

    def __init__(self):
        self._count = 0
        self.root = None
        self.tail = None

    def insert(self, data, pos=None):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            self.tail = new_node
        else:
            # insert at the end
            if pos is None:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
            else:
                # insert in the middle of the position
                temp_count = 0
                curr_head = self.root
                while curr_head is not None:
                    if pos == temp_count:
                        break
                    curr_head = curr_head.next
                    temp_count += 1
                new_node.prev = curr_head
                new_node.next = curr_head.next
                curr_head.next = new_node

        self._count += 1

    def __iter__(self):
        temp_node = self.root

        while temp_node is not None:
            yield temp_node
            temp_node = temp_node.next


    def __str__(self):
        output = ""
        for i in self:
            output += f"{str(i.data)}-->"

        return output

    def __len__(self):
        return self._count




## test
a = DoubleLinkedList()
a.insert(100)
a.insert(90)
a.insert(80)
a.insert(70)
a.insert(60)
print(a)
a.insertion_sort()
print(a)



