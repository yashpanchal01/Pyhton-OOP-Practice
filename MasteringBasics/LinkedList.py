# --- Step 1: Define the Node class first ---
# This is the building block. The LinkedList class needs to know what a Node is.
class Node:
    """An object for storing a single node of a linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None  # The pointer to the next node

# --- Step 2: Define the LinkedList class that USES the Node class ---
class LinkedList:
    """Manages the collection of nodes."""
    def __init__(self):
        self.head = None  # The list is initially empty

    def print_list(self):
        """Traverses and prints the list."""
        current_node = self.head
        nodes = []
        while current_node:
            nodes.append(str(current_node.data))
            current_node = current_node.next
        print(" -> ".join(nodes))

    def append(self, data):
        """Adds a new node to the end of the list."""
        # Here is where the error happens if Node is not defined
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        
        last_node.next = new_node

    def prepend(self, data):
        """Adds a new node to the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

# --- Step 3: Now you can use the LinkedList class ---
# Create a new linked list
llist = LinkedList()

# Append some values
llist.append("A")
llist.append("B")
llist.append("C")

print("After appending:")
llist.print_list()

# Prepend a value
llist.prepend("START")
print("\nAfter prepending:")
llist.print_list()