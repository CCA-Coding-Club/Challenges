import node_code as nd
class Linked_list:
    def __init__(self):
        self.first_node = None
        self.last_node = None

    def append_node(self, value):
        new_node = nd.Node(value)
        if self.first_node == None:
            self.first_node = new_node
            self.last_node = new_node
        else:
            new_node.set_prev_node(self.last_node)
            self.last_node.set_next_node(new_node)
            self.last_node = new_node
            
    def find(self, string_to_find):
        i = 1
        current_node = self.first_node
        while current_node:
            if str(current_node.get_value()) == string_to_find:
                print(f"value {string_to_find} is located within the node at index {i}")
                return 1
            current_node = current_node.get_next_node()
            i += 1
        print("That don't exist homedog")

my_ll = Linked_list()
my_ll.append_node('dog')
my_ll.find('dog')
my_ll.append_node('cat')
my_ll.append_node('lizard')
my_ll.append_node('hamster')
my_ll.find('hamster')