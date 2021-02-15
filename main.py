names = ["john", "jake", "jack", "george", "jenny", "jason"]
for name in names:
  if len(name) < 5 and "e" not in name:
    print(name)


print("\n")
name = "python"
print("c" + name[1:])


print("\n")
dictionary = {"name": "python", "ext": "py", "creator":"guido"}
for item in dictionary:
  print("Key:"+item,"Value:"+dictionary[item])


print("\n")
for i in range(1,101):
  if i%3==0:
    print("Fizz")
  elif i%5==0:
    print("Buzz")
  elif i%3==0 and i%5==0:
    print("FizzBuzz")
  else:
    print(i)  


print("\n")
number = 100
guess = int(input("Enter the value:"))


if guess>100:
  print("You entered greater value")
else:
  print("You entered lesser value")
