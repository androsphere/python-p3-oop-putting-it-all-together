#!/usr/bin/env python3

class Shoe:
    condition = ""
    def __init__(self, brand, size):
        self.size = size
        self.brand = brand
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self,size):
        if type(size) ==int:
            self._size=size
        else:
            print("size must be an integer")

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
        
    

