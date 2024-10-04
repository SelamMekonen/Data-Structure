class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class Linkedlist:
    def __init__(self,value):
        self.newnode = Node(value)
        self.head = self.newnode
        self.tail = self.newnode
        self.length = 1

# --------------------------------------------------Print--------------------------------------------------------#    
    def print_(self):
        self.temp = self.head
        
        while self.temp is not None:
            print(self.temp.value)
            self.temp = self.temp.next

# --------------------------------------------------Append--------------------------------------------------------#
   
    def append(self,value):
        newnode = Node(value)
        
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode
            self.length+=1
        
        return True
 
# --------------------------------------------------Pop--------------------------------------------------------#
   
    def pop(self):
        if self.head is None:
            return None
       
        else:
            temp = self.head
            pre = self.head
            
            while temp.next is not None:
                pre = temp
                temp = temp.next
            
            self.tail = pre
            self.tail.next = None
            self.length -=1
            
            if self.length == 0:
                self.head = None
                self.tail = None
            
            return temp
        
 
# --------------------------------------------------Append--------------------------------------------------------#
   
    def prepend(self,value):
        
        newnode = Node(value)
        
        if self.length == 0:
            self.head = newnode
            self.tail = newnode
        
        else:
            newnode.next = self.head
            self.head = newnode
        
        self.length +=1
        return True
    
# --------------------------------------------------Popfirst--------------------------------------------------------#    

    
    def Popfirst(self):
        if self.length == 0:
            return None
        
        elif self.length == 1:
            self.head = None
            self.tail = None
        
        else:
            temp = self.head
            self.head = self.head.next
            
            temp.next = None
        self.length -=1
        if self.length == 0:
                self.head = None
                self.tail = None
        return temp
    
# --------------------------------------------------Get--------------------------------------------------------#    
    
    def get(self, index):
        
        if index <0 or index>=self.length:
            return False
        
        else:
            temp = self.head
            
            for _ in range(index):
                temp = temp.next
            
            return temp

# --------------------------------------------------Set_value--------------------------------------------------------#    

    def set_value(self,index,value):
        
        temp = self.get(index)
        
        if temp:
            temp.value = value
            return True
        
        return False

# --------------------------------------------------Insert_value--------------------------------------------------------#    
    
    def insert_value(self, index, value):
        
        pre = self.get(index-1) 
        
        if (pre):
            temp = pre.next
            new_node = Node(value)
            
            pre.next = new_node
            new_node.next = temp
        
        else:
            return False

# --------------------------------------------------Remove_value--------------------------------------------------------#    
    
    def remove_item(self, index):
        if index<0 or index>=self.length:
            return None
        
        elif index == 0:
            return self.Popfirst()
        
        elif index == self.length-1:
            return self.pop()
        
        else:
            pre = self.get(index-1)  
            temp = pre.next
            
            pre.next = temp.next
            temp.next = None 
        
        self.length -=1
        return True  

# --------------------------------------------------Reverse--------------------------------------------------------#    


    def reverse(self):
        
        temp = self.head
        self.head = self.tail
        self.tail = temp
        
        after = temp.next
        before = None
        
        
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
            

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
              

                        

my_linklist = Linkedlist(0)

# my_linklist.print_()

# --------------------------------------------------Append--------------------------------------------------------#
my_linklist.append(1)
my_linklist.append(2)
my_linklist.append(3)


# --------------------------------------------------Pop--------------------------------------------------------#

# # 2 Item
# print(my_linklist.pop())
# # 1 Item
# print(my_linklist.pop())
# # 0 Item
# print(my_linklist.pop())


# --------------------------------------------------Prepend--------------------------------------------------------#

# my_linklist.prepend(1)
# my_linklist.print_()

# --------------------------------------------------Pop_first--------------------------------------------------------#
# print(my_linklist.Popfirst())

# --------------------------------------------------Get--------------------------------------------------------#    

# print(my_linklist.get(2))

# --------------------------------------------------Set_value--------------------------------------------------------#    

# my_linklist.set_value(2,6)
# my_linklist.print_()

# print(" ---*--- " *8)

# --------------------------------------------------Insert_value--------------------------------------------------------#    


# my_linklist.insert_value(2,6)
# my_linklist.print_()

# print(" ---*--- " *8)

# --------------------------------------------------Remove_value--------------------------------------------------------#    
 
# my_linklist.remove_item(2)
my_linklist.print_()
    
# --------------------------------------------------Remove_value--------------------------------------------------------#    
     
print(" ---*--- " *8)
my_linklist.reverse()
my_linklist.print_()


        