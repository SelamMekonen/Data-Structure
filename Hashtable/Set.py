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
            
    
    def set_item(self,key, value):
        index = self.__hash(key)
        if self.datamap[index] == None:
            self.datamap[index] = []
        
        self.datamap[index].append([key, value])
        
    
    
    def get_item(self,key):
        index= self.__hash(key)
        
        if self.datamap[index] is not None:
            for i in range(len(self.datamap[index])):
                if self.datamap[index][i][0] == key:
                    return self.datamap[index][i][1]
        
        return None
    
    def keys(self):
        all_keys = []
        
        for i in range(len(self.datamap)):
            if self.datamap[i] is not None:
                for j in range(len(self.datamap[i])):
                    all_keys.append(self.datamap[i][j][0])
        return all_keys
                    
            

my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)

# my_hash_table.get_item('bolts')
# my_hash_table.get_item('washers')
# my_hash_table.get_item('lumber')

print(my_hash_table.keys())



        
        
        
