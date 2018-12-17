# Tree data structure implementation using List data structure


class ListTree:
    def binary_tree(self, root):
        return [root, [], []]

    def insert_left(self, target_tree, element):
        left = target_tree.pop(1)
        if len(left) > 1:
            target_tree.insert(1, [element, left, []])
        else:
            target_tree.insert(1, [element, [], []])

    def insert_right(self, target_tree, element):
        right = target_tree.pop(2)
        if len(right) > 1:
            target_tree.insert(2, [element, [], right])
        else:
            target_tree.insert(2, [element, [], []])

    def get_root_value(self, target_tree):
        return target_tree.pop(0)

    def set_root_value(self, target_tree, value):
        target_tree[0] = value

    def get_left_child(self, target_tree):
        return target_tree[1]

    def get_right_child(self, target_tree):
        return target_tree[2]


if __name__ == '__main__':
    main_obj = ListTree()
    main_tree = main_obj.binary_tree('a')
    main_obj.insert_left(main_tree, 'b')
    main_obj.insert_right(main_tree, 'c')
    main_obj.insert_left(main_tree, 'd')
    print(main_obj.get_left_child(main_tree))
    print(main_obj.get_right_child(main_tree))
    main_obj.set_root_value(main_tree, 'g')
    print(main_obj.get_root_value(main_tree))
