class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_recursive(data, self.root)

    def insert_recursive(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.insert_recursive(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self.insert_recursive(data, node.right)

    def search(self, data):
        return self.search_recursive(data, self.root)

    def search_recursive(self, data, node):
        if node is None:
            return False
        if data == node.data:
            return True
        elif data < node.data:
            return self.search_recursive(data, node.left)
        else:
            return self.search_recursive(data, node.right)

    def pre_order(self):
        result = []
        self.pre_order_recursive(self.root, result)
        return result

    def pre_order_recursive(self, node, result):
        if node:
            result.append(node.data)
            self.pre_order_recursive(node.left, result)
            self.pre_order_recursive(node.right, result)

    def inorder(self):
        result = []
        self.inorder_recursive(self.root, result)
        return result

    def inorder_recursive(self, node, result):
        if node:
            self.inorder_recursive(node.left, result)
            result.append(node.data)
            self.inorder_recursive(node.right, result)

    def postOrder(self):
        result = []
        self.postOrder_recursive(self.root, result)
        return result

    def postOrder_recursive(self, node, result):
        if node:
            self.postOrder_recursive(node.left, result)
            self.postOrder_recursive(node.right, result)
            result.append(node.data)




t = BinaryTree()
t.insert(10)
t.insert(5)
t.insert(15)
t.insert(2)

print(t.search(15))  
print(t.search(7))   
print(t.pre_order())
