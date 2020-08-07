class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: Node = None

    

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data: int):
            if(self.head is None):
                self.head = Node(data)
                return

            current_node = self.head
            while(current_node.next is not None):
                current_node = current_node.next
            current_node.next = Node(data)
    
    def prepend(self, data: int):
        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head

    def deleteWithValue(self, data: int):
        if(self.head is None): return
        if(self.head.data == data):
            self.head = self.head.next

        current_node = self.head
        while(current_node.next is not None):
            if(current_node.next.data == data):
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
    
    def toString(self):
        print_value = self.head
        while(print_value is not None):
            print(print_value.data)
            print_value = print_value.next

if __name__ == "__main__":
    r = LinkedList()
    r.head = Node(3)
    r.append(1)
    r.append(2)
    r.toString()
    print("_____")
    r.prepend(12)
    r.toString()
    print("_____")
    r.deleteWithValue(3)
    r.toString()