class Queue:
    class Node:
        def __init__(self, data: int):
            self.data: int = data
            self.next = None
    
    def __init__(self):
        self._head = None
        self._tail = None

    def isEmpty(self) -> bool:
        return self._head is None

    def peek(self) -> int:
        return self._head.data

    def add(self, data: int):
        node_to_add = self.Node(data)
        if(self._tail is not None):
            self._tail.next = node_to_add
        self._tail = node_to_add
        if(self._head is None):
            self._head = node_to_add

    def remove(self) -> int:
        data = self._head.data
        self._head = self._head.next
        if(self._head is None):
            self._tail = None
        return data
    
    def printQueue(self):
        value_to_print = self._head
        while(value_to_print is not None):
            print(value_to_print.data)
            value_to_print = value_to_print.next



if __name__ == "__main__":
    r = Queue()
    print(r.isEmpty())
    r.add(2)
    r.add(4)
    r.add(12)
    r.add(-4)
    r.printQueue()
    print("_____")
    print(r.peek())
    print("_____")
    r.remove()
    r.printQueue()

    