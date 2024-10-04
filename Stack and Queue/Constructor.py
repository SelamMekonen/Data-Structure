class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Stack:  
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.length = 1
        
    
    def print_list(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def push(self, value):
        
        new_node = Node(value)
        
        if self.length == 0:
            self.top = new_node
        
        else:
            new_node.next = self.top
            self.top = new_node
            
        self.length +=1
        
    def pop(self):
        
        if self.length == 0:
            return None
        
        
        temp = self.top
        self.top = self.top.next
            
        temp.next = None
        
        self.length -=1
        
        return temp.value
    
    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        
        return self.top.value
    
    def isEmpty(self):
        return self.length == 0
    
    def stackSize(self):
        return self.length
    
   
            

my_stack = Stack(7)

my_stack.push(23)
my_stack.push(3)
my_stack.push(11)
my_stack.print_list()       

print(my_stack.pop())
print(my_stack.stackSize)
print(my_stack.peek)
print(my_stack.isEmpty)

