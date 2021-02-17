class Factorial:
    
        def fun(self,val):
            mul = 1
            for i in range(2,val+1):
                mul = mul * i
            print(mul)
            
fact = Factorial()
list = [2,5,9,7,11]
if __name__ == "__main__":
    print("I'm running")
    for number in list:
        fact.fun(number)
    print(fact.__str__())
    print(fact.__repr__())
                
