# Binary Tree data structure implementation using Custom nodes


class BinaryTree:
    def __init__(self, value):
        self.key = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        if self.left_child is not None:
            new_node = BinaryTree(value)
            new_node.left_child = self.left_child
            self.left_child = new_node
        else:
            self.left_child = BinaryTree(value)

    def insert_right(self, value):
        if self.right_child is not None:
            new_node = BinaryTree(value)
            new_node.right_child = self.right_child
            self.right_child = new_node
        else:
            self.right_child = BinaryTree(value)

    def get_root_value(self):
        return self.key

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def set_root_value(self, value):
        self.key = value


if __name__ == '__main__':
    main_obj = BinaryTree('a')
    # print(main_obj.get_root_value())
    # print(main_obj.get_left_child())
    # main_obj.insert_left('b')
    # print(main_obj.get_left_child())
    # print(main_obj.get_left_child().get_root_value())
    # main_obj.insert_right('c')
    # print(main_obj.get_right_child())
    # print(main_obj.get_right_child().get_root_value())
    # main_obj.get_right_child().set_root_value('hello')
    # print(main_obj.get_right_child().get_root_value())
