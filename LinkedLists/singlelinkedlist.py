class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList(object):
    def __init__(self):
        self._count = 0
        self.root = None
        self.tail = None

    def __len__(self):
        return self._count

    def insert(self, data, pos=None):
        pass
