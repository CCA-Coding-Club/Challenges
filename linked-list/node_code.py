class Node:
    def __init__(self, value, previous=None, next=None):
        self.value = value
        self.next = next
        self.previous = previous
    
    def __str__(self):
        return 'Congrats this class can make a node. It also is a node.'

    def set_next_node(self, next):
        self.next = next
    
    def get_next_node(self):
        return self.next

    def set_prev_node(self, previous):
        self.previous = previous

    def get_prev_node(self):
        return self.previous
    
    def get_value(self):
        return self.value
