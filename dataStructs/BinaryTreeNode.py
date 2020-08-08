class TreeNode:
    def __init__(self, data: int):
        self.left_node: TreeNode = None
        self.right_node: TreeNode = None
        self.data: int = data

    def insert(self, value: int):
        if(value <= self.data):
            if(self.left_node == None):
                self.left_node = TreeNode(value)
            else:
                self.left_node.insert(value)
        else:
            if(self.right_node == None):
                self.right_node = TreeNode(value)
            else:
                self.right_node.insert(value)

    def contains(self, value: int) -> bool:
        if(value == self.data):
            return True
        elif(value < self.data):
            if(self.left_node == None):
                return False
            else:
                return self.left_node.contains(value)
        else:
            if(self.right_node == None):
                return False
            else:
                return self.right_node.contains(value)

    def printInOrder(self):
        if(self.left_node != None):
            self.left_node.printInOrder()
        print(self.data)
        if(self.right_node != None):
            self.right_node.printInOrder()

if __name__ == "__main__":
    r = TreeNode(10)
    r.insert(5)
    r.insert(7)
    r.insert(7)
    r.insert(17)
    r.printInOrder()

