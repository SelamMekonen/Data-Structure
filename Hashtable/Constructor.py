class HashTable:
    
    def __init__(self, size = 7):
        self.datamap = [None] * 7
        
    
    def __hash(self,key):
        my_hash = 0
        
        for letter in key:
            my_hash = (my_hash + ord(letter)*23) % len(self.datamap)
        return my_hash
    
    def print_table(self):
        for i,val in enumerate(self.datamap):
            print(i, ":", val) 
            

my_hash_table = HashTable()
my_hash_table.print_table()
        
        
        
