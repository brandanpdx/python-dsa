# This class helps methods in the LinkedList class make new nodes
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    # Creates new Node
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # Method to see all Nodes in a Linked List
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # Creates new Node, adds Node to end
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    # Removes the last node from the Linked List and returns its value
    def pop(self):
        # If Linked List is empty, return None
        if self.length == 0:
            return None

        # Otherwise, set temp and pre to head
        temp = self.head
        pre = self.head

        # If the current Node has a Next value, set pre to that value, and temp advances to the next node
        while (temp.next):
            pre = temp
            temp = temp.next

        # When the above loop returns false, set the tail to that second-to-last node and remove the reference to the last node
        self.tail = pre
        self.tail.next = None

        # Decrease the length of the Linked List by 1
        self.length -= 1

        # If the Linked List is now empty, set the head and tail to None
        if self.length == 0:
            self.head = None
            self.tail = None

        # Return the value of the removed node
        return temp.value

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node


my_linked_list = LinkedList(1)
my_linked_list.append(2)

print(my_linked_list.pop())
print(my_linked_list.pop())
print(my_linked_list.pop())
