#Guessing Game

number = 100
count = 0
guess=int(input("Enter the value:"))
while count<3:
    if guess<number:
        print("Your guess is lesser")
    elif guess>number:
        print("Your guess is greater")
    else:
        print("correct answer")
        break
    if count<2:
        guess=int(input("Enter the value:"))
    count = count+1   
else:
    print("Game Over")


#Value with index===================================
    
print("\n")
list = ['a','b','c','d']
for index,value in enumerate(list):
    print(index,":",value)


#Looping dictionary================================
    
print("\n")
dictionary = {"Maths":"Algebra","Car":"Ford","Fruit":"Apple"}
for k,v in dictionary.items():
    print(v ," belongs to ",k)


#else in while loop=================================
    
print("\n")
count = 1
while count<3:
    num=int(input("Enter the value:"))
    if num%2==0:
        print("You gave Even number")
    else:
        print("You gave Odd number")
        break
    count=count+1    
else:
    print("Successfully done!")


# add function =====================================

print("\n")
def add(num1,num2):
    """ Addition of two numbers """
    print(type(num1))
    return num1+num2
print("Addition : ",add(20,12))


# args function ===================================

print("\n")
def fruits(*args):
    for value in args:
        print(value)
fruits("Apple","Mango","Grape")


# kwargs function ===================================

print("\n")
def fun(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} -> {value}")
fun(Maths="Algebra",Car="Ford",Fruit="Apple")


# count of args function ===================================

print("\n")
def fruits(*args):
    print("Number of arguments passed: ",len(args))
    for value in args:
        print(value)
fruits()        
fruits("Apple")
fruits("Mango","Grape")
fruits("Apple","Mango","Grape")    
    

# Comprehension===================================

print("\n")
list = [1, 3, 3, 4, 5, 6]
comp=[i**2 for i in list if i%2!=0]
print(comp)
    

# Lambda function =================================

print("\n")
average = lambda total,count : total/count
print("Average : ",average(50,2))
