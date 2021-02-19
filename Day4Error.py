# Handling value error

try:
    value = int(input("Enter a value: "))
except ValueError:
    print("Give number as input")
else:
    print("Correct Input")
finally:
    print("Successfully done")


print("\n")
#type error demo=============================
import math
value = input("Enter a value: ")
try:
    squareroot = math.sqrt(value)
    print(squareroot)
except TypeError:
    print("Give proper input")    


#Handling Key error ==================================
'''
print("\n")
dictionary = {"fruit":"Apple","car":"Ford"}
print(dictionary["subject"])
'''
    
print("\n")
#Demonstrating index error =============================
list = [1,2,3]
print(list[4])
