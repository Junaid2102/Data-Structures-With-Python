class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            # add data in left subtreee
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []
        # Visit left tree
        if self.left:
            elements += self.left.in_order_traversal()
        # Visit base node
        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements

    def search(self, value):
        if self.data == value:
            print(f"You entered {value} and it is found");
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum
    def delete(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right

            min_value = self.right.find_min()
            self.data = min_value
            self.right = self.right.delete(min_value)
        return self



def build_tree(elements):
    root = BinarySearchTreeNode(elements[6])
    for i in range (1, len(elements)):
        root.add_child(elements[i])

    return root

numbers = [17, 4, 1, 20, 9, 23, 18, 34]
numbers_tree = build_tree(numbers)
print("In order Traversal: ", numbers_tree.in_order_traversal())
print("Pre order Traversal: ", numbers_tree.pre_order_traversal())
print("Post order Traversal: ", numbers_tree.post_order_traversal())
print(numbers_tree.search(20))
print("Min: ", numbers_tree.find_min())
print("Max: ", numbers_tree.find_max())
print("Before deletion Sum: ", numbers_tree.calculate_sum())
numbers_tree.delete(20)
print("After Deleting: ", numbers_tree.in_order_traversal())
print("Sum: ", numbers_tree.calculate_sum())