# Linked List data structure implementation using Custom Node data structure


class CustomNode:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, item):
        self.data = item

    def get_next(self):
        return self.next

    def set_next(self, item):
        self.next = item


class CustomLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        node = CustomNode(item)
        node.set_next(self.head)
        self.head = node

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None:
            if current.get_data() is item:
                found = True
                break
            current = current.get_next()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current is not None:
            if current.get_data() == item:
                found = True
                break
            else:
                previous = current
                current = current.get_next()
        if found:
            previous.set_next(current.get_next())
        elif previous is None:
            self.head = current.get_next()


if __name__ == '__main__':
    nodeObj = Node(100)
    # listObj = LinkedList()
    # print(nodeObj.get_data())
    # print(nodeObj.get_next())
    # listObj.add(200)
    # listObj.add(300)
    # listObj.add(400)
    # listObj.add(500)
    # listObj.add(600)
    # print(listObj.search(200))
