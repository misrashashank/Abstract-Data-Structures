# Queue data structure implementation using List data structure


class ListQueue:
    def __init__(self):
        self.op_array = []

    def enqueue(self, item):
        self.op_array.insert(0, item)

    def dequeue(self):
        self.op_array.pop()

    def is_empty(self):
        return self.op_array == []

    def size(self):
        return len(self.op_array)

    def __str__(self):
        print()

    def hot_potato(self, names, num):
        obj = ListQueue()
        for item in names:
            obj.enqueue(item)
        while obj.size() > 1:
            for item in range(num):
                obj.enqueue(obj.dequeue())
            obj.dequeue()
        return obj.dequeue()


if __name__ == '__main__':
    main_obj = MyQueue()
    main_obj.enqueue("Bill")
    main_obj.enqueue("David")
    main_obj.enqueue("Susan")
    main_obj.enqueue("Jane")
    main_obj.enqueue("Kent")
    main_obj.enqueue("Brad")
    print(main_obj.hot_potato(["Bill", "David", "Susan", "Jane", "Brad"], 7))
