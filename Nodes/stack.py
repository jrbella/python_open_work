from node import Node

class Stack:
    def __init__(self, name):
        self.size = 0
        self.top_item = None
        self.name = name
        self.limit = 1000


        def push(self, value):
            if has_space():
                item = Node(value)
                item.set_next_node(self.top_item)
                self.top_item = item
            else:
                print("stack is full")


        def pop(self):
            if check_stack():
                item_to_remove = self.top_item
                self.top_item = item_to_remove.get_next_node()
                self.size -= 1
                return item_to_remove.get_value()
            print("This stack is empty")

        def peek(self):
            if check_stack():
                return self.top_item.get_value()
            print("Nothing on the stack to see")


        #Helper function
        def check_stack(){
            if self.size > 0:
                return True 
        }

        def has_space(self):
            return self.limit > self.size