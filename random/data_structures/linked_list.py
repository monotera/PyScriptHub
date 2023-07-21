"""
Created on Sat Oct 23 19:38:17 2021

@author: Nelson Mosquera (Monotera)

@Theory Taken from: www.geeksforgeeks.org

Linked list
A linked list is represented by a pointer to the first node of the linked list. 
The first node is called the head. If the linked list is empty, then the value 
of the head is NULL. 
Each node in a list consists of at least two parts: 
    -data
    -Pointer to the next node
Pros:
    -Dynamic size 
    -Ease of insertion/deletion
Cons:
    -Random access is not allowed

Time Complexity:
    -Access: O(n)
    -Search: O(n)
    -Insertion: O(1)
    -Deletion: O(1)
    -Indexing: O(n)
    
Space Complexity: O(n)

TAD LinkedList:
    head = represents first node
    isEmpty()
    size()
    push(data) = adds a new node in the head
    append(data) = adds a new node in the tail
    insert(pos,data)
    delete(pos)
    empty() = deletes all elements
    print()
    reverse()
    

Print():
    -Traverse the linked list until you find a None value
    -In each iteration print the value and update the node
isEmpty():
    -check if the head is None
size():
    -Initialize counter in 0
    -Initialize a node pointer, current = head.
    -Do following while current is not NULL:
        -current = current -> next
        -counter + 1
    -Return counter

    
"""


class Node:
    # Initialize node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    # Initialize linkedlist
    def __init__(self):
        self.head = None

    def print_list(self):
        temp_node = self.head
        while temp_node != None:
            print(temp_node.data, " -> ", end="")
            temp_node = temp_node.next
        print("")

    def isEmpty(self):
        return self.head == None

    def size(self):
        counter = 0
        temp_node = self.head
        while temp_node != None:
            temp_node = temp_node.next
            counter += 1
        return counter

    def delete(self, pos):
        if pos < 0 and self.size():
            return False
        i = 0
        temp_node = self.head
        if pos == 0:
            self.head = temp_node.next
            del temp_node
            return True

        while temp_node != None:
            if pos - 1 == i:
                deleted_node = temp_node.next
                temp_node.next = deleted_node.next
                del deleted_node
                return True
            i += 1
            temp_node = temp_node.next

    def reverse(self):
        # Check if there is only one node
        if self.head.next == None:
            return
        # Reverse list will store the head of our temp reverse list
        reverse_list = self.head
        # temp is the next node of the current element before it goes to the reverse list
        temp = reverse_list.next
        # Starts the reverse lise
        reverse_list.next = None
        # Current is the current node
        current = temp
        while current != None:
            """
            Checks if the node is the tail:
                -if is the tail then append the reverse list to this node and
                put this node as the new head of the list
                -if its not the tail:
                    -Save the next node of the current node in temp
                    -append to the current node the reverse list
                    -update the head of the reverse list
                    -update current with the saved temp (temp will have the original list)
            """
            if current.next == None:
                current.next = reverse_list
                self.head = current
                break
            temp = current.next
            current.next = reverse_list
            reverse_list = current
            current = temp

    def deleteAll(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        temp_node = self.head
        while temp_node != None:
            if temp_node.next == None:
                old_node = temp_node.next
                temp_node.next = new_node
                new_node.next = old_node
            temp_node = temp_node.next

    def insert(self, pos, data):
        new_node = Node(data)
        i = 0
        temp_node = self.head
        # Check if the position is valid
        if pos < 0 and pos > self.size():
            return False

        # Special case if the new node is the new head
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return True

        while temp_node != None:
            if pos - 1 == i:
                old_node = temp_node.next
                temp_node.next = new_node
                new_node.next = old_node
                return True
            i += 1
            temp_node = temp_node.next
        return False


# Code execution starts here
if __name__ == "__main__":
    # Start with the empty list
    my_list = LinkedList()

    my_list.head = Node(1)
    second = Node(2)
    third = Node(3)

    """
    Three nodes have been created.
    We have references to these three blocks as head,
    second and third
 
    my_list.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  | None |     | 2  | None |     |  3 | None |
    +----+------+     +----+------+     +----+------+
    """

    my_list.head.next = second
    # Link first node with second

    """
    Now next of first Node refers to second.  So they
    both are linked.
 
    my_list.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  |  o-------->| 2  | null |     |  3 | null |
    +----+------+     +----+------+     +----+------+
    """

    second.next = third
    # Link second node with the third node

    """
    Now next of second Node refers to third.  So all three
    nodes are linked.
 
    my_list.head        second              third
         |                |                  |
         |                |                  |
    +----+------+     +----+------+     +----+------+
    | 1  |  o-------->| 2  |  o-------->|  3 | null |
    +----+------+     +----+------+     +----+------+
    """
    """
    Testing of functions 
    """
    new = LinkedList()
    new.push(0)
    new.push(1)
    new.print_list()
    new.reverse()
    new.print_list()
    my_list.print_list()
    print(my_list.isEmpty())
    print(my_list.size())
    my_list.insert(0, 0)
    my_list.print_list()
    my_list.insert(1, 88)
    my_list.print_list()
    my_list.insert(5, 100)
    my_list.print_list()
    my_list.push(-1)
    my_list.print_list()
    my_list.append(-1)
    my_list.print_list()
    my_list.delete(0)
    my_list.print_list()
    my_list.delete(my_list.size() - 1)
    my_list.print_list()
    my_list.delete(2)
    my_list.print_list()
    my_list.reverse()
    my_list.print_list()
