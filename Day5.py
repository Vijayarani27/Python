# Dunder methods =========================

print("\n")
def __add__(num1,num2):
    print("add :",num1 + num2)

def __len__(name):
    count = 0
    for i in name:
        count = count+1
    print("length of ",name,": ",count)   
        

def __eq__(num1,num2):
    print("equal :",num1 == num2)

def __mul__(num1,num2):
    print("multiply :",num1 * num2)

def __lt__(num1,num2):
    print("lesser than :",num1 < num2)

__add__(3,4)
__len__("Vijay")
__eq__(4,4)
__mul__(5,10)
__lt__(3,4)


#Decorators ===============================

import timeit
print("\n")
def decorator(function):
    def wrapper(*args,**kwargs):
        print("inner")
        start_time = timeit.default_timer()
        function(*args,**kwargs)
        end_time = timeit.default_timer()
        print("Execution time is : ", end_time-start_time)
    print("outer")
    return wrapper

@decorator
def function(value):
    for i in range(value):
        print(i)
        
function(5)


#Genertors =========================================

print("\n")
def fun(value):
    for i in range(value):
        yield i

func = fun(5)
print(func)
print(next(func))
print(next(func))
print(next(func))
print(next(func))
print(next(func))
print(next(func))
