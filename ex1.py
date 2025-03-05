class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None
    

class Stack:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None
    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            print("\nStack Underflow")
        else:
            temp = self.head
            self.head = self.head.next
            del temp

def main():
    user_input = input()

if __name__ == "__main__":
    main()