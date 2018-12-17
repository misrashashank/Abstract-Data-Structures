# Dequeue data structure implementation using List data structure


class ListDequeue:
    def __init__(self):
        self.op_array = []

    def add_front(self, item):
        self.op_array.append(item)

    def add_rear(self, item):
        self.op_array.insert(0, item)

    def remove_front(self):
        return self.op_array.pop()

    def remove_rear(self):
        return self.op_array.pop(0)

    def is_empty(self):
        return self.op_array == []

    def size(self):
        return len(self.op_array)

    def dq_print(self):
        print(self.op_array)

    def check_palindrome(self, subject):
        dq_obj = ListDequeue()
        for item in subject:
            dq_obj.add_rear(item)
        flag = 0
        while dq_obj.size() > 1:
            if dq_obj.remove_front() != dq_obj.remove_rear():
                flag = 1
                break
        return False if flag == 1 else True


if __name__ == '__main__':
    main_obj = ListDequeue()
    main_obj.add_rear(4)
    main_obj.dq_print()
    main_obj.add_rear('dog')
    main_obj.dq_print()
    main_obj.add_front('cat')
    main_obj.dq_print()
    main_obj.add_front(True)
    main_obj.dq_print()
    main_obj.add_rear(8.4)
    main_obj.dq_print()
    print(main_obj.size())
    print(main_obj.is_empty())
    main_obj.remove_rear()
    main_obj.remove_front()
    main_obj.dq_print()
    print(main_obj.check_palindrome("hdeedh"))
