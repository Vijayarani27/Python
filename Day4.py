#Reading CSV File
with open('Csvfile.csv') as file:
    for i in file:
        print(i)

# Traversing Current Directory =====================
print("\n")
import os
path = os.walk(".")
for files in path:
     for filename in files[2]:
         if '.py' in filename:
             print(filename)
        

# Standard lib sys ============================
print("\n")
import sys
print(sys.argv)


# Iterator ======================================
print("\n")
class Iterator:
    def __init__(self,data):
        self.data = data
        self.index = -2

    def __iter__(self):
        return self

    def __next__(self,it):
        if self.index  < len(self.data)-2:
            self.index = self.index + 2
            return self.data[self.index]
        else:
            raise StopIteration 
           
'''  
iterator = Iterator("Python")
it = iterator.__iter__()
print(iterator.__next__(it))
print(iterator.__next__(it))
print(iterator.__next__(it))
print(iterator.__next__(it))
'''

iterator = Iterator("Hello")
it = iterator.__iter__()
print(iterator.__next__(it))
print(iterator.__next__(it))
print(iterator.__next__(it))
print(iterator.__next__(it))

