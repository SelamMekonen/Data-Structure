class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    
    # def is_a_Palindrome(self):
    #     first = self.head
    #     last = self.tail
        
    #     for _ in range(self.length):
    #         if first.value != last.value:
    #             print('Not palindrome')
    #             break 
            
    #         else:
    #             first = first.next
    #             last = last.prev
            
    #         print("A palindrome")
    
    def swap_pairs(self):
        point1 = self.head
        point2 = point1.next
        
        while point1.next.next is not None:
            point1.value, point2.value = point2.value, point1.value
            
            point1 = point1.next.next
            point2 = point2.next.next
        
        return True
    


my_dll = DoublyLinkedList(1)
my_dll.append(2)
my_dll.append(3)
my_dll.append(4)

print('my_dll before swap_pairs:')
my_dll.print_list()

my_dll.swap_pairs() 


print('my_dll after swap_pairs:')
my_dll.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    my_dll before swap_pairs:
    1
    2
    3
    4
    my_dll after swap_pairs:
    2
    1
    4
    3

"""
        
                
                