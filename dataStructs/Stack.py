class Stack:
    class Node:
        def __init__(self, data: int):
            self.data = data
            self.next = None
    
    def __init__(self):
        self.top= None

    def isEmpty(self) -> bool:
        return self.top is None

    def peek(self) -> int:
        return self.top.data

    def push(self, data: int):
        node = self.Node(data)
        node.next = self.top
        self.top = node

    def pop(self) -> int:
        if(self.isEmpty()):
            raise TypeError("Stack is Empty")
        data = self.top.data
        self.top = self.top.next
        return data

    def print_values(self):
        value_to_print = self.top
        while(value_to_print is not None):
            print(value_to_print.data)
            value_to_print = value_to_print.next

if __name__ == "__main__":
    r = Stack()
    print(r.isEmpty())
    r.push(1)
    r.push(2)
    print(r.peek())
    print("_____")
    r.push(113)
    r.push(13)
    r.print_values()
    print("_____")
    r.pop()
    r.print_values()


