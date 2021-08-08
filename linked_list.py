class Node():

    def __init__(self, val: int):
        self.value = val
        self.next = None

class MyLinkedList():

    def __init__(self):
        self.head = None
        self.size = 0

    def AddAtTail(self, val: int):
        new_node = Node(val)
        curr = self.head
        if curr == None:
            self.head = new_node
        else:
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
        self.size += 1

    def AddAtHead(self, val: int):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

        self.size += 1

    def get(self, index: int):
        if index < 0 or index >= self.size:
            return -1
        if self.head is None:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.value

    def addAtIndex(self, index: int, val: int):
        """
        Add a node of value val before the index-th node in the linked list. 
        If index equals to the length of linked list, the node will be appended to the end of linked list. 
        If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index >= self.size:
            return 
        if index == 0:
            self.AddAtHead(val)
        elif index + 1 == self.size:
            self.AddAtTail(val)
        else:
            curr = self.head
            for _ in index -1:
                curr = curr.next
            new_node = Node(val)
            new_node.next = curr.next
            curr.next = new_node
            self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """