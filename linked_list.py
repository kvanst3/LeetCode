class Node():

    def __init__(self, val):
        self.value = val
        self.next = None

class MyLinkedList():

    def __init__(self):
        self.head = None
        self.size = 0

    def AddAtTail(self, val):
        new_node = Node(val)
        curr = self.head
        if curr == None:
            self.head = new_node
        else:
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
        self.size += 1

    def AddAtHead(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

        self.size += 1
        

