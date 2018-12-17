# Stack data structure implementation using List data structure


class ListStack:
    def __init__(self):
        self.op_array = []

    def is_empty(self):
        return self.op_array == []

    def push(self, item):
        return self.op_array.append(item)

    def pop(self):
        return self.op_array.pop()

    def peek(self):
        return self.op_array[len(self.op_array) - 1]

    def size(self):
        return len(self.op_array)

    def print(self):
        print()

    def reverse_string(self, target_string):
        stack_obj = ListStack()
        for item in target_string:
            stack_obj.push(item)
        reverse_string = ""
        while not stack_obj.is_empty():
            reverse_string = reverse_string + stack_obj.pop()
        return reverse_string


if __name__ == '__main__':
    main_obj = ListStack()
    print(main_obj.is_empty())
    main_obj.push(4)
    main_obj.push('dog')
    print(main_obj.peek())
    main_obj.push(True)
    print(main_obj.size())
    print(main_obj.is_empty())
    main_obj.push(8.4)
    print(main_obj.pop())
    print(main_obj.pop())
    print(main_obj.size())
    print(main_obj.reverse_string("hello"))
